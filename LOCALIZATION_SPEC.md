# Spec: Localización Argentina — claude-for-legal-ar

## Contexto

El repositorio `claude-for-legal-ar` es una adaptación del plugin marketplace `claude-for-legal` de Anthropic (12 plugins, ~140 skills) para derecho argentino. La localización actual es **parcial y superficial**:

- Los **CLAUDE.md templates** (comportamiento base de cada plugin) son ~100% US
- Los **SKILL.md** tienen referencias argentinas como parches sobre frameworks US, no como reemplazo
- El contenido argentino real vive separado en `agnostic-legal-ar/prompts/` (5 archivos bien localizados)
- Los plugins `ip-legal`, `litigation-legal`, `product-legal`, `ai-governance-legal` no tienen NINGUNA referencia argentina integrada

**Objetivo:** Integrar la localización argentina directamente en los CLAUDE.md y SKILL.md de cada plugin, haciendo que el comportamiento default sea Argentina-first en lugar de US-first con add-ons condicionales.

---

## Principios de localización

1. **Argentina-first, no Argentina-only**: El plugin debe funcionar para cualquier jurisdicción, pero Argentina debe ser la jurisdicción primaria con ejemplos concretos, no un add-on condicional
2. **No borrar US, agregar AR**: Los templates US se mantienen como alternativas. Se agregan secciones argentinas paralelas con la misma profundidad
3. **Citas reales, no placeholders**: Donde el template US cita artículos específicos (FLSA §207, DGCL §141), el template AR debe citar artículos específicos argentinos (Art. 245 LCT, Art. 158 CCyCN)
4. **Integrar agnostic-legal-ar**: Los 5 prompts agnósticos son el mejor contenido argentino del repo. Se migran dentro de los plugins como secciones de referencia
5. **Consistencia de formato**: Todas las referencias legales argentinas usan el formato `[CITE: Ley XXXX / Art. YY]` con tag `[model knowledge — verify]`

---

## Fase 1: CLAUDE.md templates (9 plugins)

**Alcance:** 9 archivos CLAUDE.md
**Complejidad:** Media (estructura conocida, cambios predecibles)
**Criterio de éxito:** Cada CLAUDE.md tiene secciones argentinas equivalentes en profundidad a las secciones US

### 1.1 Cambios comunes a TODOS los CLAUDE.md

#### A. Sección "Attorney work product" (~línea 75-80)

**Agregar después del bloque US/EU/UK:**

```markdown
**Argentina:** No existe una doctrina equivalente a "attorney work product." La confidencialidad se rige por:
- Secreto profesional del abogado (Ley 23.118, Código Procesal Civil y Comercial de la Nación, Art. 380+)
- Códigos de ética de cada Colegio de Abogados (CPACF, etc.)
- Secreto de las comunicaciones entre abogado y cliente es absoluto en derecho argentino
- No equivalente a FRCP 26(b)(3) discovery protection
```

#### B. Sección "Outputs" — jurisdiction warning

**Agregar Argentina al breakdown existente:**

```markdown
**Argentina:** Work product is not a recognized doctrine. Confidentiality derives from professional secrecy obligations under local procedural codes and bar association ethics rules. Mark as "Confidencial — Secreto Profesional" for Argentine matters.
```

#### C. Sección "Escalation"

**Agregar canales argentinos a cada tabla de escalación:**

| Jurisdicción | Trigger | Acción |
|---|---|---|
| Argentina | Denuncia regulatoria (AAIP, CNV, BCRA, Ministerio de Trabajo) | Escalar inmediatamente a socio responsable |
| Argentina | Tutela sindical / Art. 182 LCT (indemnización agravada) | Escalar antes de cualquier acción |
| Argentina | PPC (Procedimiento Preventivo de Crisis, Ley 24.013) | Escalar + notificar Ministerio de Trabajo |

#### D. Placeholders US-centric

Reemplazar o agregar ejemplos argentinos en:

- `[PLACEHOLDER — e.g., "Delaware, our home jurisdiction"]` → `[PLACEHOLDER — e.g., "Tribunales Comerciales de CABA" / "Delaware, our home jurisdiction"]`
- `[PLACEHOLDER — NYSE / Nasdaq / other]` → `[PLACEHOLDER — BYMA / ROFEX / NYSE / Nasdaq / other]`
- `[PLACEHOLDER — EEOC, DOL, state AGs]` → `[PLACEHOLDER — Ministerio de Trabajo, SECLO, AAIP, CNV / EEOC, DOL]`
- `[PLACEHOLDER — CT Corp / National Registered Agents]` → `[PLACEHOLDER — domicilio social / CT Corp / registered agent]`

### 1.2 Cambios específicos por plugin

#### employment-legal/CLAUDE.md (399 líneas)

