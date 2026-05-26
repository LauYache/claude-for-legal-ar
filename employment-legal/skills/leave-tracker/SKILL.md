---
name: leave-tracker
description: >
  Check open leaves for deadline alerts and required decisions. Surfaces only
  the leaves that require an action and explains why — not a status board.
  Use weekly, or whenever the attorney needs to know which leaves have
  upcoming designation, certification, or exhaustion deadlines.
argument-hint: "[no arguments — works from HRIS or leave-register.yaml]"
---

# /leave-tracker

Checks all open leaves with hard legal deadlines and surfaces only the ones
requiring a decision or action. Not a status board — tells you what you need
to do and why.

## Instructions

1. Load the `leave-tracker` agent and run the full workflow.

2. If no HRIS is connected and no `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` exists, prompt
   the attorney to upload a leave spreadsheet or use
   `/employment-legal:log-leave` to add entries.

3. Alerts only for leaves requiring action. Clean leaves summarized one line each.

## Examples

```
/employment-legal:leave-tracker
```

Run this weekly — set a Monday-morning reminder to invoke
`/employment-legal:leave-tracker`. Automated scheduling requires a separate
integration (calendar reminder, cron job, etc.); Claude Code agents do not
self-schedule.

---

## Argentina — Licencias

When tracking leaves for employees in Argentina, the following leave entitlements apply under the LCT (Ley 20.744) and complementary legislation:

### Vacaciones (Arts. 156+ LCT)

Vacation entitlement depends on **seniority** (antigüedad):

| Antigüedad | Días de vacaciones |
|---|---|
| Hasta 5 años | 14 días |
| 5 a 10 años | 21 días |
| 10 a 20 años | 28 días |
| Más de 20 años | 35 días |

- Vacation period runs from October 1 to September 30 of the following year.
- The employer determines the vacation schedule, but must respect the employee's seniority-based entitlement.
- Vacation not taken by the end of the period must be paid at the daily rate calculated using the **divisor 25** (Art. 155 LCT): `Valor Día Vacación = Remuneración Mensual ÷ 25`.
- SAC (aguinaldo) must be added on vacation pay: `SAC s/ Vacaciones = Vacaciones no Gozadas ÷ 12`.

### Licencia por maternidad (Arts. 177/178 LCT)

- **Duration:** 90 days total (45 days before birth + 45 days after birth).
- The employee may choose to reduce the pre-birth period to 30 days, adding the remaining 15 days to the post-birth period (Art. 178 LCT).
- The employer must continue to pay salary during the leave (the employer is later reimbursed by ANSES — Administración Nacional de la Seguridad Social).
- The employee has job protection during pregnancy and the leave period.
- Nursing breaks: two 30-minute breaks per day during the first year after birth (Art. 179 LCT).

### Licencia por paternidad (Art. 159 LCT)

- **Duration:** **2 consecutive days** under Art. 159 LCT.
- Many **convenios colectivos de trabajo (CCT)** extend this period (commonly to 10-15 days). Always check the applicable CCT.
- The leave is paid and the employee has job protection.

### Enfermedad inculpable (Art. 208 LCT)

- Employees are entitled to paid leave for non-work-related illness or injury.
- **Duration:** depends on seniority and whether the employee has family dependents:
  - Without family: 3 months.
  - With family: 6 months.
  - For employees with more than 5 years of seniority: 6 months (without family) or 12 months (with family).
- During this period, the employer must pay the full salary. The employer may be reimbursed by the social security system after the initial period.
- The employer cannot terminate the employee during the protected period (Art. 211 LCT — termination during this period triggers aggravated indemnification).

### Other Argentine leaves

- **Licencia por matrimonio:** 10 days (Art. 180 LCT).
- **Licencia por fallecimiento de familiar:** 3 days for death of spouse, children, or parents; 1 day for other family members (Art. 181 LCT).
- **Licencia por examen:** days needed to take exams during the study period (Art. 182 LCT).
- **Licencia sindical:** for union representatives (Ley 23.551 — tutela sindical).
- **Teletrabajo — derecho a la desconexión (Ley 27.555):** remote workers cannot be required to work or respond to communications outside working hours.

### Argentina leave tracking

When logging an Argentine leave, track:

| Field | Value |
|---|---|
| Employee | [name/role] |
| Jurisdiction | Argentina [province] |
| Leave type | vacaciones / maternidad / paternidad / enfermedad inculpable / matrimonio / fallecimiento / examen / sindical |
| Start date | [date] |
| Expected return | [date] |
| CCT aplicable | [name/number — check for extended leave entitlements] |
| ART enrollment | [yes/no — required for work-related leaves] |
