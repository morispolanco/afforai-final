import streamlit as st
import requests
from googleapiclient.discovery import build
import json 

# Carga las credenciales de la API de Afforai
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Define la función para responder preguntas sobre las leyes de Guatemala
def get_answer(question):
    # Inicializa el cliente de Google Cloud Translation
    translation_client = build("translate", "v3")

    # Traducir la pregunta al español
    translated_question = translation_client.translate(question, target="es").get("translatedText")

    # Construye la consulta para la API de Afforai
    query = f"{translated_question} guatemala leyes"

    # Realiza la solicitud a la API de Afforai
    response = requests.post(
        "https://api.afforai.com/api/api_completion",
        json={
            "apiKey": api_key,
            "sessionID": session_id,
            "history": [{"role": "user", "content": query}],
            "powerful": True,
            "google": True
        }
    )

    # Obtén el resultado de la API de Afforai
    result = json.loads(response.text)

    # Busca la respuesta a la pregunta
    answer = None
    for message in result["data"]["messages"]:
        if message["role"] == "assistant":
            answer = message["content"]
            break

    # Traducir la respuesta al inglés
    translated_answer = translation_client.translate(answer, target="en").get("translatedText")

    return translated_answer

# Inicia la aplicación Streamlit
st.title("Responder preguntas sobre las leyes de Guatemala")
st.write("Ingrese su pregunta:")
question = st.text_input("Pregunta")

# Obtiene la respuesta a la pregunta
answer = get_answer(question)

# Muestra el resultado
if answer:
    st.success(answer)
else:
    st.error("Lo siento, no puedo responder a esa pregunta.")
```
