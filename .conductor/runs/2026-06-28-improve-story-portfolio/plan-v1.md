# Plan v1 — Story Portfolio v1.1 (Core package)

## Scope (locked by user)
1. Five signature beats with one peak (meaning-enacting animation)
2. Hall of Fame "drawer" staggers open
3. The Chapter Spine (re-readable narrative map at the end)
4. Embed the font (remove the external Google Fonts dependency)
Out of scope: sound tick, haptics, glow, grain (deferred). Story copy stays locked. Narrator character stays phase 2.

## File to modify
| File | Action | Notes |
|------|--------|-------|
| `index.html` | modify | The only file. Stays single, self-contained, dependency-free. |

(Any temporary font tooling happens outside the file; the shipped artifact remains one HTML file.)

## Approach

### 1. Signature beats (5 only, one peak)
- Extend each beat object with an optional `anim` key. Only these five carry it:
  - `"He fell so hard that he cut his head wide open."` → `anim: "drop"` (enters fast from above, heavier easing).
  - `"As his voice got deeper and his arms got bigger, his spirit grew smaller."` → `anim: "shrink"` (fades in, then scales down ~0.9 and settles).
  - `"Now the boy was afraid of falling."` → `anim: "hold"` (slower, heavier, no drift — a stillness).
  - PEAK: `"Hello. My name is Ali, and I'm the boy in the story."` → `anim: "reveal"` (a held beat, then the line settles in with a gentle scale + letter-spacing tighten; marks fairy-tale → real person).
  - `"So this is me, falling on purpose for the first time."` → `anim: "catch"` (drops, then catches with a small settle-back).
- Implementation: `render()` adds `beat.anim` as an extra class on the beat element. Each variant is a short CSS `@keyframes` (transform/opacity only, GPU-friendly). The existing exit (remove `.in`) is unchanged.
- `prefers-reduced-motion`: all five variants collapse to the standard fade. No exceptions.
- Every other line keeps the current uniform fade. Restraint is the point.

### 2. Hall of Fame drawer stagger
- On the `wall` beat, the four stats and the credential lines animate in sequence (each item: fade + 8px rise) using incremental `animation-delay` via `nth-child`, total stagger ≈ 0.5s.
- Pure CSS, triggered by the existing `.in` class on the wall. No JS timers. Reduced-motion → appear together.

### 3. The Chapter Spine
- Define `chapters = [{label, start}]` mapping to beat indices:
  - The Boy (0) · The Fear (7) · The Turn (13) · The Reveal (19) · The Work (23) · The Proof (31, the wall)
- During the story: the bottom progress bar shows faint segment ticks at chapter boundaries (a hint of structure), nothing tappable.
- On reaching the final beat (CTA): the bar transforms into the Spine — chapter labels fade in above it, each a tappable target. Tapping calls `jumpTo(start)` which sets the index and renders that beat (reuses existing render path + busy guard).
- "The Proof" segment is the Hall of Fame; it reads as unlocked once the end is reached.
- A small "restart / re-read" affordance is implicit (tap The Boy).
- Reliability: indexed jumps + DOM/CSS only. No new mechanics. Keyboard still works; spine is an enhancement, the linear flow is unchanged.

### 4. Embed the font
- Primary: fetch the specific Fraunces woff2 weights currently used (≈380 and 500), base64-encode, and inline them in a `@font-face` block via `data:` URIs. Remove the Google Fonts `<link>`. Result: zero external requests, look preserved, still one file.
- Guardrail: if total embedded size is unreasonable for a single file (target: keep added weight well under ~200KB), fall back to a curated system-serif stack (e.g. `'Iowan Old Style', 'Palatino', 'Georgia', serif`) and drop the external font entirely. Either way, the external dependency is gone.

## Assumptions
- Beat indices above match the current array; implementation will verify exact indices before wiring chapters.
- Embedding two static weights keeps size acceptable; otherwise system-serif fallback.

## Known Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Signature anims feel gimmicky | Low | Med | Hard cap of 5; reduced-motion fallback; one peak only |
| Anim variants clash with fade in/out timing | Med | Med | Variants affect ENTER only; exit path untouched; test each beat |
| Chapter Spine adds clutter | Low | Med | Hidden during story (only faint ticks); full spine only at the end |
| Font embed bloats file | Med | Low | Subset/limit to used weights; fallback to system serif if too big |
| Jank on low-memory Android | Low | Med | Transform/opacity only; no continuous loops |

## Acceptance Criteria
- [ ] Exactly five lines animate distinctly; all others use the standard fade.
- [ ] The peak reveal reads as a clear fairy-tale → real-person shift.
- [ ] Hall of Fame items stagger in; appear together under reduced-motion.
- [ ] At the end, a tappable chapter spine appears; each chapter jumps correctly.
- [ ] Linear tap/click/spacebar/arrow flow and invert toggle still work everywhere.
- [ ] No external network requests (font embedded or system stack).
- [ ] Reduced-motion and no-JS fallback still behave.
- [ ] Verified in browser on desktop, both themes.
