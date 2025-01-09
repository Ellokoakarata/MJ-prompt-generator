#generator.py

import os
from datetime import datetime
from openai import OpenAI

"""
Este script:
1. Usa la clase OpenAI de la librería `openai` (tal como indica tu documentación).
2. Toma como entrada (input) las ideas de usuario.
3. Genera 5 prompts basados en el JSON system_prompt dado, **siempre en inglés**.
4. Guarda dichos prompts en un archivo .md con fecha y hora.
5. Utiliza la API Key almacenada en la variable de entorno OPENAI_API_KEY.
6. Ofrece la posibilidad de incluir parámetros adicionales de Midjourney (ej.: --seed 42).
   Estos se añaden al final de las ideas del usuario para lograr mayor flexibilidad creativa.
"""

# Obtenemos la API Key de la variable de entorno
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la variable de entorno OPENAI_API_KEY. Por favor, configúrala primero.")

# Instanciamos el cliente con la documentación que diste
client = OpenAI(api_key=api_key)

# Aquí almacenamos la definición JSON de "system_prompt"
SYSTEM_PROMPT_JSON = r"""
{
  "system_prompt": {
    "name": "Generación de Prompts Estilo Anarco-Punk Psico-Caótico",
    "description": "Esta plantilla guía a la IA para producir prompts en ingles con un estilo que combine rebeldía punk, caos psicodélico y elementos fractales. Incluye parámetros y estructura recomendada para lograr resultados impactantes en herramientas generadoras de imágenes.",
    "parameters": {
      "// Personalización extra, se pueden agregar más tokens si es necesario": "",
      "personalization_tokens": [
        "--p m7275944197297799186",
        "--p m7275565311808503830"
      ],
      "chaos": 33,
      "stylize": 666,
      "// Ajustar la calidad si se desea más detalle  y esta es la documentacion from openai import OpenAI": "",
      "quality": 2,
      "// Relaciones de aspecto sugeridas": "",
      "aspect_ratios": [
        "2:3",
        "3:2",
        "16:9",
        "9:16"
      ]
    },
    "structure": {
      "title": "Título o etiqueta (opcional)",
      "sections": [
        {
          "section_name": "Personaje Central",
          "description": "Definir la apariencia y actitud del/la protagonista en clave anarco-punk (peinados extremos, vestimenta caótica, accesorios, etc.)."
        },
        {
          "section_name": "Acción o Escenario",
          "description": "Describir la acción principal (postura, movimiento, interacción) y el tipo de entorno (habitaciones grunge, azoteas distópicas, callejones con grafiti, etc.)."
        },
        {
          "section_name": "Aspectos Psico-Visuales",
          "description": "Integrar elementos fractales, efectos psicodélicos, humo, luces neón, distorsiones y glitches visuales que refuercen la estética caótica."
        },
        {
          "section_name": "Parámetros para la Herramienta de IA",
          "description": "Incluir los parámetros y tokens esenciales para Midjourney u otra IA, como --p, --chaos, --stylize, --ar, --quality, etc."
        }
      ]
    },
    "examples": [
      {
        "title": "Retrato Caótico con Vibras Punk",
        "prompt_sections": [
          {
            "section_name": "Personaje Central",
            "content": "Un anarco-punk con el cabello verde erizado, chaqueta de cuero desgastada llena de parches anarquistas y varios piercings en la cara."
          },
          {
            "section_name": "Acción o Escenario",
            "content": "Primer plano con un ángulo ligeramente bajo, en un cuartucho lleno de pantallas CRT con glitch y cables enredados."
          },
          {
            "section_name": "Aspectos Psico-Visuales",
            "content": "Fractales neón que emanan desde su cabeza, humo psicodélico que se retuerce con colores rojos y morados, y reflejos distorsionados en las pantallas."
          },
          {
            "section_name": "Parámetros para la Herramienta de IA",
            "content": "Incluir: --p m7275944197297799186, --p m7275565311808503830, --chaos 33, --stylize 666, --ar 2:3, --quality 2 (opcional)."
          }
        ],
        "final_prompt": "An anarcho-punk with spiked green hair, wearing a torn leather jacket covered in anarchist patches, stares intensely at the viewer. Surrounded by flickering CRT screens and twisted wires in a grungy backroom. Neon fractal auras swirl from their head, and psychedelic smoke coils around them. --p m7275944197297799186 --p m7275565311808503830 --chaos 33 --stylize 666 --ar 2:3 --quality 2"
      },
      {
        "title": "Azotea Punk Bajo la Tormenta",
        "prompt_sections": [
          {
            "section_name": "Personaje Central",
            "content": "Punk con mohawk rojo y chaqueta con remaches metálicos, tatuado con símbolos anarquistas y diseños fractales."
          },
          {
            "section_name": "Acción o Escenario",
            "content": "De pie en una azotea resquebrajada bajo un cielo oscuro con relámpagos que iluminan la silueta de edificios distópicos."
          },
          {
            "section_name": "Aspectos Psico-Visuales",
            "content": "Corrientes de aire distorsionadas por glitch, fractales color violeta en el cielo, y grafitis psicodélicos en el borde de la azotea."
          },
          {
            "section_name": "Parámetros para la Herramienta de IA",
            "content": "Incluir: --p m7275944197297799186, --p m7275565311808503830, --chaos 33, --stylize 666, --ar 3:2, --quality 2 (opcional)."
          }
        ],
        "final_prompt_example": "A mohawk-wearing anarcho-punk stands on a crumbling rooftop, lightning slicing through a stormy sky swirling with violet fractals. Neon graffiti flickers along the parapet, glitching in the flicker of distant neon signs. --p m7275944197297799186 --p m7275565311808503830 --chaos 33 --stylize 666 --ar 3:2 --quality 2"
      }
    ]
  }
}
"""

