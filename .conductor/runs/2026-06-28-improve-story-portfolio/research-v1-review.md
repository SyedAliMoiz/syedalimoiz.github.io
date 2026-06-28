# Research v1 Review (Codex, gpt-5.5)

*Codex reviewed via inline materials (it cannot read/write files in this sandbox). Transcribed verbatim by the Writer.*

## Summary
The brainstorm has the right governing principle: make the portfolio memorable by making the page behave like the story. The strongest ideas are small, semantic CSS moments, but the document still leans too heavily on atmosphere and motion while under-specifying reliability limits on phones.

## What's Good
- Per-beat animation flags are the best core direction: high memorability, low implementation risk, aligned with a copywriter's medium.
- The two "hero beats" are well chosen because they create structure without changing locked copy.
- The shortlist correctly defers pointer tracking and other fragile spectacle.
- Reduced-motion, invert mode, and sound gating are identified as real constraints instead of afterthoughts.

## Issues Found
1. **Per-line animation could become gimmicky fast.** Limit to 3-5 total signature beats, with one truly memorable peak. Too many and the reader watches effects instead of reading.
2. **Light/glow is under-risked.** Progress-driven atmosphere × invert × reduced-motion is a four-state design problem. Can become muddy on OLED phones or illegible in invert. Needs strict contrast testing / CSS variable caps.
3. **Sound is more fragile than stated.** Ambient audio in a single-file site risks file bloat, iOS quirks, and "portfolio with sound" gimmick perception. A tiny gesture-triggered WebAudio tick is safer than an ambient bed.
4. **Grain may hurt more than help on phones.** Can read as compression/noise or reduce text crispness. Optional and extremely subtle, not core.
5. **Micro-vibration is not universal.** Android-only haptics are fine as progressive enhancement, never a pillar. iPhone Safari users will not get it.
6. **Missing a structural wow.** Almost every idea is motion/sound/atmosphere. Needs one page-architecture move.
7. **External font conflicts with "zero-dependency."** Google Fonts is a reliability/constraint issue; decide whether Fraunces is embedded or replaced with a system serif fallback.

## Suggestions
- Structural idea: after the story completes, transform the progress bar into a "spine" / chapter map. Each segment is a story phase and can reopen the corresponding line, with the Hall of Fame attached as "proof" unlocked at the end. Keeps the locked copy intact while making the page feel like a narrative object, not a slideshow.

## Top 3 wow-to-risk
1. Per-beat meaning animations, capped at 3-5.
2. Two hero beats (identity reveal and "falling on purpose").
3. Hall of Fame drawer reveal, simple staggered CSS.

---

**Rating: NEEDS WORK**
Must address: cap signature beats; de-risk light/glow (or demote); swap ambient sound for a gesture-triggered WebAudio tick; make grain optional/subtle; frame haptics as enhancement only; add a structural move; resolve the font dependency.
