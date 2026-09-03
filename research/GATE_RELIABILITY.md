# Research gate reliability

This file records whether the research quarantine gate has demonstrated that it can fail for the reasons it claims to detect.

## 2026-09-03 · first run

**Result: RED — correctly blocked the PR, but exposed a defect in the gate itself.**

The research contract shipped with five deliberate positive controls. Four went red. One stayed green:

```text
fixture-ready-without-fixture
```

The control promoted a claim to `FIXTURE_READY` while setting:

```python
fixture_path = None
```

The validator checked:

```python
bool(str(c.get("fixture_path", "")).strip())
```

`str(None)` is the non-empty string `"None"`, so the invalid candidate passed.

CI therefore stopped with:

```text
NOT-A-GATE: positive control stayed green: fixture-ready-without-fixture
```

## Repair

The contract, not the control, was repaired.

A single helper now requires an actual non-empty string:

```python
def nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())
```

All promotion fields that require text now use that predicate.

## Second run

**Result: GREEN.**

- canonical Neta contract: green
- canonical research candidate: green
- research positive controls: **5/5 red as intended**
- PR CI: green
- post-merge `main` CI for the preregistration commit: green

## Why this incident is retained

A gate that merely exists is not evidence that it gates.

The first run demonstrated exactly the Lessons/Lichess failure mode this repository is supposed to inherit: a validator can contain the right-looking rule and still be unable to observe the invalid state it claims to reject.

This history stays here rather than being rewritten as if the first implementation had worked.