| Sección | Cambio |
|---------|--------|
| **Jurisdictional footprint** | Agregar `**Provincias argentinas con empleados:** [PLACEHOLDER]` debajo de "US states with employees" |
| **High-risk termination flags** | Agregar: `maternidad (Art. 177/178 LCT), matrimonio (Art. 180/181 LCT), enfermedad inculpable (Art. 208 LCT), tutela sindical (Ley 23.551), PPC (Ley 24.013)` |
| **Jurisdiction-specific escalation rules** | Agregar fila Argentina con: Tutela sindical, Art. 182 indemnización agravada, PPC Ley 24.013, Art. 80 certificados |
| **Cal-WARN example** (línea 89) | Agregar ejemplo paralelo: `"Flag: potential PPC issue (Ley 24.013) — Argentina requires Procedimiento Preventivo de Crisis before collective dismissals."` |
| **FLSA example** (línea 182) | Agregar ejemplo paralelo: `"Mencionaste un plazo de prescripción de 2 años para reclamos laborales — mi entendimiento es que la LCT establece plazos según el tipo de acción (Art. 254 LCT: 2 años para indemnización, 5 años para diferencias salariales)."` |
| **Escalation table** (líneas 379-385) | Agregar: `Denuncia ante Ministerio de Trabajo / SECLO | — | [GC inmediatamente] | Always` |
| **Integrations table** | Agregar: `Sistema de RRHH local | [PLACEHOLDER]` |

#### privacy-legal/CLAUDE.md (405 líneas)

| Sección | Cambio |
|---------|--------|
| **Regulatory footprint** (línea 35) | Cambiar placeholder a: `[PLACEHOLDER — Ley 25.326 (Argentina) / GDPR / CCPA / HIPAA / etc.]` |
| **Sectoral notices** (línea 154) | Agregar: `Ley 26.529 (derechos del paciente) / Ley 25.326 sectoral rules / GLBA / HIPAA NPP / FERPA / COPPA` |
| **DSAR process** | Agregar sección con deadlines Ley 25.326: Acceso = 10 días corridos (Art. 14/15), Rectificación = 5 días hábiles (Art. 16), Sin prórrogas estatutarias |
| **DPA playbook** | Agregar: Argentina no tiene cláusulas estándar publicadas por AAIP; usar modelo tipo OEA o contractual |

#### commercial-legal/CLAUDE.md (509 líneas)

| Sección | Cambio |
|---------|--------|
| **Governing law — sales-side** (línea 130) | Agregar: `Tribunales Comerciales de CABA / fuero correspondiente / Delaware` |
| **Governing law — purchasing-side** (línea 197) | Agregar equivalente argentino |
| **Contract law context** | Agregar después de sales/purchasing description: `Under CCyCN Art. 957+, freedom of contract applies but consumer protection (Ley 24.240) overrides adhesion contracts. Art. 765/766 CCyCN: pesification risk for foreign currency obligations.` |
| **SOC 2** (línea 180) | Agregar: `ISO 27001 / SOC 2 Type II for any vendor touching customer data` |
| **Signature law** | Agregar referencia: `Ley 25.506 (firma digital vs electrónica) — firma digital tiene presunción de autoría; firma electrónica (DocuSign, etc.) no` |

#### corporate-legal/CLAUDE.md (478 líneas)

| Sección | Cambio |
|---------|--------|
| **Entity format** (línea 32) | Agregar: `"Acme S.A., sociedad anónima constituida bajo las leyes de la República Argentina, CUIT [PLACEHOLDER]"` |
| **Regulators** (línea 35) | Agregar: `CNV (Comisión Nacional de Valores), BCRA, AAIP, IGJ/DPPJ` |
| **Resolutions format** (línea 398) | Agregar: `"SE RESUELVE:" / "POR MAYORÍA/UNANIMIDAD SE APRUEBA:" format for Argentine entities` |
| **M&A side** (línea 320) | Agregar: `Compraventa de acciones (LGS) / assets (CCyCN), due diligence under Argentine practice` |
| **Exchange** (línea 421) | Agregar: `BYMA (Bolsa y Mercados Argentinos) / ROFEX / NYSE / Nasdaq` |
| **§16 reporting** (líneas 431-438) | Agregar: `CNV reporting obligations (Comunicaciones A-series), insider trading under Ley 26.831 (Mercado de Capitales)` |
| **Registered agent** (línea 452) | Agregar: `Domicilio social (Argentina — no registered agent concept) / CT Corp / registered agent` |
| **Cap table tool** (línea 455) | Agregar: `Libro de Acciones (physical/digital) / Carta / Shareworks` |
| **Board minutes** | Agregar: `Libro de Actas de Directorio (Art. 73 LGS), Art. 158 CCyCN (resoluciones por escrito unánimes), Art. 272 LGS (conflictos de interés)` |

#### ip-legal/CLAUDE.md (395 líneas)

