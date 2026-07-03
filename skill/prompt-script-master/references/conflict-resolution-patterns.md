# Conflict Resolution Patterns (2026-07-03)

## Pattern 1: Boundary Note (边界注释)

**Symptom**: File A says "rule X", file B implies "not X". Both files are correct within their own scope, but the scope isn't explicitly stated.

**Examples from this audit**:
- `final-prompt-purity.md` says "final prompt must be pure" → implies "one paragraph"
- Time axis rules require multi-segment output
- Resolution: Added note clarifying "purity applies to FINAL output to video model, NOT to intermediate products shown to user for confirmation"

- `dynamic-level-guide.md` says "auto-suggest" → implies "agent decides"
- `confirmation-gate.md` says "must wait for user confirm" → implies "don't decide"
- Resolution: Added cross-reference: "suggestion belongs here, confirmation belongs there"

**Pattern**: Add a `> **边界说明**：` blockquote at the top of the conflicting file, clarifying which domain the rule applies to and which domain it doesn't.

## Pattern 2: Cross-Reference (交叉引用)

**Symptom**: Two files describe complementary phases of the same workflow, but neither references the other, creating apparent conflict.

**Resolution**: Add a `> **流程衔接**：` blockquote linking the two files: "This file handles phase A; phase B is handled by <other file>. Flow: A → B."

## Pattern 3: Authority Deduplication

**Symptom**: Three files all define the same rule slightly differently (e.g., timeline splitting: fixed 0-2s/2-5s vs 0-3s/3-7s/7-10s vs flexible).

**Resolution**: Choose ONE authoritative file, rewrite it definitively, then update all other files to reference it rather than re-stating the rule.

## Full-warehouse Grep Verification

After any rule change, don't trust a checklist alone. Run:
```bash
rg "<old keyword pattern>" --glob '!*.bak' --glob '!.git'
```
If results appear, those files need inspection.
