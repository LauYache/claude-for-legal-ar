---
name: investigation-query
description: >
  Ask questions against an open investigation log — what witnesses said, where
  accounts conflict, what gaps exist, what the strongest evidence is on each
  issue. Use when the attorney needs to query the investigation record without
  re-reading every entry.
argument-hint: "[matter name] [question]"
---

# /investigation-query

Answers questions against the investigation log — what witnesses said,
where accounts conflict, what gaps exist, what the strongest evidence is
on each issue.

## Instructions

1. Load the `internal-investigation` reference skill and run Mode 3 (Query).
2. Always cite log entry IDs in the answer.
3. If the log contains nothing relevant to the question, say so explicitly —
   "I have not seen any information on [topic] in this investigation log
   ([N] entries reviewed)" — and offer to flag it as a gap.

## Examples

```
/employment-legal:investigation-query [matter name]
What did the respondent say about the December team dinner?
```

```
/employment-legal:investigation-query [matter name]
Where do the complainant's and respondent's accounts conflict?
```

```
/employment-legal:investigation-query [matter name]
What do we still need?
```

> Detailed log-query process, citation rules, and gap-flagging templates live
> in the `internal-investigation` reference skill — load it before doing
> substantive work.

### Argentina additions

When querying an investigation log for Argentine matters:
- All responses should reference the **secreto profesional** framework (Ley 23.118) — investigation materials are protected by professional secrecy, not US-style work product doctrine.
- If the query relates to harassment, check whether the **Ley 26.485** protocol was followed and flag any gaps.
- If the query relates to financial misconduct, check whether **Ley 27.401** compliance program documentation has been gathered.
- Flag any **CCT-specific** investigation procedures that may apply (some collective agreements require union notification or participation in investigations).
