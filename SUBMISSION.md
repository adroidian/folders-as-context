# Submission Notes

## Hermes

Candidate location in the Hermes Agent repository:

```text
skills/software-development/folders-as-context/SKILL.md
```

Include `templates/workspace/` as supporting material if the skill registry supports linked files. Otherwise, keep templates in a separate public repo and link from the skill body.

## OpenClaw / other agent runtimes

This is runtime-portable. For systems without a formal skill loader, install the same behavior by:

1. adding the lane skeleton,
2. adding `CONTRACT.md` files,
3. patching the agent boot prompt/context with the core law and hard stops,
4. smoke-testing one harmless task.

## Public safety checklist

- No private user names, paths, hostnames, or secrets.
- No raw transcripts.
- No environment-specific runbooks.
- MIT license included.
- Skill frontmatter validates.
