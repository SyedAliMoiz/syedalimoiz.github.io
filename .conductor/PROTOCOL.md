# Conductor Protocol v3.0

A two-AI collaboration system where Claude (Writer) and Codex (Reviewer) iterate autonomously until consensus, with full documentation trail.

## How to Start

**Trigger**: User says `/conduct` followed by their goal.

**Example**:
```
/conduct I want to add a dark mode toggle to the settings page
```

**What happens**:
1. Writer (Claude) creates a run folder and `context.md`
2. Writer adds **Understanding Check** (MANDATORY): "So you want X to happen so that Y can happen?"
3. Both agents add any additional clarifying questions (optional)
4. **User confirms understanding** + answers any questions
5. Agents iterate autonomously (research → plan) until consensus
6. User reviews `plan-final.md`
7. User says "execute" to start implementation

**User involvement**:
- Start: state goal
- Stage 0: **confirm understanding check** (MANDATORY) + answer any additional questions
- End of planning: review `plan-final.md`, say "execute"
- Done: review completed work

## Roles (Fixed Per Session)

| Role | Agent | Responsibility |
|------|-------|----------------|
| **Writer** | Claude | Proposes research, plans, approaches. Revises based on critique. |
| **Reviewer** | Codex | Stress-tests, finds gaps, identifies risks. Rates APPROVED or NEEDS WORK. |

## Stages (Aligned with AGENTS.md)

| Stage | Name | Description |
|-------|------|-------------|
| 0 | context | Gather goal, clarifying questions, user answers |
| 1 | research | Analyze codebase, iterate until APPROVED |
| 2 | planning | Design approach, iterate until APPROVED, then user says "execute" |
| 3 | implementation | Write code, review until APPROVED |
| 4 | complete | Done |

**Note**: User approval ("execute") happens at the END of Stage 2, before transitioning to Stage 3. It's a gate, not a separate stage.

## File Structure

```
.conductor/
├── PROTOCOL.md          # This file (full spec)
├── config.json          # Global settings
├── state.json           # ACTIVE RUN POINTER + stage + history
├── TEMPLATE.md          # Starter templates
├── invoke-codex.sh      # Helper script
└── runs/
    └── <YYYY-MM-DD>-<slug>/
        ├── run.md               # Manifest with links to latest artifacts
        ├── context.md           # Goal, why, constraints, assumptions
        ├── questions.md         # Both AIs' questions (locked after answers)
        ├── answers.md           # User's answers (one-time)
        ├── research-v1.md       # Writer's research draft
        ├── research-v1-review.md# Reviewer's critique
        ├── research-final.md    # Copy of approved version
        ├── plan-v1.md           # Writer's plan draft
        ├── plan-v1-review.md    # Reviewer's critique
        ├── plan-final.md        # Created after plan APPROVED, BEFORE user "execute" (for user review)
        ├── code-review.md       # Reviewer's code review (Stage 3)
        └── state.json           # Run-local state (detailed)
```

## State Tracking

### Top-Level: `.conductor/state.json`
```json
{
  "active_run": "2026-01-17-feature-x",
  "stage": 1,
  "stage_name": "research",
  "awaiting": "reviewer",
  "last_updated": "2026-01-17T10:30:00Z",
  "history": [
    {
      "stage": 0,
      "actor": "codex",
      "action": "completed",
      "rating": "APPROVED",
      "timestamp": "2026-01-17T10:00:00Z"
    }
  ]
}
```

### Run-Level: `runs/<run>/state.json`
```json
{
  "stage": 1,
  "stage_name": "research",
  "iteration": 2,
  "current_file": "research-v2.md",
  "awaiting": "reviewer",
  "approved_research": null,
  "approved_plan": null,
  "user_approved": false,
  "started": "2026-01-17T00:00:00Z",
  "last_updated": "2026-01-17T10:30:00Z"
}
```

### Stage Transitions (Reviewer Updates)

After writing a review, Reviewer updates **BOTH** state files:

**Top-level `.conductor/state.json`**:
- Set `last_updated` to current ISO timestamp
- Add entry to `history` array
- Update `stage` and `stage_name` if APPROVED

**Run-level `runs/<run>/state.json`**:
- Set `last_updated` to current ISO timestamp
- Update `iteration`, `current_file`, `awaiting`
- If APPROVED, set `approved_research` or `approved_plan` to the approved version

**Stage transitions** (only on APPROVED):
- 0 → 1: "context" → "research"
- 1 → 2: "research" → "planning"
- 2 → 3: "planning" → "implementation" (requires user "execute" first — see below)
- 3 → 4: "implementation" → "complete"

### User "Execute" Gate (Stage 2 → 3)

When plan is APPROVED but before advancing to Stage 3:
1. Writer presents `plan-final.md` to user
2. User says **"execute"**
3. Writer sets `user_approved: true` in run-level state.json
4. Reviewer then advances stage to 3 (implementation)

---

## Workflow

### Stage 0: Context & Clarification
1. User says `/conduct` and states high-level goal (what and why)
2. Writer creates run folder, updates top-level `state.json` with `active_run`
3. Writer creates `context.md` with goal, constraints, and initial **Assumptions**
4. Writer creates `run.md` manifest
5. **Understanding Check (MANDATORY)**:
   - Writer adds an understanding confirmation to `questions.md`:
     > "So you want [X change] to happen so that [Y meta-goal] can happen?"
   - Example: "So you want the user message to persist after the assistant starts responding, so that users don't lose their sent message, so that they have a familiar and positive chat experience?"
   - This is ALWAYS required, even for simple tasks
