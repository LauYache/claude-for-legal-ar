# Versión Agnóstica — Argentina Legal Prompts

Esta carpeta contiene una versión de las directrices y habilidades de análisis legal argentino **completamente desacoplada** de la estructura propietaria de plugins de Claude Code o Claude Cowork.

Puedes utilizar estos prompts en cualquier cliente de IA (como OpenCode, ChatGPT, Aider, LibreChat, Dify, Flowise, Copilot Studio) o integrarlos directamente en tus propios scripts de Python/Node.js.

> **Nota:** Esta carpeta es una suite de prompts standalone — **no es un plugin instalable** con `/plugin install`. No contiene `.claude-plugin/plugin.json` ni aparece en `marketplace.json`. Si querés instalar las capacidades legales argentinas como plugin de Claude Code, usá los plugins individuales (`employment-legal`, `corporate-legal`, etc.) desde el directorio raíz del repositorio.

## Estructura de la Carpeta

*   **`prompts/`**: Contiene los prompts de sistema auto-contenidos redactados en Markdown para cada área:
    *   [`laboral_lct.md`](./prompts/laboral_lct.md): Despidos, indemnizaciones Art. 245 LCT, cálculo de horas extras Ley 11.544, y clasificación de contratistas.
    *   [`privacidad_datos.md`](./prompts/privacidad_datos.md): Respuestas a solicitudes de derechos de acceso y supresión bajo la Ley N° 25.326.
    *   [`comercial_contratos.md`](./prompts/comercial_contratos.md): Revisión contractual en pesos/dólares (Art. 765 CCyCN), firmas electrónicas (Ley 25.506) y competencia judicial.
    *   [`societario_actas.md`](./prompts/societario_actas.md): Redacción y validación de actas societarias y resoluciones sin reunión (Art. 158 CCyCN y LGS 19.550).
    *   [`propiedad_intelectual.md`](./prompts/propiedad_intelectual.md): Clearance de marcas e INPI (Ley de Marcas 22.362).
*   **`harness/`**:
    *   [`run_agnostic.py`](./harness/run_agnostic.py): Un script en Python simple para automatizar el envío de un prompt de sistema, un contrato/documento local y la consulta al modelo que elijas (OpenAI, Anthropic, Gemini, etc.).

## Cómo Utilizar los Prompts en Clientes Web (ChatGPT, Claude Pro, etc.)

1.  Abre el archivo `.md` de la habilidad que te interese dentro de `prompts/`.
2.  Copia todo el contenido de las instrucciones.
3.  Pégalo como **Prompt de Sistema** (System Prompt / Custom Instructions / System Message) en tu cliente de IA.
4.  Adjunta o pega el contrato, caso o datos del empleado como prompt de usuario, y realiza tu consulta.

## Cómo Utilizar en OpenCode / Aider (Agentes de Consola)

Puedes indicar directamente al agente de consola que consuma el prompt de sistema local para guiar su respuesta. Por ejemplo, en tu prompt de OpenCode:

> "Usa las instrucciones en `agnostic-legal-ar/prompts/comercial_contratos.md` como sistema y analiza el contrato adjunto `contrato-proveedor.txt`."
