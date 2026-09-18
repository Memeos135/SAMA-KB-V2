# Agent definitions

The three agents that actually answer a SAMA compliance question are **Claude Skills**,
not code in this repository. They live in Claude's own skills system and run against
`corpus/markdown/` and the three files under `graphify-out/` listed in the root
`README.md` — via Grep/Read only, no script, shell command or Python.

| Agent | Role | Snapshot in this folder |
|---|---|---|
| `sama-counsel` | Entry point. Routes facets, assigns diggers, writes the answer, fact-checks it, delivers it as a Claude Doc. | `sama-counsel.md` |
| `sama-digger` | Subagent. Pulls verbatim excerpts with exact page locators from one assigned corpus stem. Never invoked directly by a user. | `sama-digger.md` |
| `sama-auditor` | Subagent. Fact-checks counsel's answer against the corpus and the facet ledger. Never invoked directly by a user. | `sama-auditor.md` |

## These files are a snapshot, not the live source

Editing `sama-counsel.md` in this folder changes nothing about how a question actually
gets answered. The real, authoritative version of each skill lives in Claude's skills
system, outside this repository. If you change the live skill, re-paste its content
here so this folder doesn't go stale — the previous version of this folder described
the retired opencode `orchestrator → legal → mapper → extractor → reviewer →
formatter` design and the `sama.retrieve` / `sama.cite` scripts, and stayed on disk
for weeks describing a design that no longer ran anything. That drift is exactly what
this note exists to prevent.

Last synced from the live skills: 2026-09-18.
