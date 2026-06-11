# Folders as Context

A portable agent skill for treating folder structure as operational context.

Core idea:

> Location is metadata. Movement is state transition.

Folders are not just storage. In an agent-readable workspace, paths help agents decide what to read, trust, edit, preserve, archive, or escalate. This skill defines a small workspace grammar using lane directories such as `incoming/`, `receipts/`, `decisions/proposed/`, and `data/wiki/`, plus local `CONTRACT.md` files that describe behavior and authority for each lane.

## What this is

- A Hermes-compatible `SKILL.md`.
- A portable method that can be adapted to other agent runtimes.
- A lightweight folder contract pattern for restart recovery, evidence preservation, and safer agent operations.

## What this is not

- Not a permission slip for agents to bulk move or delete user data.
- Not a replacement for explicit user instructions.
- Not a secrets store.
- Not a giant prompt disguised as a file tree.

## Install in Hermes

Copy the skill folder into a Hermes profile skill directory:

```bash
mkdir -p ~/.hermes/skills/software-development
cp -R skills/software-development/folders-as-context ~/.hermes/skills/software-development/
```

Or for a named profile:

```bash
mkdir -p ~/.hermes/profiles/<profile>/skills/software-development
cp -R skills/software-development/folders-as-context ~/.hermes/profiles/<profile>/skills/software-development/
```

Then start a fresh Hermes session and load it by name. Depending on the skill resolver, category-qualified loading may be needed:

```bash
hermes -s software-development/folders-as-context
```

## Quick workspace skeleton

```text
workspace/
  AGENTS.md
  incoming/CONTRACT.md
  watchboard/CONTRACT.md
  briefs/CONTRACT.md
  decisions/proposed/CONTRACT.md
  decisions/accepted/CONTRACT.md
  decisions/superseded/CONTRACT.md
  receipts/CONTRACT.md
  handoffs/CONTRACT.md
  data/wiki/CONTRACT.md
  archive/CONTRACT.md
```

See `templates/workspace/` for starter contracts.

## License

MIT.
