# Context

## Goal
Brainstorm, then implement, improvements to the single-file story-reveal portfolio (`index.html`) that push the "I've never seen a portfolio like this" reaction — even on a phone — without sacrificing reliability.

## Why
This is a direct-response copywriter's portfolio, so the site itself is proof of the craft. Ali's earlier 3D "museum" versions were unique but broke on real devices (functionality was effectively zero), and that killed them. The new text-reveal build is bulletproof, but Ali's honest worry is that a plain text reveal, on its own, may not be novel enough to earn the genuine "wow, I've never seen a portfolio like this" reaction he is chasing. We want to elevate the EXPERIENCE (words + world + small interactions + a planned narrator character) while keeping it unbreakable.

## Current State
Single self-contained `index.html`, zero dependencies, zero build step. Features:
- Snippet-by-snippet story: one line per screen, each fades up and holds alone on a black screen.
- Advance by tap / click / spacebar / arrow keys; arrow-left/up goes back.
- Thin progress bar at the bottom; a "tap to continue" hint that disappears after the first tap.
- White-on-black default with a persistent invert toggle (localStorage), animated color cross-fade.
- A "Hall of Fame" wall screen: big numbers (9M+, 40%, $215k+, 1,750%) plus a credentials block, framed as "Here's everything else that was in the drawer."
- CTA screen: "Let's get to work." + "Say 'hi' here:" with Email and LinkedIn pill links.
- Fraunces serif via Google Fonts (system serif fallback).
- Responsive by construction: fluid `clamp()` type, `min(92vw, 40rem)` column, `flex-wrap` stats, `dvh` height, safe-area insets.
- `prefers-reduced-motion` support; a `<noscript>` fallback that renders the full story as plain text.
Verified working on desktop in both themes. Real-phone tap-through still pending (Ali's to do).

## Desired State
A version that feels singular and memorable enough to earn "I've never seen a portfolio like this," even on a phone, while staying rock-solid: no 3D, no heavy frameworks, nothing fragile. The little "writer" narrator character is planned as a deliberate phase 2.

## Constraints
- **Reliability is non-negotiable.** Must work flawlessly on mobile and desktop. No 3D, no heavy frameworks, nothing that can break the way the old versions did. Prefer staying (near) single-file and dependency-light.
- **Story content is LOCKED** (final V3). This brainstorm is about EXPERIENCE and craft, not rewriting the story copy.
- **Writing rules** (for any micro-copy/UI text we add): open hard, never define by negation, no hedging, no staccato, every line earns its keep, concrete and true over embellished.
- **CTA stays:** "Let's get to work." + Say hi (Email + LinkedIn).
- **Text-first.** The narrator character is phase 2; it may be discussed but the core must shine without it.
- **Audience:** broad. Win condition = "wow, I've never seen a portfolio like this," even on a phone, plus people who like/trust/relate to Ali reaching out.

## Success Criteria
A prioritized set of improvement ideas, each weighed for impact on the "wow" reaction against risk to reliability; consensus with Codex on which to implement; then a clean implementation that keeps the single-file, unbreakable property.

## Assumptions
- Single-file vanilla (HTML/CSS/JS) approach stays. No framework or build step is introduced.
- The narrator character is deferred (phase 2) but ideas that anticipate it are welcome.
- Deployment happens later; this run is about the experience itself.

## Decisions Log
- (populated during research/planning)

## Open Questions (Locked)
- (populated if needed)
