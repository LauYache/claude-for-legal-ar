---
name: handbook-updates
description: >
  Diff a proposed handbook change against the current version, flag ripple
  effects and state supplement impacts. Use when user says "update the
  handbook", "add this to the handbook", "handbook change", or has a policy
  ready for insertion.
---

# Handbook Updates

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Handbook changes have ripple effects. Change the PTO policy and you've affected the final pay calculation, the leave policy cross-reference, and three state supplements. This skill finds the ripples before they become inconsistencies.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → handbook location, state supplements list, update cadence.

## Workflow

### Step 1: Get the change

- What section is changing?
- What's the new language?
- Why? (Legal requirement, policy decision, cleanup)

### Step 2: Diff against current

Read the current handbook section. Show the diff:

```diff
- [old language]
+ [new language]
```

### Step 3: Find cross-references

Search the handbook for references to the changed section:

- Other policies that cite this one ("see the PTO policy for accrual rates")
- Defined terms that this section uses or defines
- State supplements that modify this section

Each cross-reference: does it still make sense after the change? Flag any that break.

### Step 4: State supplement impact

For each state supplement in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`:

- Does this supplement modify the section being changed?
- Does the change make the supplement obsolete, wrong, or incomplete?
- Does the change create a need for a *new* supplement in a state that didn't need one before?

### Step 5: Promise check

Is the change reducing something the old version promised?

If yes: that's a risk. Some states treat handbook policies as contractual. Reducing a benefit may need more than just updating the document — advance notice, consideration, or in some cases it can't be done retroactively.

Flag this. Don't block it — but flag it.

## Output

```markdown
## Handbook Update: [Section name]

### Change

[diff]

### Cross-reference impact

| Section | References changed section | Still accurate? | Fix needed |
|---|---|---|---|
| [name] | [how] | ✅/⚠️ | [what] |

### State supplement impact

| State | Current supplement | After change | Action |
|---|---|---|---|
| [state] | [what it says] | [still valid / obsolete / needs update] | [none / update / new supplement needed] |

### Promise check

[If reducing a benefit: flag + jurisdictional risk note]

### Ready to publish

- [ ] Cross-references updated
- [ ] State supplements updated
- [ ] [If benefit reduction: notice/consideration addressed]
- [ ] Version number and date updated
- [ ] Acknowledgment process (if required)
```

## What this skill does not do

- Approve handbook changes. HR/legal leadership does.
- Communicate changes to employees.
- Track acknowledgments.

---

## Argentina — Actualizaciones obligatorias

When the handbook covers employees in Argentina, the following mandatory update categories apply. Argentine labor law requires certain policies to be in writing and communicated to employees, and failure to maintain an updated handbook can create liability.

### Teletrabajo (Ley 27.555)

If the company has remote workers in Argentina, the handbook **must** include a teletrabajo policy that addresses:
- **Derecho a la desconexión** (right to disconnect) — employees cannot be required to respond to communications outside working hours.
- **Equipment and expense reimbursement** — the employer must provide equipment and cover connectivity costs.
- **Working hours** — must be the same as on-site workers; overtime rules apply equally.
- **Reversibility** — the employee has the right to request a return to on-site work under certain conditions.
- **Privacy** — the employer's monitoring of remote work must respect the employee's privacy rights.

### Violencia laboral (Ley 26.485)

Ley 26.485 (Protección Integral para Prevenir, Sancionar y Erradicar la Violencia contra las Mujeres) applies to workplace violence and harassment. The handbook must include:
- A **protocolo de acoso laboral** (workplace harassment protocol) that establishes procedures for reporting, investigating, and resolving harassment complaints.
- Clear definitions of workplace violence (violencia laboral), including psychological harassment (mobbing), sexual harassment (acoso sexual), and discrimination-based harassment.
- Protection against retaliation for complainants.
- The protocol must be communicated to all employees and be accessible.

### Actos discriminatorios (Ley 23.592)

Ley 23.592 establishes criminal penalties for discriminatory acts. The handbook must include:
- A **non-discrimination policy** covering race, religion, nationality, ideology, sex, economic position, social condition, and other protected grounds.
- A procedure for reporting and investigating discriminatory conduct.
- Sanctions for employees who engage in discriminatory behavior.

### Additional Argentine mandatory policies

- **Código de conducta** — while not strictly mandatory, a code of conduct is expected and may be required by certain CCTs.
- **Política de drogas y alcohol** — required by many CCTs and by ART (workplace risk insurance) requirements.
- **Protocolo de actuación ante accidentes** — required by ART regulations.
- **Política de datos personales** — required under Ley 25.326 for employee data processing.

### Argentina handbook update checklist

When updating the handbook for Argentina, check:

| Policy | Required by | Update needed? |
|---|---|---|
| Teletrabajo / derecho a desconexión | Ley 27.555 | [ ] |
| Protocolo de acoso / violencia laboral | Ley 26.485 | [ ] |
| No discriminación | Ley 23.592 | [ ] |
| Datos personales del empleado | Ley 25.326 | [ ] |
| Drogas y alcohol | CCT / ART | [ ] |
| Vacaciones (Art. 156+ LCT) | LCT | [ ] |
| Licencias (maternidad, paternidad, enfermedad) | LCT Arts. 159, 177, 178, 208 | [ ] |