| Sección | Cambio |
|---------|--------|
| **Registered in** (línea 225) | Agregar: `INPI (Argentina)` como jurisdicción primaria |
| **Watch jurisdictions** (líneas 262-265) | Agregar: `Boletín de Marcas (INPI Argentina)` |
| **Approval matrix** (líneas 286-291) | Agregar: `INPI opposition procedure (30 days from Boletín publication) / DMCA takedown` |
| **Patent agent privilege** (línea 90) | Agregar: `Agentes de la Propiedad Industrial registered with INPI, governed by INPI regulations` |
| **Enforcement posture** | Agregar sección: `Argentina enforcement: Ley 22.362 (marcas), Ley 11.723 (derechos de autor), Ley 24.481 (patentes). No statutory damages — actual damages must be proven. Criminal penalties under Art. 31 Ley 22.362, Art. 72 Ley 11.723.` |

#### litigation-legal/CLAUDE.md (558+ líneas)

| Sección | Cambio |
|---------|--------|
| **Entity format** (línea 32) | Agregar formato argentino: `"Acme S.A., sociedad anónima, CUIT [PLACEHOLDER], domicilio legal en [PLACEHOLDER]"` |
| **Regulators** (línea 35) | Agregar: `CNV, BCRA, AAIP, ANMAT, ENACOM` |
| **Financial reporting** (líneas 406-409) | Agregar: `RT 17 FACPCE (reserves), CNV reporting requirements (Comunicaciones A-series), IGJ reporting` |
| **Frequent fora** (línea 470) | Agregar: `Tribunales Ordinarios (Comerciales/Civiles) de CABA, arbitraje CEMA, arbitraje ICC, mediación prejudicial obligatoria` |
| **Legal hold** | Agregar: `No discovery in Argentine civil procedure. Evidence production via medidas para mejor proveer, oficios judiciales, peritajes.` |
| **Privilege conventions** | Agregar: `Secreto profesional (Art. 380+ CPCCN, Ley 23.118). No attorney-client privilege doctrine. Communications protected by professional secrecy.` |

#### product-legal/CLAUDE.md (397 líneas)

| Sección | Cambio |
|---------|--------|
| **Platform policy** (línea 182) | Agregar: `ENACOM (telecomunicaciones), Defensoría del Público, Ley 26.904 (grooming), Ley 25.326 (datos personales), Ley 24.240 (defensa del consumidor)` |
| **Marketing claims** | Agregar: `Ley 24.240 (publicidad engañosa), Código de Ética de CONAR Argentina, Ley 22.802 (Lealtad Comercial)` |

#### ai-governance-legal/CLAUDE.md (479 líneas)

| Sección | Cambio |
|---------|--------|
| **Regulatory framework** (línea 44) | Agregar: `No specific AI law in Argentina yet. Apply Ley 25.326 (data protection), consumer protection (Ley 24.240), sectoral rules (BCRA for fintech, CNV for capital markets), and emerging guidelines from AAIP.` |
| **Source feeds** (línea 436) | Agregar: `InfoLEG (sistemas.infoleg.gob.ar), Boletín Oficial, AAIP, CNV, BCRA, ENACOM, ANMAT` |
| **AI system inventory** | Agregar: `No mandatory AI registry in Argentina. Voluntary compliance with AAIP guidelines on automated decision-making under Ley 25.326 Art. 11 (automated decisions affecting rights).` |

#### regulatory-legal/CLAUDE.md (355 líneas)

| Sección | Cambio |
|---------|--------|
| **Regulators we watch** | Agregar: `AAIP, CNV, BCRA, ENACOM, ANMAT, IGJ, AFIP, Ministerio de Trabajo` |
| **Source hierarchy** (línea 306) | Agregar: `InfoLEG (primary for national norms), Boletín Oficial (primary for regulations), AAIP resolutions, CNV communications, BCRA communications` |
| **Feed configuration** (línea 52) | Agregar: `Boletín Oficial RSS/API, InfoLEG updates, AAIP news feed` |

---

## Fase 2: Skills de ip-legal (12 skills)

**Alcance:** 12 SKILL.md en `ip-legal/skills/`
**Complejidad:** Alta (cero contenido argentino integrado actualmente)
**Criterio de éxito:** Cada skill tiene framework argentino como opción primaria junto al US

### 2.1 cease-desist/SKILL.md

