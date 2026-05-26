# Catálogo de Fuentes Regulatorias — Argentina

Este catálogo sirve de referencia para el `reg-feed-watcher` en el contexto argentino. Detalla los organismos emisores de normas y regulaciones, sus canales de publicación y la forma en que Claude puede acceder a sus actualizaciones.

---

## Fuentes Nacionales Primarias

| Organismo | URL / Feed | Formato | Cobertura | Notas |
|---|---|---|---|---|
| **Boletín Oficial de la República Argentina (BORA)** | `https://www.boletinoficial.gob.ar/` | HTML / PDF / API | Leyes, decretos, resoluciones ministeriales y de entes autárquicos. | Publicación diaria (días hábiles). Es la fuente primaria de validez de toda norma en el país. Permite búsquedas por rubro (Primera Sección: Legislación y Avisos Oficiales). |
| **InfoLEG (Base de Datos Legislativa)** | `http://servicios.infoleg.gob.ar/infolegInternet/rss/anexos-boletinoficial.xml` | RSS / HTML | Leyes nacionales, decretos y resoluciones actualizadas y consolidadas. | Provisto por el Ministerio de Justicia. Es excelente para obtener textos consolidados y modificaciones de leyes vigentes. |
| **Agencia de Acceso a la Información Pública (AAIP)** | `https://www.argentina.gob.ar/aaip/novedades` | HTML | Resoluciones sobre protección de datos personales (Ley 25.326), acceso a la información y políticas públicas de privacidad. | Autoridad de aplicación de protección de datos. Clave para el módulo `privacy-legal`. |
| **Administración Federal de Ingresos Públicos (AFIP)** | `https://www.afip.gob.ar/novedades/` | HTML / RSS (vía InfoLEG) | Resoluciones Generales (RG), normativas impositivas, previsionales, de seguridad social y aduaneras. | Monitorear novedades impositivas semanales. Afecta directamente al módulo societario y de empleo. |
| **Banco Central de la República Argentina (BCRA)** | `https://www.bcra.gob.ar/PublicacionesEstadisticas/normas_ultimas.asp` | HTML / PDF | Comunicaciones A, B, C y resoluciones del directorio (normativa cambiaria y financiera). | Crítico para empresas extranjeras que operan en Argentina debido a regulaciones del Mercado Libre de Cambios (MULC). |
| **Comisión Nacional de Valores (CNV)** | `https://www.argentina.gob.ar/cnv` | HTML / PDF | Normativa del mercado de capitales, fideicomisos financieros y sociedades emisoras. | Crítico para entidades financieras y corporaciones cotizantes. |
| **Inspección General de Justicia (IGJ)** | `https://www.argentina.gob.ar/justicia/igj/novedades` | HTML | Resoluciones Generales aplicables a sociedades comerciales (S.A., S.R.L., S.A.S.) y entidades civiles en CABA. | Clave para el cumplimiento societario (`corporate-legal`). Para provincia de Buenos Aires, el equivalente es la **Dirección Provincial de Personas Jurídicas (DPPJ)**. |
| **Instituto Nacional de la Propiedad Industrial (INPI)** | `https://www.argentina.gob.ar/inpi/boletines` | PDF / HTML | Boletines de marcas, patentes y modelos de utilidad. Oposiciones y resoluciones de concesión. | Clave para el módulo `ip-legal` y clearance de marcas. |
| **Superintendencia de Riesgos del Trabajo (SRT)** | `https://www.argentina.gob.ar/srt/normativa` | HTML | Normas sobre higiene y seguridad laboral, riesgos de trabajo y resoluciones de comisiones médicas. | Crítico para el módulo de derecho laboral (`employment-legal`). |

---

## Fuentes Secundarias e Informativos Legales

Estas fuentes resumen y comentan la legislación primaria. Deben usarse para identificar novedades y luego contrastarlas con el Boletín Oficial o InfoLEG.

| Fuente | URL / Feed | Formato | Cobertura | Notas |
|---|---|---|---|---|
| **Errepar / Erreius** | `https://www.errepar.com/` | Suscripción / Portal | Novedades tributarias, societarias, laborales y civiles de Argentina. | Editorial líder en información profesional. Requiere suscripción paga para textos completos, pero publica resúmenes abiertos de gran valor. |
| **Dialéctica / El Dial** | `https://www.eldial.com/` | Portal | Jurisprudencia, doctrina y novedades legislativas argentinas. | Diario jurídico argentino. Excelente para seguir fallos judiciales de cámaras nacionales y provinciales. |
| **La Ley (Thomson Reuters Argentina)** | `https://laley.thomsonreuters.com.ar/` | Suscripción | Doctrina, jurisprudencia nacional y provincial anotada. | Integrado en plataformas de investigación legal de TR locales. |
| **Abogados.com.ar** | `https://abogados.com.ar/feed` | RSS | Noticias del sector legal, artículos de doctrina de estudios de abogados locales y fallos relevantes. | Excelente para detectar tendencias y resúmenes de firmas líderes (Marval, O'Farrell, Allende & Brea, etc.). |

---

## Estrategia de Monitoreo Local

1. **El Boletín Oficial (BORA)** es la fuente suprema de verdad. Cualquier cambio en las obligaciones de cumplimiento debe rastrearse preferentemente allí.
2. **InfoLEG** debe ser la fuente de consulta para ver cómo quedó redactada una ley nacional tras sufrir modificaciones (por ejemplo, los cambios introducidos por Decretos de Necesidad y Urgencia - DNU o Leyes Ómnibus).
3. **Para alertas ad-hoc cambiarias e impositivas**, el monitoreo de los portales del BCRA y de la AFIP es indispensable debido al dinamismo del marco impositivo y cambiario argentino.