def generar_cinco_prompts(ideas_usuario: str) -> list:
    """
    Genera 5 prompts usando la documentación y el estilo de la IA:
    - Se basa en el JSON (SYSTEM_PROMPT_JSON).
    - Recibe las ideas del usuario y produce 5 prompts, cada uno en inglés.
    - Retorna lista con los 5 prompts (strings).
    """

    # Construimos el mensaje para el modelo
    system_message = (
        "Usa el siguiente JSON de referencia para crear 5 prompts que mezclen "
        "las ideas del usuario con el estilo Anarco-Punk Psico-Caótico descrito. "
        "No des explicaciones, solo outputs finales. "
        "Recuerda que cada prompt debe estar en inglés:\n\n"
        f"{SYSTEM_PROMPT_JSON}\n"
    )

    user_message = (
        f"Estas son las ideas del usuario:\n{ideas_usuario}\n\n"
        "Crea 5 prompts siguiendo la estructura y estilo del JSON. "
        "Cada prompt debe ser un solo bloque de texto y **estar en inglés**."
    )

    # Llamada al método chat.completions.create según tu documentación
    print(">>> Generando prompts con la IA... (podría tardar unos segundos)")
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",  # Ajusta el modelo según tus necesidades
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        response_format={"type": "text"},
        temperature=0.89,
        max_tokens=2000,   # Ajustado para permitir respuestas más largas
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extraemos el contenido de la respuesta
    raw_text = response.choices[0].message.content.strip()

    # Suponiendo que vienen 5 prompts separados por doble salto de línea
    prompts = raw_text.split("\n\n")

    # Aseguramos que queden exactamente 5
    if len(prompts) > 5:
        prompts = prompts[:5]
    elif len(prompts) < 5:
        prompts += ["Prompt vacío (falta contenido)"] * (5 - len(prompts))

    print(">>> Los 5 prompts han sido generados correctamente.\n")
    return prompts

def main():
    # Pedimos ideas al usuario
    ideas = input("Ingresa tus ideas para la generación de prompts: ")

    # (Opcional) Permitimos que el usuario agregue parámetros de Midjourney extra
    extra_params = input("¿Deseas añadir parámetros adicionales de Midjourney? (opcional): ")
    if extra_params.strip():
        # Se añade al final de las ideas:
        ideas += f"\n\nParámetros adicionales de MJ: {extra_params}"

    # Generamos los 5 prompts
    print(">>> Iniciando la generación de 5 prompts en inglés...")
    prompts_generados = generar_cinco_prompts(ideas)

    # Creamos nombre de archivo con fecha y hora
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"prompts_{timestamp}.md"

    print(">>> Convirtiendo prompts a formato Markdown y guardando en archivo...")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Prompts generados ({timestamp})\n\n")
        for i, prompt in enumerate(prompts_generados, start=1):
            print(f"   - Guardando Prompt {i} en el archivo...")
            f.write(f"## Prompt {i}\n")
            f.write(f"{prompt}\n\n")

    print(f"\n>>> Se generaron 5 prompts y se guardaron en '{filename}'.")
    print(">>> ¡Listo! Ya tienes tus prompts para Midjourney.")

if __name__ == "__main__":
    main()