| Línea/Sección | US actual | Agregar AR |
|---|---|---|
| Legal basis (línea 201) | `Lanham Act §32 / §43(a) / 17 U.S.C. §501` | `Ley 22.362 (marcas) / Ley 11.723 (derechos de autor) / Ley 24.481 (patentes) / CCyCN` |
| Remedies (líneas 214-215) | `15 U.S.C. §1117 / 17 U.S.C. §504`, `Anti-Cybersquatting (15 U.S.C. §1125(d))` | `Ley 22.362 Art. 31 (penales civiles/criminales), Ley 11.723 Art. 72 (penales). No statutory damages in Argentina — actual damages must be proven.` |
| Additional claims (línea 237) | `§43(a)(1)(B), Rule 11, Lanham Act / Copyright Act attorneys' fees` | `Acciones civiles y penales bajo Ley 22.362 / Ley 11.723, costas procesales, medidas cautelares (Art. 192+ CPCCN)` |
| Likelihood of confusion (línea 316) | `Polaroid / AMF / Sleekcraft factors` | `Criterios de confusión del INPI: semejanza gráfica, fonética, ideológica; naturaleza del producto, canales de comercialización` |
| Copyright registration | `US suits require registration for filed claims` | `In Argentina, copyright registration at DNDA is declarative, not constitutive, but strongly recommended for evidence purposes.` |
| New section | — | **Procedimiento INPI**: Oposición dentro de 30 días de publicación en Boletín de Marcas. Requisitos: formulario, tasa, fundamentos. Contestación: 6 días hábiles. Resolución: 40 días hábiles. |

### 2.2 clearance/SKILL.md

| Sección | Agregar AR |
|---------|-----------|
| Trademark search | `INPI database (tramitesenlinea.inpi.gob.ar), Boletín de Marcas, Clasificación de Niza. Search for identical and confusingly similar marks in same class.` |
| Patent search | `INPI patent database, Ley 24.481 novelty requirements, prior art search in Argentine and international databases.` |
| Copyright clearance | `DNDA registry (trámitesenlinea.inpi.gob.ar/dnda), Ley 11.723. Note: registration is declarative.` |

### 2.3 fto-triage/SKILL.md

| Sección | Agregar AR |
|---------|-----------|
| Patent FTO | `Ley 24.481 patent framework. 20-year term from filing. No utility models for software. Check INPI for active patents in Argentina.` |
| Risk levels | `High: Active INPI patent in same class. Medium: Pending INPI application. Low: No Argentine registration found.` |

### 2.4 infringement-triage/SKILL.md

| Sección | Agregar AR |
|---------|-----------|
| Trademark infringement | `Ley 22.362 Art. 31: criminal penalties (1 month to 3 years imprisonment + fines). Civil action for damages. INPI administrative cancellation procedure.` |
| Copyright infringement | `Ley 11.723 Art. 72: criminal penalties. Civil action. Note: no DMCA equivalent in Argentina; use direct takedown notices to hosting providers under Ley 25.326 and CCyCN.` |

### 2.5 invention-intake/SKILL.md

| Sección | Agregar AR |
|---------|-----------|
| Patent eligibility | `Ley 24.481 Art. 6: discoveries, scientific theories, mathematical methods, software "as such" are not patentable. Biotech: Ley 24.366. Plant varieties: Ley 20.247.` |
| Inventor rights | `Ley 24.481 Art. 36-40: employee inventions. Service inventions belong to employer. Free inventions belong to employee. Mixed inventions: shared.` |

### 2.6 ip-clause-review/SKILL.md

| Sección | Agregar AR |
|---------|-----------|
| IP ownership | `Under CCyCN and Ley 22.362/Ley 24.481, IP rights are assignable. Moral rights (derechos morales) under Ley 11.723 are inalienable and imprescriptible.` |
| Licensing | `Ley 22.362 Art. 30: trademark licenses must be recorded at INPI to be effective against third parties. Ley 24.481: patent licenses must be recorded.` |

### 2.7 oss-review/SKILL.md

| Sección | Agregar AR |
|---------|-----------|
| Open source compliance | `Same as US: GPL, MIT, Apache, etc. are enforceable in Argentina under CCyCN contract law. No specific Argentine OSS legislation.` |
| Copyleft risk | `Note: Argentine courts have not ruled on GPL enforcement. Treat as binding contract under CCyCN Art. 957+.` |

### 2.8 portfolio/SKILL.md

| Sección | Agregar AR |
|---------|-----------|
| Trademark portfolio | `INPI registration: 10-year term, renewable. Classes under Nice Classification. Opposition window: 30 days from Boletín de Marcas publication.` |
| Maintenance | `Use fees (tasas de uso) not required in Argentina. Renewal: every 10 years. Non-use cancellation: 5 years of non-use.` |

### 2.9 takedown/SKILL.md

| Sección | Agregar AR |
|---------|-----------|
| Copyright takedown | `No DMCA in Argentina. Use direct notice to hosting provider under CCyCN liability rules and Ley 25.326. Reference: "Godoy c/ Google" precedent (CSJN).` |
| Trademark takedown | `INPI opposition procedure (30 days). Marketplace takedown (MercadoLibre has IP protection program). Direct cease-and-desist to infringer.` |

### 2.10 cold-start-interview/SKILL.md (ip-legal)

| Sección | Agregar AR |
|---------|-----------|
| Jurisdiction questions | `Where are your IP assets registered? INPI (Argentina)? USPTO? EUIPO? Madrid Protocol?` |
| Enforcement questions | `Have you filed oppositions in the Boletín de Marcas? Do you monitor for INPI publications?` |

