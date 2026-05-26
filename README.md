# Claude for Legal - Argentina (Adaptación Local y Versión Agnóstica / Local Adaptation & Agnostic Version)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Jurisdiction](https://img.shields.io/badge/Jurisdiction-Argentina-blue.svg)](#)
[![Compatibility](https://img.shields.io/badge/Compatibility-Claude_Code-orange.svg)](#)

Esta es una adaptación y extensión del repositorio original `anthropics/claude-for-legal` para la República Argentina, ajustada a su marco regulatorio, normativo y comercial (BORA, InfoLEG, AFIP, BCRA, CNV, LCT, Ley de Protección de Datos Personales 25.326, CCyCN, etc.).  
*This is an adaptation and extension of the original `anthropics/claude-for-legal` repository for the Argentine Republic, adjusted to its regulatory, normative, and commercial framework (BORA, InfoLEG, AFIP, BCRA, CNV, LCT, Personal Data Protection Law 25,326, CCyCN, etc.).*

![Claude Code Argentina en Acción](./references/images/claude_code_screenshot.png)

Además de mantener la estructura original compatible con **Claude Code** y **Claude Desktop/Cowork**, se incluye una **versión agnóstica de prompts e instructivos de sistema** para utilizar esta inteligencia legal en cualquier otro cliente o modelo (como OpenCode, Aider, ChatGPT, Claude.ai, etc.).  
*In addition to maintaining the original structure compatible with **Claude Code** and **Claude Desktop/Cowork**, an **agnostic version of prompts and system instructions** is included to use this legal intelligence in any other client or model (such as OpenCode, Aider, ChatGPT, Claude.ai, etc.).*

---

## Adaptaciones Clave (Marco Normativo) / Key Adaptations (Regulatory Framework)

El repositorio localiza el análisis legal en las siguientes áreas críticas:  
*The repository localizes legal analysis in the following critical areas:*

*   **Laboral (`employment-legal`):** Despidos e indemnizaciones bajo la LCT N° 20.744 (antigüedad Art. 245, preaviso Art. 232, integración del mes Art. 233, protecciones por maternidad/matrimonio), encuadre de monotributistas (Art. 23 LCT) y horas extras (Ley 11.544).  
    *Labor (`employment-legal`): Dismissals and severance pay under LCT No. 20,744 (severance Art. 245, notice Art. 232, month integration Art. 233, maternity/marriage protection), worker classification of monotributistas (Art. 23 LCT), and overtime (Law 11,544).*
*   **Privacidad (`privacy-legal`):** Procesamiento de solicitudes de derechos ARCO bajo la Ley 25.326. Respuestas estrictas en 10 días corridos (Acceso) y 5 días hábiles (Supresión/Rectificación) sin prórrogas automáticas.  
    *Privacy (`privacy-legal`): Processing of ARCO rights requests under Law 25,326. Strict response times of 10 calendar days (Access) and 5 business days (Deletion/Rectification) without automatic extensions.*
*   **Societario (`corporate-legal`):** Actas y resoluciones por escrito según la Ley General de Sociedades N° 19.550 y Art. 158 del CCyCN. Abstención de directores por conflicto de interés (Art. 272 LGS).  
    *Corporate (`corporate-legal`): Minutes and written resolutions under General Corporations Law No. 19,550 and Art. 158 of the CCyCN. Abstention of directors due to conflict of interest (Art. 272 LGS).*
*   **Comercial (`commercial-legal`):** Firma digital vs. electrónica (Ley 25.506) y cláusulas de dolarización/pesificación (protección ante el Art. 765 del CCyCN y prórrogas de jurisdicción Art. 2605).  
    *Commercial (`commercial-legal`): Digital vs. electronic signature (Law 25,506) and dollarization/pesification clauses (protection against Art. 765 of the CCyCN and jurisdiction clauses Art. 2,605).*
*   **Propiedad Intelectual (`ip-legal`):** Clearance marcario e investigación de similitud gráfica/fonética/conceptual bajo la Ley de Marcas N° 22.362 y el boletín de oposiciones del INPI (30 días).  
    *Intellectual Property (`ip-legal`): Trademark clearance and graphic/phonetic/conceptual similarity analysis under Trademark Law No. 22,362 and the INPI opposition bulletin (30 days).*

---

## Inicio Rápido / Quick Start

### Opción A: En Claude Code (Plugins) / Option A: In Claude Code (Plugins)
1. **Registra este repositorio como un marketplace local:**  
   *Register this repository as a local marketplace:*
   ```bash
   /plugin marketplace add /Users/lbyache/Documents/repositorios/claude-for-legal-ar
   ```
2. **Instala los plugins que necesites:**  
   *Install the plugins you need:*
   ```bash
   /plugin install employment-legal@claude-for-legal-ar
   /plugin install commercial-legal@claude-for-legal-ar
   ```
3. **Reinicia Claude Code y corre la entrevista inicial:**  
   *Restart Claude Code and run the initial setup interview:*
   ```bash
   /employment-legal:cold-start-interview
   ```

### Opción B: En Otros Clientes/Modelos (Suite Agnóstica) / Option B: In Other Clients/Models (Agnostic Suite)
Si usas OpenCode, Aider o ChatGPT, puedes usar directamente los prompts Markdown autoportantes y el ejecutor Python:  
*If you use OpenCode, Aider, or ChatGPT, you can directly use the self-contained Markdown prompts and the Python runner:*
```bash
cd agnostic-legal-ar
export ANTHROPIC_API_KEY="tu-api-key"
python3 harness/run_agnostic.py --prompt laboral_lct --input tu_documento.txt
```

---

## Estructura del Repositorio / Repository Structure

*   **`agnostic-legal-ar/`** - Suite de prompts y runner de Python desacoplados de Claude Code. / *Agnostic prompt suite and Python runner.*
*   **`[plugin-name]-legal/`** - Plugins de especialidad para Claude Code/Cowork. / *Specialty plugins for Claude Code/Cowork.*
*   **`references/`** - Catálogo de fuentes legales oficiales de Argentina (`ar-legal-catalog.md`). / *Catalog of official Argentine legal sources.*
*   **`managed-agent-cookbooks/`** - Recetas para desplegar agentes automáticos en la nube. / *Cookbooks for deploying managed agents in the cloud.*
*   **`docs/`** - Documentación extendida y guías de referencia. / *Extended documentation and reference guides.*

---

## Documentación y Licencia / Documentation & License

*   Para consultar el manual de uso extendido de todos los conectores, plugins oficiales originales y configuraciones avanzadas, lee la [Guía de Referencia Completa (Original)](./docs/original_reference.md).  
    *To consult the extended user manual for all connectors, original official plugins, and advanced configurations, read the [Complete Reference Guide (Original)](./docs/original_reference.md).*
*   Para ver el catálogo detallado de fuentes de información y reguladores argentinos, consulta el [Catálogo de Fuentes Legales Argentinas](./references/ar-legal-catalog.md).  
    *To see the detailed catalog of information sources and Argentine regulators, consult the [Argentine Legal Sources Catalog](./references/ar-legal-catalog.md).*

Licensed under the [Apache License, Version 2.0](LICENSE).

Copyright 2026 Anthropic PBC.  
Adaptación para la República Argentina y Suite Agnóstica Copyright 2026 LauYache.
