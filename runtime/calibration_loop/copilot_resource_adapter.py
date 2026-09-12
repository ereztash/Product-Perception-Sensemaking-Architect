#!/usr/bin/env python3
"""Best-effort GitHub Copilot CLI execution adapter for the canonical Calibration Loop.
Execution plumbing only; canonical peer prompts, routing, schemas and authority rules remain unchanged.
"""
from __future__ import annotations
import json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODEL = os.environ.get("COPILOT_MODEL", "").strip()
EFFORT = os.environ.get("COPILOT_REASONING_EFFORT", "").strip()
DEFAULT_PROMPTS = {"RND": "prompts/RND_AGENT_V0_2_CANDIDATE.md", "NETA": "prompts/SYSTEM.md"}
DELTA_KEYS = {"decision", "action", "reversal", "evidence", "allocation", "distinction"}
NEED_KEYS = {
    "signal_interpretation_ambiguity", "multiple_plausible_mechanisms", "proxy_substitution_risk",
    "research_to_intervention_transition", "broad_reasoning_needed", "architecture_alternatives_needed",
    "novel_synthesis_needed", "external_research_needed", "owner_authority_needed", "repo_authority_needed",
    "environment_authority_needed", "field_authority_needed",
}

class AdapterError(RuntimeError): pass

def safe_text(ref: str) -> str:
    p = (ROOT / ref).resolve()
    try: p.relative_to(ROOT.resolve())
    except ValueError as exc: raise AdapterError(f"reference escapes repository: {ref}") from exc
    if not p.is_file(): raise AdapterError(f"reference not found: {ref}")
    return p.read_text(encoding="utf-8")

def bridge(resource: str, phase: object) -> str:
    if resource == "RND" and phase == "DIAGNOSE":
        return """# Runtime bridge contract
Return exactly ONE JSON object and no Markdown with exactly these top-level fields: material_question, bottleneck, resource_assessment, candidate_moves, needs, rationale.
resource_assessment must be a non-empty array; EACH item must contain EXACTLY: resource (string), expected_contribution (string), authority_ceiling (string), uncertainty (string), expected_delta (object). expected_delta must contain EXACTLY six boolean keys: decision, action, reversal, evidence, allocation, distinction.
candidate_moves must be a non-empty array; EACH item exactly: move, resource, expected_decision_value, reversibility (all strings).
needs must contain EXACTLY these boolean keys: signal_interpretation_ambiguity, multiple_plausible_mechanisms, proxy_substitution_risk, research_to_intervention_transition, broad_reasoning_needed, architecture_alternatives_needed, novel_synthesis_needed, external_research_needed, owner_authority_needed, repo_authority_needed, environment_authority_needed, field_authority_needed.
Do not add fields. Diagnose this frozen Construct Separation Audit task. The question is not how many distinctions can be named; it is which distinctions materially change evidence eligibility, intervention, claim boundary, product action, or resource allocation, and what cheapest discriminator resolves each live ambiguity."""
    if resource == "RND" and phase == "SYNTHESIZE":
        return """# Runtime bridge contract
Return exactly ONE JSON object and no Markdown with exactly: decision_before, decision_after, next_move, resource_deltas, learning_records, stop_or_continue, routing_amendment_proposed.
resource_deltas must preserve routed-resource order exactly. EACH item must contain EXACTLY: resource (string), material (boolean), unique_delta (string), observed_delta (object). observed_delta must contain EXACTLY six keys: decision, action, reversal, evidence, allocation, distinction; each value is either null or a non-empty string. material must equal whether any observed_delta value is non-null.
learning_records is an array. stop_or_continue is STOP or CONTINUE. routing_amendment_proposed is normally null.
Preserve disagreements and authority ceilings. Role-conditioned agreement is not independent triangulation. Synthesize whether Construct Separation Audit earned promotion as a recurring method, which candidate cases are P0/P1/P2/P3, and which distinctions are premature. The next move must be the cheapest decision-changing move, not a request to instrument everything."""
    if resource == "NETA" and phase == "ANALYZE":
        return """# Runtime bridge contract
Return exactly ONE JSON object and no Markdown with exactly: resource:"NETA", summary (string), unique_delta (string), evidence_refs (array of strings, only refs present in request), limitations (array of strings).
Analyze the frozen Construct Separation Audit independently under Neta's canonical method. For EACH candidate C1-C10, distinguish observable from interpretation, name plausible competing mechanisms, state the cheapest discriminator, and state whether the distinction changes a product/design/evidence decision. Explicitly rank P0 evidence-contamination, P1 wrong-intervention, P2 wrong-perception, and P3 semantic-hygiene cases. Try to falsify the meta-rule by identifying cases where separation adds no useful discrimination. Pay special attention to intention vs executed move; decision time vs motor/UI time; engine disagreement vs cognitive error vs technical slip; opponent strength vs realism vs subjective challenge vs pedagogical targeting; legal choice vs meaningful decision; confidence/competence/calibration; recall/understanding/reported application/observed application; negative observation vs negative state; progress aliases; and player behavior vs product-elicited behavior. Do not infer FIELD facts not present in the frozen task, and do not recommend telemetry unless its expected decision value exceeds its measurement/intervention contamination cost. End with a ranked set of separations that should affect the active lichess_app process redesign and a verdict on whether the meta-method earns explicit recurring use."""
    raise AdapterError(f"unsupported resource/phase: {resource}/{phase}")

