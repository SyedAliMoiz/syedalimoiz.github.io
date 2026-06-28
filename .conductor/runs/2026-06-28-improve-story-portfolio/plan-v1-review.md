# Plan v1 Review (Codex, gpt-5.5)

*Reviewed via inline materials; transcribed by the Writer.*

## Summary
Directionally strong and respects reliability constraints, but needs tighter implementation rules. Biggest risks: animation state conflicts with the existing `.in` enter/exit model, and Chapter Spine taps interacting with the global document-click advance handler.

## Issues Found
1. **Animation variants may fight the `.in` enter/exit.** Variant keyframes animating opacity/transform on the same element can conflict or snap when the keyframe ends — risky for shrink/reveal/catch if their final transform differs from the normal `.in` transform.
2. **Exit not fully specified for variant beats.** "Exit untouched" is only safe if every animation ends at the exact state `.in` expects, OR the animation runs on an inner wrapper while the outer handles enter/exit.
3. **Spine taps can collide with global click advance.** Tappable chapter labels must stopPropagation, or a tap calls jumpTo AND bubbles into next() → off-by-one or race.
4. **jumpTo needs clear busy/index semantics.** Define behavior mid-transition (ignore if busy); update progress immediately; keep idx/displayed beat consistent.
5. **Spine visibility edge case.** Spine labels should show only when `idx === beats.length - 1`; after jumping back, return to story mode (faint ticks only), don't leave end-state labels on earlier beats.
6. **Font embedding underspecified.** Google Fonts CSS serves unicode-range shards; embedding wrong/too many bloats the file. Specify subset, exact weights, hard cutoff; prefer system-serif fallback over multiple large shards.
7. **No-JS coverage.** Confirm noscript stays readable after the font change, and that new interactive controls don't leave inert/confusing UI without JS.

## Suggestions (adopted)
- Stable outer `.beat` for opacity/exit; animate an inner `.beat-content` for signature effects.
- Variant animations end at `opacity:1; transform:none` unless exit explicitly handles the final state.
- `stopPropagation()` on Spine controls (and invert).
- `jumpTo()`: if busy return; set idx; render; update progress; hide end-state Spine unless at CTA.
- Prefer system-serif fallback over large base64 font shards if over target.

---

**Rating: NEEDS WORK** → all seven points incorporated into `plan-final.md`.
