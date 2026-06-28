#!/bin/bash
# Conductor: Invoke Codex as Reviewer
# Usage: ./invoke-codex.sh <run-folder> <action> [output-file]
#
# Actions:
#   review-research  - Review the latest research draft
#   review-plan      - Review the latest plan draft
#   ask-questions    - Add clarifying questions
#   review-code      - Review implementation

set -e

RUN_FOLDER="$1"
ACTION="$2"
OUTPUT_FILE="$3"
# Auto-detect project directory (parent of .conductor/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

if [ -z "$RUN_FOLDER" ] || [ -z "$ACTION" ]; then
    echo "Usage: ./invoke-codex.sh <run-folder> <action> [output-file]"
    exit 1
fi

RUN_PATH="$PROJECT_DIR/.conductor/runs/$RUN_FOLDER"

if [ ! -d "$RUN_PATH" ]; then
    echo "Error: Run folder not found: $RUN_PATH"
    exit 1
fi

case "$ACTION" in
    ask-questions)
        PROMPT="You are the REVIEWER in a Conductor session. Read .conductor/runs/$RUN_FOLDER/context.md and add up to 3 clarifying questions to .conductor/runs/$RUN_FOLDER/questions.md under 'Reviewer (Codex) Questions'. Focus on gaps, risks, and ambiguities. Update BOTH .conductor/state.json and .conductor/runs/$RUN_FOLDER/state.json."
        OUTPUT="${OUTPUT_FILE:-$RUN_PATH/questions.md}"
        ;;
    review-research)
        # Find latest research draft
        LATEST_FILE=$(ls -1 "$RUN_PATH"/research-v*.md 2>/dev/null | grep -v review | sort -V | tail -1)
        LATEST_NAME=$(basename "$LATEST_FILE")
        VERSION=$(echo "$LATEST_NAME" | sed 's/research-//' | sed 's/.md//')
        PROMPT="You are the REVIEWER. Read .conductor/runs/$RUN_FOLDER/$LATEST_NAME and write a review to .conductor/runs/$RUN_FOLDER/research-$VERSION-review.md. Use the rating format from PROTOCOL.md (APPROVED or NEEDS WORK). Update BOTH .conductor/state.json and .conductor/runs/$RUN_FOLDER/state.json."
        OUTPUT="${OUTPUT_FILE:-$RUN_PATH/research-$VERSION-review.md}"
        ;;
    review-plan)
        LATEST_FILE=$(ls -1 "$RUN_PATH"/plan-v*.md 2>/dev/null | grep -v review | grep -v final | sort -V | tail -1)
        LATEST_NAME=$(basename "$LATEST_FILE")
        VERSION=$(echo "$LATEST_NAME" | sed 's/plan-//' | sed 's/.md//')
        PROMPT="You are the REVIEWER. Read .conductor/runs/$RUN_FOLDER/$LATEST_NAME and write a review to .conductor/runs/$RUN_FOLDER/plan-$VERSION-review.md. Use the rating format from PROTOCOL.md (APPROVED or NEEDS WORK). Update BOTH .conductor/state.json and .conductor/runs/$RUN_FOLDER/state.json."
        OUTPUT="${OUTPUT_FILE:-$RUN_PATH/plan-$VERSION-review.md}"
        ;;
    review-code)
        PROMPT="You are the REVIEWER. Review the implementation against .conductor/runs/$RUN_FOLDER/plan-final.md. Write findings to .conductor/runs/$RUN_FOLDER/code-review.md. Update BOTH .conductor/state.json and .conductor/runs/$RUN_FOLDER/state.json."
        OUTPUT="${OUTPUT_FILE:-$RUN_PATH/code-review.md}"
        ;;
    *)
        echo "Unknown action: $ACTION"
        echo "Valid actions: ask-questions, review-research, review-plan, review-code"
        exit 1
        ;;
esac

echo "Invoking Codex..."
echo "Action: $ACTION"
echo "Run: $RUN_FOLDER"
echo "Model: gpt-5.2-codex (high reasoning)"
echo "Output: $OUTPUT"

codex exec "$PROMPT" \
    --model gpt-5.2-codex \
    -c model_reasoning_effort='"high"' \
    --sandbox workspace-write \
    -C "$PROJECT_DIR" \
    -o "$OUTPUT"

echo "Done. Output written to: $OUTPUT"
