---
name: investigation-open
description: >
  Open a new internal investigation matter — runs intake, generates the sources
  checklist, and creates the persistent investigation log. Use when a complaint
  or allegation comes in and the attorney needs to stand up a privileged
  investigation workspace.
argument-hint: "[brief description of the allegation]"
---

# /investigation-open

Opens a new investigation matter — runs intake, generates the sources
checklist, and creates the persistent investigation log.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`.
2. Load the `internal-investigation` reference skill and run Mode 1 (Open).
3. If a matter with the same slug already exists, warn before overwriting.

## Examples

```
/employment-legal:investigation-open
Harassment complaint filed against a manager in the Austin office.
```

```
/employment-legal:investigation-open
Acoso laboral denunciado contra un gerente en la oficina de CABA.
```

```
/employment-legal:investigation-open
(skill will ask for details)
```

> Detailed intake, privilege-formation requirements, sources checklist, and log
> templates live in the `internal-investigation` reference skill — load it
> before doing substantive work.

### Argentina additions

When opening an investigation in Argentina:
- Mark investigation files as **"Confidencial — Secreto Profesional"** (professional secrecy under Ley 23.118 and Colegio de Abogados ethics codes).
- Add **Ley 26.485** (violencia laboral) protocol compliance to the sources checklist if the allegation involves harassment.
- Add **Ley 27.401** (responsabilidad penal corporativa) compliance program documentation if the allegation involves financial misconduct or corruption.
- Ensure the intake captures the applicable **CCT** (convenio colectivo de trabajo) — it may impose additional investigation or disciplinary procedures.
- Flag whether the respondent or complainant is a **union representative** (tutela sindical, Ley 23.551) — this triggers additional procedural protections.
