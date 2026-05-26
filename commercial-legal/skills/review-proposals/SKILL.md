---
name: review-proposals
description: >
  Review and approve (or reject) pending playbook update proposals from the
  playbook-monitor agent and apply approved changes to the practice profile. Use
  when the playbook-monitor agent has surfaced proposals, when the user says
  "review playbook proposals", "what playbook updates are pending", or wants to
  step through deviation-driven playbook changes.
argument-hint: "[no arguments needed — works from the pending proposals file]"
---

# /review-proposals

Steps through pending playbook update proposals from the monitor agent and applies approved changes to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.

## Instructions

1. **Load the playbook-monitor agent** and run Step 5 (review and approval flow).

2. **If no proposals file exists** or it is empty: respond *"No pending proposals. Playbook is up to date."* Do not proceed further.

3. **Present proposals one at a time.** For each, show the full proposal block and offer four options: Accept, Reject, Edit, Defer.

4. **For Accept or Edit:** show the exact diff to `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` before writing. Only apply after the attorney explicitly confirms.

5. **For Reject or Defer:** log the decision. Do not modify `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`.

6. **After all proposals are resolved:** show a summary of what changed, then archive the proposals file.

## Argentina — proposal review overlay

When reviewing playbook proposals that involve Argentine-governed contracts or Argentine parties, consider these CCyCN-based grounds for playbook updates:

- **CCyCN Art. 962 (buena fe):** If deviations show a pattern of accepting clauses that violate good faith principles (asymmetrical obligations, hidden penalties, lack of transparency), propose updating the playbook to flag these as YELLOW or RED.
- **CCyCN Art. 966 (lesión):** If signed agreements show a pattern of accepting contractually imbalanced terms that could trigger lesión claims, propose adding lesión as a review criterion.
- **Ley 24.240 (consumidor):** If the company regularly enters contratos de adhesión with consumers, propose adding consumer protection checks to the playbook — abusive clauses, contra proferentem interpretation, mandatory local jurisdiction.
- **CCyCN Art. 765/766 (pesificación):** If foreign currency contracts are being signed without pesificación risk analysis, propose adding a currency clause review step.
- **CCyCN Art. 2605 (jurisdicción):** If foreign jurisdiction clauses are being accepted in domestic contracts, propose adding a jurisdiction validity check.

Apply these as additional lenses when evaluating whether a deviation pattern warrants a playbook update.

## Examples

```
/commercial-legal:review-proposals
```

```
/commercial-legal:review-proposals
(runs automatically after playbook-monitor notifies you)
```
