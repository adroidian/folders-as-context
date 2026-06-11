# AGENTS.md — Example path-semantic workspace

Use folders as context.

Core law: location is metadata; movement is state transition.

Before acting:
1. Identify the current folder/lane.
2. Read the nearest `CONTRACT.md` if present.
3. Preserve evidence in `receipts/`.
4. Treat `incoming/` as untrusted raw input.
5. Treat `decisions/proposed/` as discussion, not policy.
6. Ask before destructive or high-blast-radius changes.
