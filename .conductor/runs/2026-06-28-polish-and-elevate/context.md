# Context — Polish & Elevate (without losing the soul)

## Goal
Make a focused pass of improvements to the story-portfolio that genuinely elevate it, implementing strong ideas, WITHOUT losing its soul/essence/bigger picture/purpose. Every change is committed separately so any of it can be rolled back.

## THE SOUL (north star — reject anything that violates this)
- **Purpose:** a direct-response copywriter's portfolio that IS proof of the craft. It should make people who relate to Ali reach out, and make anyone think "I've never seen a portfolio like this."
- **Essence = CONGRUENCE.** The medium enacts the meaning; the form embodies the words. The wow comes from craft (writing + form), NEVER from gimmicks.
- **Emotional spine = FALLING.** The boy who cracked his head and got up fearless, then grew afraid of falling (being seen, judged, ignored), hid his work, learned to make OTHERS heard while staying invisible — and is now, on this page, "falling on purpose for the first time." It is about being SEEN and HEARD.
- **Structure mirrors meaning:** the childhood story is a paced, one-line-at-a-time reveal (you are being led, like a child read to); at "I'm the boy in the story" it becomes a self-directed, designed scroll (you grow up with him). The reveal is a standalone hinge between the two.
- **Aesthetic:** minimal, typographic, white-on-black (invert option), Fraunces, quiet, cinematic, words-first.
- **Reliability is sacred.** The old 3D versions died because they broke. Single self-contained file, zero external requests, no frameworks, no 3D, no scroll-physics, mobile-bulletproof.
- **Writing rules:** open hard, never define by negation, no hedging, no staccato, every line earns its keep, concrete/true.

## Reject filter
Any idea that does ANY of these is OUT: adds gimmick over craft · buries or competes with the words · risks breaking on mobile · dilutes the emotional arc · adds an external dependency · makes it feel like a "tech demo" instead of a piece of writing.

## Current state
Single `index.html`, ~104KB, embedded Fraunces, zero external requests. Three acts: (1) carousel story (one line at a time, tap/click/space/arrows, soft signature animations on 4 beats), (2) the "Hello. My name is Ali, and I'm the boy in the story" reveal as a standalone hinge, (3) a scrollable designed page (hero / method / proof with big numerals + italic "she cried" / Hall of Fame / close+CTA), gentle scroll-reveal. Controls: invert toggle, optional sound (off-by-default WebAudio tick), back control (carousel: step back; page: return to hinge). Reduced-motion + no-JS fallback. Verified working (note: the automation browser only composites when focused).

## Constraints
Single-file vanilla, zero deps, mobile-first, reliability sacred. Story COPY is locked (this is about experience/craft/polish, not rewriting lines). Deploy is the LAST step (later). The narrator character is a separate future phase.

## Success criteria
A vetted set of improvements that measurably elevate craft/feel/usability while passing the reject filter, each implemented and committed (rollback-able), verified working.