### 2.11 customize/SKILL.md (ip-legal)

| Sección | Agregar AR |
|---------|-----------|
| Config options | `Add ip_jurisdiction: [AR, US, EU, global] and inpi_monitoring: [true/false]` |

### 2.12 matter-workspace/SKILL.md (ip-legal)

| Sección | Agregar AR |
|---------|-----------|
| Matter types | `Add: INPI opposition, Boletín de Marcas monitoring, DNDA registration, patent filing (INPI)` |

---

## Fase 3: Skills de litigation-legal (19 skills)

**Alcance:** 19 SKILL.md en `litigation-legal/skills/`
**Complejidad:** Media (menos dependentes de jurisdicción, más procedural)
**Criterio de éxito:** Skills reconocen procedimiento argentino como alternativa válida

### 3.1 Skills prioritarios (los que más tocan jurisdicción)

#### demand-intake/SKILL.md
- Agregar: `CPCCN (Código Procesal Civil y Comercial de la Nación) filing requirements`
- Agregar: `Mediación prejudicial obligatoria (Ley 26.589) before filing in federal courts`
- Agregar: `Competencia: Tribunales Ordinarios de CABA, fueros Comerciales/Civiles/Laborales`

#### brief-section-drafter/SKILL.md
- Agregar formato de escritos argentinos: `Memorándum, Contestación de Demanda, Alegatos, Recurso de Apelación`
- Agregar: `Estructura: I. Objeto, II. Hechos, III. Derecho, IV. Petitorio`
- Agregar: `Citas jurisprudenciales: Fallos CSJN, cámaras nacionales (CNCom, CNFed, CNTrab)`

#### legal-hold/SKILL.md
- Agregar: `No discovery in Argentine civil procedure. Evidence preservation via: custodia de documentos, medidas cautelares (Art. 192+ CPCCN)`
- Agregar: `Document retention: Ley 25.326 (datos personales), Ley 11.683 (procedimiento tributario, 6 años), Ley 20.744 (documentación laboral, 4 años)`

#### subpoena-triage/SKILL.md
- Agregar: `Medidas para mejor proveer (Art. 38 CPCCN), oficios judiciales, peritajes`
- Agregar: `Third-party document requests: Art. 387-390 CPCCN (exhibición de documentos)`

#### privilege-log-review/SKILL.md
- Agregar: `Secreto profesional argentino (Art. 380+ CPCCN, Ley 23.118, códigos de ética de Colegios de Abogados)`
- Agregar: `No attorney-client privilege doctrine. Professional secrecy is broader and absolute.`

### 3.2 Skills secundarios (menos jurisdicción-specific)

| Skill | Cambio |
|-------|--------|
| chronology | Agregar formato de fechas argentino (DD/MM/AAAA), referencias a fallos CSJN |
| claim-chart | Agregar columnas para normativa argentina (LCT, CCyCN, leyes especiales) |
| demand-draft | Agregar estructura de demanda argentina (hechos, derecho, petitorio) |
| demand-received | Agregar plazos procesales argentinos (contestación: 10 días hábiles, excepciones: 6 días) |
| deposition-prep | Agregar: `No depositions in Argentine procedure. Testimonial evidence via informes de parte, confesional, testigos` |
| matter-briefing | Agregar sección de contexto procesal argentino |
| matter-close | Agregar: `Costas procesales (Art. 68+ CPCCN), regulación de honorarios` |
| matter-intake | Agregar jurisdicción argentina como opción |
| matter-update | Sin cambios mayores |
| matter-workspace | Agregar tipos de materia argentinos |
| oc-status | Agregar: `Externos: estudios de abogados argentinos, procuradores` |
| portfolio-status | Agregar: `Litigios en Tribunales de CABA, cámaras de apelación` |

---

## Fase 4: Skills restantes de los otros 7 plugins (~75 skills)

**Alcance:** ~75 SKILL.md en employment-legal, privacy-legal, commercial-legal, corporate-legal, product-legal, ai-governance-legal, regulatory-legal
**Complejidad:** Media-Alta
**Criterio de éxito:** Cada skill reconoce el marco argentino como opción primaria

### 4.1 employment-legal (18 skills pendientes, 1 ya hecho: termination-review)

