# Run Folder Template

When starting a new run, create folder: `runs/<YYYY-MM-DD>-<slug>/`

---

## run.md (Manifest)

```markdown
# Run: <slug>

**Status**: context | research | planning | implementation | complete
**Started**: <date>
**Last Updated**: <date>

## Latest Artifacts
- Context: [context.md](./context.md)
- Questions: [questions.md](./questions.md) | [answers.md](./answers.md)
- Research: [research-vN.md](./research-vN.md) ← latest | [research-final.md](./research-final.md)
- Plan: [plan-vN.md](./plan-vN.md) ← latest | [plan-final.md](./plan-final.md)
- Code Review: [code-review.md](./code-review.md) (Stage 3)
- Escalation: [escalation.md](./escalation.md) (if stalemate)

## Quick Links
- [State](./state.json)
```

---

## context.md

```markdown
# Context

## Goal
What are we trying to accomplish?

## Why
Why does this matter? What problem does it solve?

## Current State
What exists now?

## Desired State
What should exist after?

## Constraints
Any limitations, requirements, or boundaries?

## Success Criteria
How do we know we're done?

## Assumptions
Things we're assuming to be true:
-

## Decisions Log
Key decisions made during this run:
- (populated during research/planning)

## Open Questions (Locked)
Questions we couldn't fully answer but proceeded anyway:
- (populated if needed)
```

---

## questions.md

```markdown
# Clarifying Questions

## Understanding Check (MANDATORY)
So you want [X change] to happen so that [Y meta-goal] can happen?

<!-- Example: "So you want the user message to persist after the assistant starts responding, so that users don't lose their sent message, so that they have a familiar and positive chat experience?" -->

## Writer (Claude) Questions
<!-- Additional clarifying questions, or "No additional questions" -->

## Reviewer (Codex) Questions
<!-- Additional clarifying questions, or "No additional questions" -->

---
*Questions locked after user confirms understanding and answers questions. See Scope Change Protocol if reopening needed.*

## Scope Change Questions
<!-- Only used if scope change is triggered mid-session -->
```

**Minimum required** (even for simple tasks):
```markdown
# Clarifying Questions

## Understanding Check (MANDATORY)
So you want [specific change] to happen so that [user's meta-goal] can happen?

## Writer (Claude) Questions
No additional questions.

## Reviewer (Codex) Questions
No additional questions.
```

---

## answers.md

```markdown
# Answers

## Understanding Check Confirmation
<!-- User confirms: "Yes" or corrects: "No, actually I want..." -->

## To Writer (Claude) Questions
<!-- User answers here, or "N/A - no additional questions" -->

## To Reviewer (Codex) Questions
<!-- User answers here, or "N/A - no additional questions" -->

## Scope Change Answers
<!-- Only used if scope change is triggered mid-session -->
```

**Minimum required** (even for simple tasks):
```markdown
# Answers

## Understanding Check Confirmation
Yes, that's correct.

## To Writer (Claude) Questions
N/A - no additional questions.

## To Reviewer (Codex) Questions
N/A - no additional questions.
```

---

## state.json (Run-Level)

```json
{
  "stage": 0,
  "stage_name": "context",
  "iteration": 1,
  "current_file": "context.md",
  "awaiting": "user",
  "approved_research": null,
  "approved_plan": null,
  "user_approved": false,
  "started": "<timestamp>",
  "last_updated": "<timestamp>"
}
```

---

## Review Template (for Reviewer)

```markdown
# [Stage] Review

## Summary
[1-2 sentence overview of what you reviewed]

## What's Good
-

## Issues Found
1. **[Issue title]**: [Description]

## Questions
-

## Suggestions
-

---

**Rating: APPROVED** or **Rating: NEEDS WORK**

[If NEEDS WORK, list specific items to address]
```

---

## escalation.md (if needed)

```markdown
# Escalation: [stage] Stalemate

## Summary of Disagreement
What we couldn't agree on after [N] iterations.

## Option A: Writer's Approach
**Description**:
**Tradeoffs**:
- Pro:
- Con:

## Option B: Reviewer's Approach
**Description**:
**Tradeoffs**:
- Pro:
- Con:

## Option C: Compromise (if possible)
**Description**:
**Tradeoffs**:
- Pro:
- Con:

## Recommendation
[Which option and why]
```

---

## plan-final.md Template

```markdown
# Final Plan: [feature/task name]

## Summary
One paragraph describing the agreed approach.

## Why This Works
Rationale for why this approach was chosen.

## Approach
### Phase 1: [name]
-
### Phase 2: [name]
-

## Files to Create/Modify
| File | Action | Purpose |
|------|--------|---------|

## Assumptions
-

## Decisions Log
-

## Known Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

---
*Approved by Reviewer. Awaiting user "execute" to proceed to implementation.*
```
