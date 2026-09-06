#!/usr/bin/env python3
"""Executable repository-canonicalization invariants.

These checks exist because the repository drifted once already: decision-relevant
research lived only on a side branch while the canonical docs asserted that
`main` was the only source of truth.

Stdlib only. Every invariant ships with a positive control so the run proves the
checker can fail, not merely that it passed.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --- frozen prompt blobs -----------------------------------------------------
# Git blob SHA-1, i.e. sha1(b"blob %d\0" % len(data) + data).
FROZEN_PROMPTS = {
    "prompts/SYSTEM.md": "339b9a1be2fd0f1f6f6c7960e5be58e5566d3691",
    "prompts/RND_AGENT_V0_1.md": "bc0e725d0449478d53b93bb6643d24404c22708c",
}

# --- documents whose claims decide what is currently true ---------------------
DECISION_RELEVANT_DOCS = [
    "README.md",
    "docs/CANONICAL_STATE.md",
    "docs/REPOSITORY_MAP.md",
]

# --- capabilities that must not become canonical without a promotion artifact -
UNEARNED_CAPABILITIES = {
    "Architecture Agent": "eval/architecture-agent/ARCHITECTURE_AGENT_PROMOTION.md",
    "Orchestrator": "docs/ORCHESTRATOR_PROMOTION.md",
    "Execution Agent": "docs/EXECUTION_AGENT_PROMOTION.md",
    "Requirements Agent": "docs/REQUIREMENTS_AGENT_PROMOTION.md",
}

# Directories where a production prompt or runnable agent implementation lives.
PRODUCTION_DIRS = ("prompts", "runtime")

# --- confirmation discipline --------------------------------------------------
CONFIRMATION_STREAM = "research/rnd-agent/scope-discovery/RND_SCOPE_CONFIRMATION_STREAM_V0_2.md"
CONFIRMATION_ADMISSION_TERMS = [
    "unseen",
    "blind",
    "different model lineage",
    "provenance",
]

# --- weakened-status vocabulary ----------------------------------------------
WEAK_STATUS_TOKENS = (
    "CANDIDATE",
    "DISCOVERY_ONLY",
    "NOT_VALIDATED",
    "CONFIRMATION_BLOCKED",
    "RESEARCH_HYPOTHESIS",
    "NOT_EARNED",
)
VALIDATED_SECTION_MARKERS = (
    "validated capabilities",
    "validated capability",
    "promoted capabilities",
)


class ContractError(ValueError):
    """A canonicalization invariant was violated."""


def fail(msg: str) -> None:
    raise ContractError(msg)


def require(condition: bool, msg: str) -> None:
    if not condition:
        fail(msg)


def read(rel: str) -> str:
    path = ROOT / rel
    require(path.is_file(), f"missing required file: {rel}")
    return path.read_text(encoding="utf-8")


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


# --- invariant 1: prompt freeze ----------------------------------------------

def check_prompt_freeze(overrides: dict[str, bytes] | None = None) -> None:
    """A frozen prompt is a comparator. Changing it silently destroys every
    result measured against it."""
    overrides = overrides or {}
    for rel, expected in FROZEN_PROMPTS.items():
        data = overrides.get(rel)
        if data is None:
            path = ROOT / rel
            require(path.is_file(), f"frozen prompt missing: {rel}")
            data = path.read_bytes()
        actual = git_blob_sha(data)
        require(
            actual == expected,
            f"frozen prompt changed: {rel}\n"
            f"  expected blob {expected}\n"
            f"  actual   blob {actual}\n"
            f"  a frozen comparator may only change through its own capability gate,\n"
            f"  and the recorded hash must move in the same commit",
        )


# --- invariant 2: canonical branch rule --------------------------------------

BRANCH_AS_TRUTH = re.compile(
    r"(source of truth|canonical|authoritative)[^.\n]{0,80}"
    r"\b(branch|refs?/heads)\b",
    re.IGNORECASE,
)
MAIN_EXEMPT = re.compile(r"\bmain\b", re.IGNORECASE)


def check_canonical_branch_rule(docs: dict[str, str] | None = None) -> None:
    """No decision-relevant document may name a side branch as current truth."""
    docs = docs if docs is not None else {rel: read(rel) for rel in DECISION_RELEVANT_DOCS}
    for rel, text in docs.items():
        for line in text.splitlines():
            match = BRANCH_AS_TRUTH.search(line)
            if not match:
                continue
            if MAIN_EXEMPT.search(line):
                continue
            fail(
                f"side branch named as current truth in {rel}:\n"
                f"  {line.strip()}\n"
                f"  only `main` may be described as canonical or authoritative"
            )


# --- invariant 3: status discipline ------------------------------------------

def check_status_discipline(docs: dict[str, str] | None = None) -> None:
    """A weakened status may not be laundered by listing the artifact under a
    validated-capabilities heading without an explicit promotion artifact."""
    docs = docs if docs is not None else {rel: read(rel) for rel in DECISION_RELEVANT_DOCS}
    for rel, text in docs.items():
        lines = text.splitlines()
        in_validated = False
        heading = ""
        for line in lines:
            if line.startswith("#"):
                heading = line
                in_validated = any(m in line.lower() for m in VALIDATED_SECTION_MARKERS)
                continue
            if not in_validated:
                continue
            for token in WEAK_STATUS_TOKENS:
                if token in line:
                    fail(
                        f"status laundering in {rel} under {heading.strip()!r}:\n"
                        f"  {line.strip()}\n"
                        f"  an artifact carrying {token} may not be listed as validated\n"
                        f"  without an explicit promotion artifact"
                    )


# --- invariant 4: confirmation discipline ------------------------------------

CONFIRMATORY_N = re.compile(r"CONFIRMATORY_N\s*=\s*(\d+)")


def read_confirmatory_n(text: str) -> int:
    matches = CONFIRMATORY_N.findall(text)
    require(bool(matches), f"{CONFIRMATION_STREAM} must state CONFIRMATORY_N explicitly")
    values = {int(m) for m in matches}
    require(
        len(values) == 1,
        f"{CONFIRMATION_STREAM} states conflicting CONFIRMATORY_N values: {sorted(values)}",
    )
    return values.pop()


def check_confirmation_discipline(text: str | None = None) -> None:
    """CONFIRMATORY_N may not rise without the four admission conditions being
    stated in the same document that carries the count."""
    text = read(CONFIRMATION_STREAM) if text is None else text
    n = read_confirmatory_n(text)
    if n == 0:
        return
    lowered = text.lower()
    missing = [t for t in CONFIRMATION_ADMISSION_TERMS if t not in lowered]
    require(
        not missing,
        f"CONFIRMATORY_N = {n} without stated admission conditions.\n"
        f"  missing from {CONFIRMATION_STREAM}: {', '.join(missing)}\n"
        f"  a count may only rise with an admitted case, a blinded comparator,\n"
        f"  independent adjudication and preserved provenance",
    )


# --- invariant 5+6: unearned capability creep --------------------------------

def production_files() -> list[Path]:
    files: list[Path] = []
    for d in PRODUCTION_DIRS:
        base = ROOT / d
        if not base.is_dir():
            continue
        files.extend(p for p in base.rglob("*") if p.is_file() and p.suffix in {".md", ".py"})
    return files


def _declaration_patterns(name: str) -> list[re.Pattern[str]]:
    """A capability is *declared* by a heading, a prompt identity line or a code
    definition. A mention inside prose, a deferral or a mock payload is not a
    declaration and must not trip this gate."""
    escaped = re.escape(name)
    ident = re.escape(name.replace(" ", ""))
    return [
        # markdown heading naming the capability
        re.compile(rf"^\s*#{{1,6}}\s+[^\n]{{0,30}}\b{escaped}\b", re.IGNORECASE),
        # prompt identity line
        re.compile(rf"^\s*(?:You are|Role|Identity|Agent|Name)\b[^\n]{{0,30}}\b{escaped}\b", re.IGNORECASE),
        # code definition
        re.compile(rf"^\s*(?:class|def)\s+\w*{ident}\w*\s*[(:]", re.IGNORECASE),
    ]


def check_unearned_capabilities(extra: list[tuple[str, str]] | None = None) -> None:
    """No production file may *declare* an unearned capability before its
    promotion artifact exists. Discussing or deferring it is allowed."""
    candidates: list[tuple[str, str]] = [
        (str(p.relative_to(ROOT)), p.read_text(encoding="utf-8")) for p in production_files()
    ]
    candidates.extend(extra or [])

    for name, promotion_ref in UNEARNED_CAPABILITIES.items():
        promoted = (ROOT / promotion_ref).is_file()
        patterns = _declaration_patterns(name)
        for rel, text in candidates:
            for line in text.splitlines():
                if not any(p.match(line) for p in patterns):
                    continue
                if _is_negated(line):
                    continue
                require(
                    promoted,
                    f"unearned capability declared in a production file: {rel}\n"
                    f"  {line.strip()}\n"
                    f"  {name} has no promotion artifact at {promotion_ref};\n"
                    f"  it may be discussed or deferred under research/ or docs/, not declared here",
                )


NEGATION = re.compile(
    r"\b(no|not|never|without|defer|deferred|unearned|NOT_EARNED|do not|don't|"
    r"forbidden|absent|instead of|rather than|category error|before implementing|"
    r"candidate|proposed|hypothetical|whether)\b",
    re.IGNORECASE,
)


def _is_negated(line: str) -> bool:
    return bool(NEGATION.search(line))


# --- invariant 7: README and CANONICAL_STATE must not contradict -------------

def check_no_orchestrator_claim() -> None:
    """Both top-level documents must still say the orchestrator is not built."""
    for rel in ("README.md", "docs/CANONICAL_STATE.md"):
        text = read(rel)
        require(
            re.search(r"orchestrator", text, re.IGNORECASE) is not None,
            f"{rel} no longer states the orchestrator's status",
        )
        require(
            re.search(r"orchestrator[^\n]{0,120}(not built|NOT_EARNED|deferred|do not build)", text, re.IGNORECASE)
            or re.search(r"(not built|NOT_EARNED|deferred|no learned)[^\n]{0,120}orchestrator", text, re.IGNORECASE),
            f"{rel} mentions an orchestrator without recording it as unbuilt",
        )


# --- positive controls -------------------------------------------------------

def positive_controls() -> int:
    """Prove each invariant can fail. A gate that cannot go red is not a gate."""
    controls: list[tuple[str, callable]] = [
        (
            "mutated-frozen-prompt",
            lambda: check_prompt_freeze({"prompts/SYSTEM.md": b"mutated frozen prompt\n"}),
        ),
        (
            "side-branch-as-truth",
            lambda: check_canonical_branch_rule(
                {"CONTROL.md": "The canonical branch is research/some-lane-2026-09-06."}
            ),
        ),
        (
            "status-laundering",
            lambda: check_status_discipline(
                {"CONTROL.md": "## Validated capabilities\n\n- Architecture: CANDIDATE\n"}
            ),
        ),
        (
            "confirmation-count-without-admission",
            lambda: check_confirmation_discipline("CONFIRMATORY_N = 12\n\nWe counted some cases.\n"),
        ),
        (
            "unearned-architecture-agent-implementation",
            lambda: check_unearned_capabilities(
                [("prompts/CONTROL.md", "You are the Architecture Agent.\n")]
            ),
        ),
        (
            "unearned-orchestrator-implementation",
            lambda: check_unearned_capabilities(
                [("runtime/CONTROL.md", "# Orchestrator\n")]
            ),
        ),
    ]

    for name, fn in controls:
        try:
            fn()
        except ContractError:
            print(f"CONTROL RED: {name}")
            continue
        fail(f"NOT-A-GATE: positive control stayed green: {name}")
    return len(controls)


def main() -> None:
    check_prompt_freeze()
    print("PROMPT FREEZE: " + ", ".join(f"{k} @ {v[:12]}" for k, v in FROZEN_PROMPTS.items()))

    check_canonical_branch_rule()
    print("CANONICAL BRANCH RULE: only `main` named as authoritative")

    check_status_discipline()
    print("STATUS DISCIPLINE: no weakened status listed as validated")

    n = read_confirmatory_n(read(CONFIRMATION_STREAM))
    check_confirmation_discipline()
    print(f"CONFIRMATION DISCIPLINE: CONFIRMATORY_N = {n}")

    check_unearned_capabilities()
    print("CAPABILITY CREEP: " + ", ".join(sorted(UNEARNED_CAPABILITIES)) + " remain unimplemented")

    check_no_orchestrator_claim()
    print("ORCHESTRATOR: recorded as unbuilt in README and CANONICAL_STATE")

    count = positive_controls()
    print(f"positive controls: {count}/{count} correctly failed")
    print("CANONICAL-STATE CONTRACT: PASS")


if __name__ == "__main__":
    main()
