---
name: dsar-response
description: >
  Walk through a Data Subject Access Request (or deletion, portability, correction
  request) and draft the response — verify identity, locate data system-by-system,
  assess exemptions, draft the acknowledgment and substantive response letters.
  Use when a DSAR comes in, the user pastes an access/deletion/portability/correction
  request, or says "DSAR came in", "access request", "right to be forgotten", or
  "someone wants their data".
argument-hint: "[paste the request, or describe it]"
---

# /dsar-response

1. Load `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → DSAR process (systems list, verification method, SLA).
2. Run the workflow below.
3. Classify request type. Check escalation triggers — if any fire, route before proceeding.
4. Walk through: verify identity → walk systems list → exemption analysis → draft.
5. Output response draft. Do NOT send — human reviews and sends.
6. Log the DSAR per house process.

**Before pasting the request:** the request will contain the data subject's PII. Confirm your session and output storage meet your data-handling requirements. Redact anything you don't need (ID attachments, unrelated email threads). Do not store the subject's name in filenames.

```
/privacy-legal:dsar-response
[paste the request email]
```

---

# DSAR Response Drafting

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A DSAR has a deadline (set by the applicable regime), a process (verify, locate, assess exemptions, respond), and a bunch of places it can go wrong. This skill walks through each step and drafts the response.

## Jurisdiction assumption

This analysis assumes the jurisdictional scope specified in your configuration. Privacy rules, response deadlines, and lawful bases vary materially by jurisdiction (GDPR vs. state consumer privacy laws vs. sectoral). If the data subject, processing activity, or controller is in a different jurisdiction than configured, this analysis may not apply as written.

## Load the process

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DSAR process`. That section has:
- The systems list (every place user data lives)
- Identity verification method
- Response SLA
- Who handles routine vs. who gets escalated

If the systems list is empty or stale, flag it — can't do a complete DSAR without knowing where to look.

## Workflow

### Step 1: Classify the request

Identify which right the data subject is invoking. Common categories:

- **Access** — copy of their data + information about processing
- **Deletion / erasure** — remove their data (subject to exemptions)
- **Portability** — their data in machine-readable format
- **Correction / rectification** — fix inaccurate data
- **Objection** — stop a particular processing (often marketing)
- **Restriction** — pause processing pending a dispute
- **Opt-out of sale/share / automated decision-making** — regime-specific rights