6. **Additional Questions (OPTIONAL)**:
   - Writer adds clarifying questions if any (max 3)
   - Writer invokes Reviewer to add questions (max 3)
7. **Wait for user confirmation**:
   - User confirms understanding check (yes/corrects it)
   - User answers any additional questions
8. Once confirmed/answered, questions are **locked** — see "Scope Change Protocol" if reopening needed
9. **Stage 0 completion**: Reviewer updates state to advance to Stage 1
   - No review artifact for Stage 0 (tracked in state/history only)
   - History entry: `{"stage": 0, "actor": "codex", "action": "completed", "rating": "APPROVED", ...}`

**Note**: Even simple tasks require the understanding check. The goal chain confirmation ensures both agents truly understand the user's intent before proceeding.

### Stage 1: Research
1. Writer drafts `research-v1.md` (codebase analysis, patterns, constraints, dependencies)
2. Reviewer writes `research-v1-review.md` with rating
3. If `NEEDS WORK` → Writer revises to `research-v2.md`, repeat
4. If `APPROVED` → Writer copies approved version to `research-final.md`
5. Reviewer updates state → advance to Stage 2
6. Max 5 iterations before **escalation**

### Stage 2: Planning
1. Writer drafts `plan-v1.md` (approach, files to change, risks, milestones, test criteria)
2. Reviewer writes `plan-v1-review.md` with rating
3. If `NEEDS WORK` → Writer revises to `plan-v2.md`, repeat
4. If `APPROVED`:
   - Writer creates `plan-final.md` with full rationale (for user review)
   - Present `plan-final.md` to user
   - **Wait for user to say "execute"**
   - Writer sets `user_approved: true` in run-level state
   - Reviewer then updates state → advance to Stage 3
5. Max 5 iterations before **escalation**

**Timeline**: plan APPROVED → plan-final.md created → user reviews → user says "execute" → Stage 3 begins

### Stage 3: Implementation
1. Writer implements according to `plan-final.md`
2. Reviewer performs code review, writes `code-review.md`
3. If `NEEDS WORK` → Writer fixes issues, repeat
4. If `APPROVED` → Reviewer updates state → advance to Stage 4 (complete)

### Stage 4: Complete
- Session done
- All artifacts preserved in run folder

---

## Review Format (REQUIRED)

Reviewer MUST use this exact format (Rating at END):

```markdown
# [Stage] Review

## Summary
[1-2 sentence overview of what you reviewed]

## What's Good
- [Positive point 1]
- [Positive point 2]

## Issues Found
1. **[Issue title]**: [Description and why it matters]
2. **[Issue title]**: [Description and why it matters]

## Questions
- [Any clarifying questions about the content]

## Suggestions
- [Optional improvements, clearly marked as optional]

---

**Rating: APPROVED** or **Rating: NEEDS WORK**

[If NEEDS WORK, list the specific items that must be addressed]
```

---

## Scope Change Protocol

Questions are locked after Stage 0, but scope can be reopened if:

1. **Trigger**: Writer or Reviewer discovers the current scope is unworkable
2. **Process**:
   - Document reason in history with action: `scope-change-requested`
   - Add new questions to `questions.md` under `## Scope Change Questions`
   - Set `awaiting: user` in both state files
   - User provides answers in `answers.md` under `## Scope Change Answers`
   - Resume from current stage (don't restart)
3. **Limit**: Max 2 scope changes per run

---

## Escalation Protocol (Stalemate Handling)

When iteration cap (5) is reached without APPROVED:

1. **Writer creates `escalation.md`** containing:
   - Summary of the disagreement
   - Option A: Writer's preferred approach + tradeoffs
   - Option B: Reviewer's preferred approach + tradeoffs
   - Option C: Compromise approach (if possible)
   - Recommendation with reasoning

2. **User chooses** one of the options

3. **Resume** with chosen approach, reset iteration count

---

## Quick Reference Tables

### Writer (Claude) Actions

| Stage | Read | Write |
|-------|------|-------|
| 0 | - | context.md, questions.md, run.md |
| 1 | answers.md, review files | research-v1.md, research-v2.md, research-final.md |
| 2 | research-final.md, review files | plan-v1.md, plan-v2.md, plan-final.md |
| 3 | plan-final.md, code-review.md | actual code changes |

### Reviewer (Codex) Actions

| Stage | Read | Write |
|-------|------|-------|
| 0 | context.md | questions.md (add to it) |
| 1 | research-vN.md | research-vN-review.md |
| 2 | plan-vN.md | plan-vN-review.md |
| 3 | code changes | code-review.md |

---

## Context.md Required Sections

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

## Plan-Final.md Required Sections

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

---

## Guardrails

1. **No coding until user says "execute"** — Implementation only after plan-final.md reviewed and approved by user
2. **Iteration cap** — Max 5 iterations per stage before escalation
3. **Locked questions** — Use Scope Change Protocol if critical new questions arise
4. **Consistent ratings** — Only APPROVED or NEEDS WORK
5. **Final files gated**:
   - `research-final.md` — after research APPROVED
   - `plan-final.md` — after plan APPROVED (before user "execute", for review)
6. **One active run** — Top-level state.json ensures both agents work on same run
7. **Rating at END** — Review files must end with the rating line

---

## Invoking Codex (for Writer)

**Required model**: `gpt-5.2-codex` with `high` reasoning effort

```bash
# Using helper script (model pre-configured)
./.conductor/invoke-codex.sh <run-folder> <action>

# Or directly
codex exec "<prompt>" \
    --model gpt-5.2-codex \
    -c model_reasoning_effort='"high"' \
    --sandbox workspace-write \
    -C /path/to/project
```