| Skill | Contenido AR a agregar |
|-------|----------------------|
| **hiring-review** | LCT Art. 10+ (capacidad), Art. 80 (certificados de trabajo previos), Ley 23.590 (no discriminación), Ley 25.326 (datos del empleado), Art. 88 LCT (período de prueba: 3 meses) |
| **wage-hour-qa** | Ya tiene sección AR. Completar: Ley 11.544 (jornada 8h/48h), horas extras al 50%/100%, SAC (decreto ley 23.041/56), divisor vacaciones Art. 155 LCT |
| **worker-classification** | LCT Art. 23 (presunción de laboralidad), Art. 2 (empleador), Art. 25 (solidaridad), teletrabajo Ley 27.555, monotributistas como riesgo de encubrimiento |
| **handbook-updates** | Ley 27.610 (teletrabajo), Ley 26.485 (violencia laboral), Ley 23.592 (actos discriminatorios), protocolo de acoso |
| **policy-drafting** | Referencias a leyes argentinas según dominio |
| **internal-investigation** | Ley 26.485, Ley 27.401 (responsabilidad penal corporativa), protocolo de investigación |
| **leave-tracker** | LCT Art. 156+ (vacaciones), Art. 158 (antigüedad), Art. 177 (licencia maternidad), Art. 159 (licencia paternidad: 2 días, ampliado por convenio) |
| **log-leave** | Mismas referencias que leave-tracker |
| **international-expansion** | Argentina como jurisdicción destino: LCT, convenios colectivos, cargas sociales (~27% sobre nómina) |
| **expansion-kickoff** | Agregar Argentina como opción de expansión |
| **expansion-update** | Agregar referencias argentinas |
| **investigation-*** (5 skills) | Agregar marco argentino: Ley 27.401, Ley 26.485, secreto profesional |
| **matter-workspace** | Agregar tipos de materia argentinos |
| **cold-start-interview** | Agregar preguntas sobre jurisdicción argentina |
| **customize** | Agregar opciones de config argentinas |

### 4.2 privacy-legal (8 skills pendientes)

| Skill | Contenido AR a agregar |
|-------|----------------------|
| **dpa-review** | Ley 25.326 Art. 12 (transferencias internacionales), AAIP no tiene cláusulas estándar publicadas, usar modelo OEA |
| **pia-generation** | Ley 25.326 Art. 11 (decisiones automatizadas), datos sensibles Art. 7, consentimiento Art. 5 |
| **policy-monitor** | Agregar fuentes argentinas: AAIP resolutions, Ley 25.326 updates |
| **reg-gap-analysis** | Agregar Ley 25.326 como framework de referencia |
| **use-case-triage** | Agregar criterios de Ley 25.326 para evaluación de casos de uso |
| **matter-workspace** | Agregar tipos de materia argentinos |
| **cold-start-interview** | Agregar preguntas sobre Ley 25.326, AAIP, bases de datos registradas |
| **customize** | Agregar opciones de config argentinas |

### 4.3 commercial-legal (11 skills pendientes)

| Skill | Contenido AR a agregar |
|-------|----------------------|
| **nda-review** | CCyCN Art. 1363+ (contratos), Ley 25.326 (confidencialidad de datos), Ley 24.766 (secreto industrial) |
| **saas-msa-review** | CCyCN Art. 957+ (contratos electrónicos), Ley 25.506 (firma digital), Ley 24.240 (si es consumidor) |
| **review** | Agregar marco CCyCN como base de análisis |
| **review-proposals** | Agregar referencias argentinas |
| **escalation-flagger** | Agregar triggers argentinos (pesificación Art. 765 CCyCN, Ley 24.240) |
| **renewal-tracker** | Sin cambios mayores |
| **amendment-history** | Sin cambios mayores |
| **stakeholder-summary** | Sin cambios mayores |
| **matter-workspace** | Agregar tipos de materia argentinos |
| **cold-start-interview** | Agregar preguntas sobre CCyCN, jurisdicción argentina |
| **customize** | Agregar opciones de config argentinas |

### 4.4 corporate-legal (12 skills pendientes)

| Skill | Contenido AR a agregar |
|-------|----------------------|
| **board-minutes** | Art. 73 LGS (actas de directorio), Art. 158 CCyCN (resoluciones por escrito), Art. 272 LGS (conflictos), Libro de Actas |
| **entity-compliance** | IGJ/DPPJ reporting, Ley 27.430 (impuesto a las ganancias), Ley 26.831 (mercado de capitales) |
| **closing-checklist** | Agregar pasos argentinos: inscripción IGJ/DPPJ, publicación Boletín Oficial, alta AFIP |
| **diligence-issue-extraction** | Agregar referencias a normativa argentina |
| **material-contract-schedule** | CCyCN framework |
| **integration-management** | Agregar contexto argentino |
| **deal-team-summary** | Sin cambios mayores |
| **tabular-review** | Sin cambios mayores |
| **ai-tool-handoff** | Sin cambios mayores |
| **matter-workspace** | Agregar tipos de materia argentinos |
| **cold-start-interview** | Agregar preguntas sobre LGS, IGJ, tipo societario |
| **customize** | Agregar opciones de config argentinas |

### 4.5 product-legal (6 skills pendientes)