**Research the applicable rule before proceeding.** For each invoked right, identify the jurisdiction(s) whose law applies (GDPR, UK GDPR, CCPA/CPRA, other US state privacy laws, sectoral regimes, or Argentina's Ley N° 25.326). Cite the controlling statute or regulation with pinpoint references:
- **US / EU:** Standard CCPA/GDPR rules and response windows (typically 30 days for GDPR, 45 days for CCPA).
- **Argentina:** Under Ley N° 25.326 (Protección de Datos Personales), the deadlines are much stricter:
  - **Right of Access (*Derecho de Acceso*):** Response is due within **10 calendar days** (*días corridos*) of receipt (Art. 15).
  - **Right of Rectification, Update, or Deletion (*Derecho de Rectificación, Actualización o Supresión*):** Response is due within **5 business days** (*días hábiles*) of receipt (Art. 16).
Note effective dates; data subject rights are amended frequently. Flag uncertainty and escalate for attorney verification rather than stating a rule you haven't confirmed.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for the jurisdiction's rights, exemptions, or deadlines, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking.
>
> **Source attribution tiering.** Tag every citation with its source. For model-knowledge citations, use one of three tiers rather than a single blanket "verify" tag:
> - `[settled]` — stable, well-known statutory and regulatory references unlikely to have changed (e.g., GDPR Art. 33, CCPA § 1798.100, Ley 25.326 Art. 14/15/16).
> - `[verify]` — model-knowledge citations that are real but should be verified: specific implementing regulations, agency guidance, case holdings, thresholds, effective dates, post-2023 amendments.
> - `[verify-pinpoint]` — pinpoint citations (specific subsection letters, volume/page numbers, paragraph numbers, regulatory subpart references) carry the highest fabrication risk and should ALWAYS be verified against a primary source.
>
> Tool-retrieved citations keep their source tag (`[Westlaw]`, `[issuing authority site]`, or the MCP tool name); web-search citations remain `[web search — verify]`; user-supplied citations remain `[user provided]`. The tiering surfaces the real verification work. Never strip or collapse the tags.

Some requests are combinations — "delete my account and send me my data first" is deletion + portability. Handle as two linked requests.

### Step 2: Verify identity

Per the method in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. Common approaches:

- **Logged-in verification:** Request came from within an authenticated session → identity confirmed
- **Email match:** Request came from an email on file → usually sufficient for low-risk requests
- **Additional verification:** For high-value accounts or deletion requests → challenge question, phone verification, ID document

**Calibrate to risk.** Over-verifying turns the DSAR process into a barrier (bad look with regulators). Under-verifying risks handing someone else's data to a fraudster.

If identity can't be verified:

```markdown
We were unable to verify that this request came from the individual whose data
is at issue. To proceed, please [verification step]. We cannot provide personal
data in response to a request we cannot verify.
```

This pauses the clock (arguably) but don't sit on it — respond to say you need verification within a few days, not on day 29.

### Step 3: Locate the data

Walk the systems list from `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. For each system:

| System | Queried? | Data found? | What |
|---|---|---|---|
| Production database | | | |
| Analytics (e.g., Mixpanel, Amplitude) | | | |
| Support tickets (e.g., Zendesk) | | | |
| CRM (e.g., Salesforce, HubSpot) | | | |
| Email marketing (e.g., Marketo) | | | |
| Logs | | | |
| Backups | | | (note: usually exempt from deletion — see below) |
| Third-party processors | | | (they may need to be notified for deletion) |

For a B2B processor: the "data subject" is usually *your customer's* end user. Check whether this is actually your customer's DSAR to handle, not yours. Many processor DPAs say "forward DSARs to the controller."

### Step 4: Exemption analysis

Not everything gets produced or deleted. **Research the applicable rule before proceeding.** For each item, identify every exemption that plausibly applies under the regime in scope (e.g., third-party privacy, privilege, trade secret, security, legal obligation to retain, establishment/defense of legal claims, transactional necessity, backup rotation accommodations, freedom of expression). Cite the controlling statute, regulation, or case with a pinpoint cite. Exemption scope varies by jurisdiction and regime — verify currency and flag uncertainty.

**Don't narrow the list on a subjective call.** The skill proposes exemptions where a good-faith basis exists and flags the uncertain ones; the attorney narrows the list before the response goes out. Dropping an exemption that later turns out to apply is costly — once material is disclosed, the exemption is functionally gone. Over-asserting a plausible exemption is correctable by the attorney in review. Prefer the recoverable error.

Every proposed exemption carries an explicit note: **"proposed — requires attorney review before asserting. Regulators scrutinize blanket exemption claims, so the attorney narrows this list; the skill does not."**

Common recurring questions to work through:

- Does the record contain data about *other* people that needs to be redacted before production?
- Is there a specific legal retention obligation that blocks deletion? Cite it.
- Is there an active litigation hold covering this individual's data?
- Are there backup rotation or technical-feasibility accommodations that need to be documented (not used as a general excuse)?

**Document every exemption claimed.** If a regulator asks why you didn't delete something, "we had a legal obligation" needs a citation.

### Step 5: Draft the response — TWO LETTERS

> **Research-connector pre-flight.** Before emitting either letter or the internal exemption analysis, check whether a legal research connector is reachable for this session — Westlaw, an EUR-Lex / regulator-site connector, or any firm-configured research MCP. Collect this into the reviewer note per CLAUDE.md `## Outputs` — the reviewer note sits on the INTERNAL exemption-analysis and cover memo, NOT on the outward-facing DSAR letters to the data subject. If no connector returns results in Step 1 (right classification), Step 4 (exemption analysis), or the Deadline management research step (or none is configured at run time), record it in the **Sources:** line of the internal reviewer note — e.g., `not connected — cites from training knowledge; claimed exemptions, response deadlines, and extension mechanisms are especially fabrication-prone, verify before asserting any exemption to a data subject or regulator`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner above the output.

Most regimes expect (or require) a prompt acknowledgment separate from the substantive response. Produce both; do not collapse them into one letter that waits until the 45-day deadline to go out.

- **Step 5a — Acknowledgment letter.** Sent within days of receipt (target: same-day to 3–5 days, always well inside the regime's statutory window). Confirms receipt, states what the controller understands the request to be, states the response clock and the target date, asks for any identity-verification material still outstanding. Does NOT contain the substantive disclosure. A prompt acknowledgment is the first regulator-visible signal that the DSAR process is working; it also reduces the risk of a duplicate request or an early complaint.
- **Step 5b — Substantive response letter.** The actual disclosure, deletion confirmation, or portability export. Goes out by the statutory deadline (or the internal SLA if tighter). Only after identity verification is complete and the Step 3 / Step 4 data location + exemption analysis is done.

**Before proceeding to send either letter to the data subject:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. If the Role is Non-lawyer:

> Sending a DSAR response has legal consequences — the content, the exemptions claimed, and the omissions are all reviewable by a regulator, and misstatements become enforcement exposure. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: data subject, right invoked, applicable regime(s), what was located across the systems list, what is being withheld and under which exemption, identity verification posture, response deadline, and the three things to ask the attorney before the letter goes out.]
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

Do not proceed past this gate without an explicit yes.

> **Note:** Both DSAR letters are externally-facing deliverables sent to the data subject. Do **not** include the work-product header from `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` `## Outputs` on either letter. Internal notes, logs, and exemption analyses that accompany the letters are attorney work product — keep those separate and prepend the work-product header per `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` `## Outputs` (which differs by user role — see `## Who's using this`).

> **Before sending either letter:** This is a draft for attorney review, not a response to send. Sending commits the controller to a position, may waive exemptions, and may start a regulator's clock. A licensed attorney reviews, edits, and approves before either letter goes to the data subject. Do not send unreviewed.

#### Step 5a — Acknowledgment letter template

```markdown
Subject: We received your privacy request — [Company] — [date]

Dear [Name],

We received your [access / deletion / portability / correction] request on [date received].

**Your request, as we understand it:** [one-sentence restatement — e.g., "a copy of all personal data we hold associated with your account, along with the categories of third parties with whom we share it, and deletion of your account after we provide the copy."]

**What happens next:**
- Our target date for the substantive response is [date — no later than the regime's statutory deadline; use internal SLA if tighter]. [If identity verification is outstanding: "We need [specific verification step] before we can proceed — see below."]
- If we need more time because the request is complex or we receive other requests from you at the same time, we will tell you before the initial deadline and explain why. [If the regime allows an extension, cite the controlling provision.]
- No fee applies to this request. [Or: the fee applies only if the regime permits it and the request is manifestly unfounded or excessive — cite the provision.]

[If identity verification is outstanding:]
**To verify your identity,** please [specific verification step — e.g., reply to this email from the address on file with the last 4 digits of the payment method we have on file]. This does not pause our deadline; we continue to work in parallel.

If you have questions, contact [privacy contact].

[Sender]
```

**Clock-start rule.** The response clock starts on receipt of the request, not on completion of identity verification — unless the applicable regime says otherwise. Do not tacitly toll the clock on verification. If a regime has a different trigger, cite it; do not assume.

#### Step 5b — Substantive response letter templates

**Access request response:**

```markdown
Subject: Your Data Access Request — [Company] — [date]

We received your request on [date] for a copy of the personal data we hold about you.

**What we found:**

We hold the following categories of personal data associated with [identifier]:

| Category | Source | Purpose | Retained until |
|---|---|---|---|
| [Account info: name, email] | You, at signup | Account management | Account deletion |
| [Usage data] | Our service | Analytics, product improvement | [period] |
| [Support correspondence] | You | Customer support | [period] |

**Your data is attached** in [format]. [Secure delivery note — password-protected
archive, secure link with expiry, etc.]

**Third parties:** We share data with the following processors: [list or link to
subprocessor page].

**Your other rights:** You may also request [deletion / correction / portability].
To do so, [method].

**Data we did not include:**
- [Category] — [exemption and reason, e.g., "internal security logs — disclosure
  would compromise security measures"]
- [Data about other individuals has been redacted from support correspondence]

If you have questions about this response, contact [privacy contact].
```

**Deletion request response:**

```markdown
Subject: Your Deletion Request — [Company] — [date]

We received your request on [date] to delete the personal data we hold about you.

**What we deleted:**

| Category | System | Deleted on |
|---|---|---|
| [Account and profile] | Production | [date] |
| [Analytics events] | [Amplitude/etc.] | [date] |
| [etc.] | | |

**What we retained and why:**

| Category | Reason | Retained until |
|---|---|---|
| [Transaction records] | Legal obligation (tax record retention, [cite law]) | [date] |
| [Backup snapshots] | Will be deleted on next rotation | [date] |

**Third-party processors:** We have instructed [list] to delete your data from
their systems.

Your account is now closed. If you have questions, contact [privacy contact].
```

### Argentina — DSAR

Under **Ley 25.326** (Ley de Protección de Datos Personales), DSAR deadlines are significantly shorter than under GDPR or CCPA:

- **Right of Access (*Derecho de Acceso*):** Response is due within **10 calendar days** (*días corridos*) of receipt (**Art. 14/15**). The AAIP must be notified of the request, and the response must be provided within this statutory window.
- **Right of Rectification, Update, or Deletion (*Derecho de Rectificación, Actualización o Supresión*):** Response is due within **5 business days** (*días hábiles*) of receipt (**Art. 16**).
- **Right of Suppression (*Derecho de Supresión*):** Governed by **Art. 17** — data subjects may request deletion of their data when it is incomplete, inaccurate, or no longer necessary for the purpose for which it was collected.
- **No statutory extension mechanisms.** Unlike GDPR (which permits a 2-month extension for complex requests) or CCPA (which permits a 45-day extension), **Ley 25.326 provides NO statutory extension mechanisms**. The 10-day and 5-day deadlines are absolute.
- **Habeas data.** Under **Art. 43 of the Constitución Nacional**, data subjects may file a *habeas data* action in federal court to enforce their rights of access, rectification, and suppression. This is the judicial enforcement mechanism when the data controller fails to respond within the statutory deadlines.
- **AAIP complaints.** Data subjects may file complaints directly with the **AAIP** (Agencia de Acceso a la Información Pública), which has authority to investigate and impose sanctions.
- **Identity verification.** Use **DNI** (Documento Nacional de Identidad) for identity verification of Argentine data subjects.

If a DSAR involves Argentine data subjects, apply these deadlines regardless of any internal SLA that may be longer. The Ley 25.326 deadlines are the legal backstop.

### Step 6: Log it

DSARs get audited. Record:
- Date received
- Date identity verified
- Date responded
- What was produced/deleted
- Exemptions claimed and basis
- Who handled it

If your team uses a DSAR tracking tool, create the record there. If not, a log file works.

## Escalation triggers

Per `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → Escalation table, escalate when:

- Requester is (or might be) a plaintiff, opposing counsel, or journalist
- Request scope is unusual ("all data including internal communications about me")
- There's a litigation hold on this individual's data (deletion request + lit hold = conflict, lawyer decides)
- Requester is disputing a previous DSAR response
- Any regulator is cc'd or mentioned

## Deadline management

**Two-letter rule.** Every DSAR produces an acknowledgment letter (prompt — target same-day to 3–5 days after receipt) AND a substantive response letter (by the statutory deadline). 

**Research the currently operative response deadline for the specific right invoked and the applicable jurisdictions.** Cite the controlling statute or regulation with pinpoint references:
- **US / EU:** Standard extension rules apply (e.g., 30 extra days for GDPR if complex, 45 extra days for CCPA). Notice must be sent before the initial deadline.
- **Argentina:** There are **NO statutory extension mechanisms** for Ley N° 25.326 deadlines. 
  - **Access right:** Must be fully answered within **10 calendar days** (*días corridos*) of receipt.
  - **Rectification/Deletion right:** Must be fully answered within **5 business days** (*días hábiles*) of receipt.
  - The clock starts on receipt. If identity verification is required, it must be requested immediately to avoid late response penalties and potential AAIP complaints or Habeas Data legal actions.

If `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DSAR process` records an internal SLA that is tighter than the legal deadline, use the internal SLA and note the legal backstop.

If you're going to need an extension (in jurisdictions where permitted), send the "we need more time" notice well before the first deadline. Day-of extensions look bad.

## What this skill does not do

- It doesn't query systems directly. It walks you through the checklist; a human (or a connected tool) does the actual queries.
- It doesn't make exemption calls on close cases. It flags them for a lawyer.
- It doesn't send the response. Draft, review, human sends.
