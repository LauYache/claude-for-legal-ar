#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harness Ejecutor Agnóstico de Prompts Legales de Argentina
Este script permite cargar un prompt de sistema local, adjuntar un documento 
de entrada y enviarlo a las APIs de Anthropic o OpenAI sin requerir dependencias externas (usa urllib).

Uso:
  export ANTHROPIC_API_KEY="tu-api-key"
  python3 run_agnostic.py --prompt laboral_lct --input caso_empleado.txt --provider anthropic

  export OPENAI_API_KEY="tu-api-key"
  python3 run_agnostic.py --prompt comercial_contratos --input contrato.txt --provider openai --model gpt-4o
"""

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

# Directorios de referencia
BASE_DIR = Path(__file__).resolve().parents[1]
PROMPTS_DIR = BASE_DIR / "prompts"


def load_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error al leer el archivo {path}: {e}", file=sys.stderr)
        sys.exit(1)


def call_anthropic(system_prompt: str, user_content: str, model: str, api_key: str) -> str:
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    payload = {
        "model": model,
        "max_tokens": 4096,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": user_content}
        ]
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data["content"][0]["text"]
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"Error de API Anthropic ({e.code}): {error_body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error de conexión: {e}", file=sys.stderr)
        sys.exit(1)


def call_openai(system_prompt: str, user_content: str, model: str, api_key: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "content-type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"Error de API OpenAI ({e.code}): {error_body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error de conexión: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Harness ejecutor de prompts legales agnósticos.")
    parser.add_argument(
        "-p", "--prompt", 
        required=True, 
        help="Nombre del archivo de prompt en prompts/ (ej. laboral_lct, comercial_contratos)"
    )
    parser.add_argument(
        "-i", "--input", 
        required=True, 
        help="Ruta al archivo con el documento o caso legal a analizar"
    )
    parser.add_argument(
        "--provider", 
        choices=["anthropic", "openai"], 
        default="anthropic",
        help="Proveedor de API a utilizar (anthropic o openai)"
    )
    parser.add_argument(
        "-m", "--model", 
        help="Modelo de LLM específico (por defecto usa claude-3-5-sonnet-latest o gpt-4o)"
    )

    args = parser.parse_args()

    # Buscar el prompt de sistema
    prompt_file = PROMPTS_DIR / f"{args.prompt}.md"
    if not prompt_file.exists():
        # Intentar con extensión .md directa si la especificaron
        prompt_file = PROMPTS_DIR / args.prompt
        if not prompt_file.exists():
            print(f"Error: El prompt '{args.prompt}' no existe en {PROMPTS_DIR}", file=sys.stderr)
            print("Prompts disponibles:", file=sys.stderr)
            for f in PROMPTS_DIR.glob("*.md"):
                print(f"  - {f.stem}", file=sys.stderr)
            sys.exit(1)

    system_prompt = load_file(prompt_file)
    user_content = load_file(Path(args.input))

    if args.provider == "anthropic":
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print("Error: La variable de entorno ANTHROPIC_API_KEY no está configurada.", file=sys.stderr)
            sys.exit(1)
        model = args.model or "claude-3-5-sonnet-latest"
        print(f"Enviando consulta a Anthropic ({model})...")
        response = call_anthropic(system_prompt, user_content, model, api_key)
    else:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("Error: La variable de entorno OPENAI_API_KEY no está configurada.", file=sys.stderr)
            sys.exit(1)
        model = args.model or "gpt-4o"
        print(f"Enviando consulta a OpenAI ({model})...")
        response = call_openai(system_prompt, user_content, model, api_key)

    print("\n--- RESPUESTA DEL ASISTENTE LEGAL ---")
    print(response)


if __name__ == "__main__":
    main()