| Skill | Contenido AR a agregar |
|-------|----------------------|
| **launch-review** | ENACOM, Ley 25.326, Ley 24.240, Ley 26.904, Ley 22.802 |
| **marketing-claims-review** | Ley 24.240 (publicidad engañosa), CONAR Argentina, Ley 22.802 (Lealtad Comercial) |
| **feature-risk-assessment** | Agregar criterios argentinos |
| **is-this-a-problem** | Agregar marco regulatorio argentino |
| **matter-workspace** | Agregar tipos de materia argentinos |
| **cold-start-interview** | Agregar preguntas sobre regulación argentina |

### 4.6 ai-governance-legal (9 skills pendientes)

| Skill | Contenido AR a agregar |
|-------|----------------------|
| **aia-generation** | Ley 25.326 Art. 11 (decisiones automatizadas), AAIP guidelines |
| **ai-inventory** | No mandatory registry in Argentina. Voluntary AAIP compliance. |
| **policy-starter** | Agregar referencias argentinas |
| **policy-monitor** | Agregar fuentes argentinas |
| **reg-gap-analysis** | Agregar Ley 25.326 como framework |
| **use-case-triage** | Agregar criterios argentinos |
| **vendor-ai-review** | Agregar consideraciones argentinas |
| **matter-workspace** | Agregar tipos de materia argentinos |
| **cold-start-interview** | Agregar preguntas sobre AAIP, Ley 25.326 |

### 4.7 regulatory-legal (8 skills pendientes)

| Skill | Contenido AR a agregar |
|-------|----------------------|
| **policy-redraft** | Agregar fuentes argentinas: InfoLEG, Boletín Oficial |
| **gap-surfacer** | Agregar reguladores argentinos |
| **gaps** | Agregar marco regulatorio argentino |
| **comments** | Agregar proceso de comentarios en Argentina |
| **matter-workspace** | Agregar tipos de materia argentinos |
| **cold-start-interview** | Agregar preguntas sobre reguladores argentinos |
| **customize** | Agregar opciones de config argentinas |
| **reg-feed-watcher** | Ya tiene feeds argentinos. Verificar que estén completos. |

---

## Fase 5: Integración de agnostic-legal-ar en los plugins

**Alcance:** 5 prompts agnósticos → integrados como secciones de referencia en los plugins
**Complejidad:** Baja (el contenido ya está escrito)
**Criterio de éxito:** El contenido de agnostic-legal-ar es accesible desde los plugins sin necesidad de copiar/pegar manualmente

### 5.1 Mapeo de integración

| Prompt agnóstico | Plugin destino | Sección destino | Acción |
|-----------------|---------------|----------------|--------|
| `prompts/laboral_lct.md` | employment-legal | Nueva sección `## Argentine Employment Law Reference` en CLAUDE.md | Copiar contenido como referencia. Vincular desde skills relevantes (termination-review, hiring-review, wage-hour-qa, worker-classification, leave-tracker) |
| `prompts/privacidad_datos.md` | privacy-legal | Nueva sección `## Argentine Data Protection Reference (Ley 25.326)` en CLAUDE.md | Copiar contenido. Vincular desde dsar-response, dpa-review, pia-generation |
| `prompts/comercial_contratos.md` | commercial-legal | Nueva sección `## Argentine Contract Law Reference (CCyCN)` en CLAUDE.md | Copiar contenido. Vincular desde vendor-agreement-review, nda-review, saas-msa-review |
| `prompts/societario_actas.md` | corporate-legal | Nueva sección `## Argentine Corporate Law Reference (LGS/IGJ)` en CLAUDE.md | Copiar contenido. Vincular desde board-minutes, written-consent, entity-compliance |
| `prompts/propiedad_intelectual.md` | ip-legal | Nueva sección `## Argentine IP Law Reference (INPI/Ley 22.362)` en CLAUDE.md | Copiar contenido. Vincular desde cease-desist, clearance, portfolio, takedown |

### 5.2 Formato de integración

Cada sección de referencia debe seguir este formato:

```markdown
## [Jurisdiction] [Domain] Law Reference

> **Source:** [agnostic-legal-ar/prompts/XXX.md] — Argentina-first framework

### Key Legislation
- [Ley XXXX] — [Nombre] — [Breve descripción]
- [Art. YY] — [Contenido relevante]

### Procedures
- [Procedimiento 1]: [Pasos, plazos, requisitos]

### Common Pitfalls
- [Pitfall 1]: [Descripción + mitigación]

### Cross-Reference
- Used by: [skill-1], [skill-2], [skill-3]
```

---

## Fase 6: Cleanup y validación

**Alcance:** Todo el repositorio
**Complejidad:** Baja
**Criterio de éxito:** Todos los plugins validan sin errores, README refleja estado real

### 6.1 Placeholders US-centric

Buscar y reemplazar los 616+ `[PLACEHOLDER]` que tienen ejemplos exclusivamente US:

| Placeholder actual | Nuevo placeholder |
|---|---|
| `[PLACEHOLDER — e.g., "Delaware, our home jurisdiction"]` | `[PLACEHOLDER — e.g., "Tribunales Comerciales de CABA" / "Delaware, our home jurisdiction"]` |
| `[PLACEHOLDER — NYSE / Nasdaq / other]` | `[PLACEHOLDER — BYMA / ROFEX / NYSE / Nasdaq / other]` |
| `[PLACEHOLDER — EEOC, DOL, state AGs]` | `[PLACEHOLDER — Ministerio de Trabajo, SECLO, AAIP, CNV / EEOC, DOL]` |
| `[PLACEHOLDER — CT Corp / National Registered Agents]` | `[PLACEHOLDER — domicilio social (AR) / CT Corp / registered agent]` |
| `[PLACEHOLDER — Carta / Shareworks]` | `[PLACEHOLDER — Libro de Acciones (AR) / Carta / Shareworks]` |
| `[PLACEHOLDER — California, New York, UK]` | `[PLACEHOLDER — CABA, Buenos Aires, California, UK]` |

### 6.2 Validación técnica

1. Ejecutar `claude plugin validate` en cada plugin:
   ```bash
   for plugin in employment-legal privacy-legal commercial-legal corporate-legal ip-legal litigation-legal product-legal ai-governance-legal regulatory-legal; do
     claude plugin validate $plugin
   done
   ```

2. Ejecutar `validate.py` para schemas:
   ```bash
   python validate.py
   ```

3. Ejecutar `lint-tool-scope.py` para verificar scope:
   ```bash
   python lint-tool-scope.py
   ```

### 6.3 README update

Agregar sección "Estado de Localización Argentina" al README:

```markdown
## Estado de Localización Argentina

| Plugin | CLAUDE.md | Skills | Estado |
|--------|-----------|--------|--------|
| employment-legal | ✅ AR integrado | 20/20 con AR | Completo |
| privacy-legal | ✅ AR integrado | 9/9 con AR | Completo |
| commercial-legal | ✅ AR integrado | 12/12 con AR | Completo |
| corporate-legal | ✅ AR integrado | 13/13 con AR | Completo |
| ip-legal | ✅ AR integrado | 12/12 con AR | Completo |
| litigation-legal | ✅ AR integrado | 19/19 con AR | Completo |
| product-legal | ✅ AR integrado | 7/7 con AR | Completo |
| ai-governance-legal | ✅ AR integrado | 10/10 con AR | Completo |
| regulatory-legal | ✅ AR integrado | 9/9 con AR | Completo |

### Marco Legal Argentino Referenciado
- **Laboral:** LCT 20.744, Ley 11.544, Ley 23.551, Ley 25.323, Ley 25.345, Ley 24.013, Ley 27.555
- **Privacidad:** Ley 25.326, Ley 26.529, resoluciones AAIP
- **Comercial:** CCyCN, Ley 25.506, Ley 24.240, Ley 22.802
- **Societario:** LGS 19.550, CCyCN Art. 158, IGJ/DPPJ, Ley 26.831
- **Propiedad Intelectual:** Ley 22.362, Ley 11.723, Ley 24.481, INPI
- **Procesal:** CPCCN, Ley 23.118, Ley 26.589, Ley 27.401
```

---

## Orden de ejecución recomendado

```
Fase 1 (CLAUDE.md) → employment-legal, privacy-legal, commercial-legal, corporate-legal, ip-legal
Fase 1 (CLAUDE.md) → litigation-legal, product-legal, ai-governance-legal, regulatory-legal
Fase 2 (ip-legal skills) → cease-desist, clearance, fto-triage, infringement-triage
Fase 2 (ip-legal skills) → invention-intake, ip-clause-review, oss-review, portfolio, takedown
Fase 2 (ip-legal skills) → cold-start-interview, customize, matter-workspace
Fase 3 (litigation-legal skills) → demand-intake, brief-section-drafter, legal-hold, subpoena-triage, privilege-log-review
Fase 3 (litigation-legal skills) → remaining 14 skills
Fase 4 (otros plugins skills) → employment-legal (18 skills)
Fase 4 (otros plugins skills) → privacy-legal (8 skills)
Fase 4 (otros plugins skills) → commercial-legal (11 skills)
Fase 4 (otros plugins skills) → corporate-legal (12 skills)
Fase 4 (otros plugins skills) → product-legal, ai-governance-legal, regulatory-legal
Fase 5 (integrar agnostic-legal-ar) → 5 prompts en 5 plugins
Fase 6 (cleanup + validación) → placeholders, validación, README
```

---

## Métricas de éxito

| Métrica | Antes | Después |
|---------|-------|---------|
| CLAUDE.md con contenido AR | 0/9 | 9/9 |
| Skills con contenido AR | ~15/140 | 140/140 |
| Placeholders US-only | 616+ | 0 (todos con alternativa AR) |
| agnostic-legal-ar integrado | 0/5 | 5/5 |
| Plugins validan sin errores | ✅ | ✅ |
| README refleja estado real | ❌ | ✅ |