def extract_json(text: str) -> dict:
    raw = text.strip()
    m = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", raw, flags=re.DOTALL | re.IGNORECASE)
    if m: raw = m.group(1).strip()
    try: value = json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        if start < 0: raise AdapterError(f"Copilot returned no JSON object: {raw[:1000]}")
        try: value, _ = json.JSONDecoder().raw_decode(raw[start:])
        except json.JSONDecodeError as exc: raise AdapterError(f"Copilot returned invalid JSON: {raw[:1000]}") from exc
    if not isinstance(value, dict): raise AdapterError("semantic output must be one JSON object")
    return value

def nonempty(v: object) -> bool: return isinstance(v, str) and bool(v.strip())

def validate_delta(d: object, observed: bool) -> bool:
    if not isinstance(d, dict) or set(d) != DELTA_KEYS: return False
    return all((v is None or nonempty(v)) if observed else isinstance(v, bool) for v in d.values())

def validate(resource: str, phase: object, p: dict) -> None:
    if resource == "RND" and phase == "DIAGNOSE":
        required = {"material_question", "bottleneck", "resource_assessment", "candidate_moves", "needs", "rationale"}
        if set(p) != required: raise AdapterError(f"RND diagnosis fields drift: {sorted(set(p) ^ required)}")
        if not all(nonempty(p[k]) for k in ("material_question", "bottleneck", "rationale")): raise AdapterError("RND diagnosis strings empty")
        for item in p.get("resource_assessment", []):
            if set(item) != {"resource","expected_contribution","authority_ceiling","uncertainty","expected_delta"} or not validate_delta(item.get("expected_delta"), False): raise AdapterError("RND resource_assessment shape drift")
        if not isinstance(p["needs"], dict) or set(p["needs"]) != NEED_KEYS or not all(isinstance(v, bool) for v in p["needs"].values()): raise AdapterError("RND diagnosis needs shape drift")
        return
    if resource == "RND" and phase == "SYNTHESIZE":
        required = {"decision_before", "decision_after", "next_move", "resource_deltas", "learning_records", "stop_or_continue", "routing_amendment_proposed"}
        if set(p) != required or p.get("stop_or_continue") not in {"STOP", "CONTINUE"}: raise AdapterError("RND synthesis shape drift")
        for item in p.get("resource_deltas", []):
            if set(item) != {"resource","material","unique_delta","observed_delta"} or not validate_delta(item.get("observed_delta"), True): raise AdapterError("RND resource_deltas shape drift")
        return
    if resource == "NETA" and phase == "ANALYZE":
        required = {"resource", "summary", "unique_delta", "evidence_refs", "limitations"}
        if set(p) != required or p.get("resource") != "NETA" or not nonempty(p.get("summary")) or not nonempty(p.get("unique_delta")): raise AdapterError("NETA semantic shape drift")
        return
    raise AdapterError(f"unsupported validation target: {resource}/{phase}")

def main() -> int:
    try:
        request = json.load(sys.stdin)
        if not isinstance(request, dict): raise AdapterError("stdin must contain one JSON object")
        resource, phase = request.get("resource"), request.get("phase")
        if resource not in DEFAULT_PROMPTS: raise AdapterError(f"unsupported resource: {resource}")
        parts = [safe_text(request.get("prompt_ref") or DEFAULT_PROMPTS[resource])]
        if request.get("telos_ref"): parts.append("# Referenced telos document\n" + safe_text(request["telos_ref"]))
        parts += [bridge(resource, phase), "# Runtime request\n" + json.dumps(request, ensure_ascii=False, sort_keys=True, indent=2)]
        command = ["copilot", "-p", "\n\n".join(parts), "-s", "--no-ask-user", "--no-custom-instructions"]
        if MODEL: command += ["--model", MODEL]
        if EFFORT: command += ["--effort", EFFORT]
        proc = subprocess.run(command, text=True, capture_output=True, check=False)
        if proc.returncode != 0: raise AdapterError(f"Copilot CLI failed: {(proc.stderr.strip() or proc.stdout.strip())[:3000]}")
        semantic = extract_json(proc.stdout); validate(resource, phase, semantic)
        print(json.dumps(semantic, ensure_ascii=False))
        print(json.dumps({"adapter_provider":"github-copilot-cli","model":MODEL or "provider-default","effort":EFFORT or "provider-default","resource":resource,"phase":phase}), file=sys.stderr)
        return 0
    except (AdapterError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"adapter_error": str(exc)}, ensure_ascii=False), file=sys.stderr); return 2

if __name__ == "__main__": raise SystemExit(main())
