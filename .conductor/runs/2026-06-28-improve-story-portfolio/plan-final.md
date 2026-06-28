# Final Plan: Story Portfolio v1.1 (Core package)

## Summary
Upgrade the single-file story portfolio so it feels authored and memorable, by making the page enact the story: five signature lines whose motion performs their meaning (one true peak at the identity reveal), the Hall of Fame "drawer" staggering open, and a Chapter Spine that turns the finished page into a re-readable narrative object. Remove the last external dependency by self-hosting the font. Every change is indexed jumps, CSS transforms/opacity, and progressive enhancement, so it stays unbreakable. Incorporates all seven points from Codex's plan review.

## Why This Works
The "never seen this" reaction comes from congruence, not spectacle: a copywriter's site that behaves like the writing. Because the effects are small and semantic, they are cheap and reliable. Codex's review hardened the two real risk areas (animation/exit conflicts and the Spine's click handling), which the architecture below resolves directly.

## Approach

### Phase 1 — Inner-wrapper refactor (enables safe signature animation)
- Each beat renders as `.beat` (outer) wrapping `.beat-content` (inner).
- The OUTER `.beat` keeps full ownership of enter/exit: `.in` drives the opacity 0→1 and translateY fade; exit removes `.in` exactly as today. Untouched timing (0.65s enter, 280ms exit, `busy` guard).
- Signature animations run ONLY on the INNER `.beat-content`, so they never collide with the outer fade/exit.

### Phase 2 — Five signature beats (one peak)
- Add `anim` to exactly five beats: `drop` (cut his head open), `shrink` (spirit grew smaller), `hold` (afraid of falling), `reveal` (PEAK: "I'm the boy in the story"), `catch` (falling on purpose).
- Each is a one-shot CSS `@keyframes` on `.beat-content` that **resolves to `transform: none` / normal letter-spacing** at 100%, so when the outer `.beat` later exits, nothing snaps (Codex #1, #2).
- `prefers-reduced-motion`: inner animations disabled; standard fade only.
- All other lines: unchanged uniform fade.

### Phase 3 — Hall of Fame drawer stagger
- On the wall beat, stats and credential rows fade+rise in sequence via `nth-child` `animation-delay` (~0.5s total), triggered by the outer `.in`. Reduced-motion → appear together.

### Phase 4 — Chapter Spine (with Codex's state rules)
- `chapters = [{label, start}]`: The Boy(0) · The Fear(7) · The Turn(13) · The Reveal(19) · The Work(23) · The Proof(wall). Exact indices verified against the array before wiring.
- Story mode: thin progress bar with faint, non-interactive ticks at chapter boundaries.
- End mode: only when `idx === beats.length - 1`, the bar reveals tappable chapter labels (`<button>`s).
- `jumpTo(start)`: `if (busy) return;` set `i = start`; `render(i)`; update progress width immediately; return UI to story mode (labels hidden) since every chapter start precedes the end. Reader then continues linearly; the Spine returns when they reach the end again (Codex #4, #5).
- Spine buttons call `e.stopPropagation()`, and the document-click advance handler excludes the spine container, so a tap never also triggers `next()` (Codex #3).

### Phase 5 — Self-host the font (remove external dependency)
- Embed the Fraunces Latin woff2 for the used weights (~380, ~500) as base64 `@font-face` `data:` URIs; delete the Google Fonts `<link>`. Use only the Latin subset shard (small), not all unicode-range shards.
- Hard cutoff: if added weight exceeds ~150KB, drop the embed and ship a curated system-serif stack (`'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif`). Either path: zero external requests (Codex #6).
- `<noscript>` full-story fallback stays; Spine/progress markup is JS-built so no inert controls appear without JS; verify readability with the new font/fallback (Codex #7).

## Files to Create/Modify
| File | Action | Purpose |
|------|--------|---------|
| `index.html` | modify | All changes. Stays one self-contained, dependency-free file. |

## Decisions Log
- Animations on inner wrapper, not the beat element (Codex).
- Spine is end-state only; jumps return to story mode (Codex).
- Font self-hosted (subset) with system-serif fallback over the size cap (Codex).

## Known Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Variant anim snaps on exit | Low | Med | Inner wrapper; all variants end at transform:none |
| Spine tap double-advances | Low | Med | stopPropagation + handler excludes spine |
| jumpTo race mid-transition | Low | Med | `if (busy) return` |
| Stale Spine labels after jump | Low | Low | Labels only when `idx === last` |
| Font embed bloat | Med | Low | Latin subset only; 150KB cap; system-serif fallback |
| Jank on low-memory Android | Low | Med | transform/opacity only; one-shot, no loops |

## Acceptance Criteria
- [ ] Exactly five lines animate distinctly; the reveal reads as fairy-tale → real person; all others standard fade.
- [ ] No snap/flicker when leaving a signature beat (exit clean).
- [ ] Hall of Fame staggers in; appears together under reduced-motion.
- [ ] Chapter Spine appears only at the end; each chapter jumps correctly; a Spine tap never also advances.
- [ ] jumpTo ignored while busy; progress correct after jumps; story mode restored after a jump.
- [ ] No external network requests (font embedded or system stack).
- [ ] Linear tap/click/spacebar/arrows + invert still work everywhere; reduced-motion + no-JS intact.
- [ ] Verified in browser, desktop, both themes; spot-checked narrow width.

---
*Resolves all 7 issues from Codex's plan review. Awaiting user "execute" to proceed to implementation.*
