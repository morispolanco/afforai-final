import streamlit as st
import requests

# Carga las credenciales de la API de Afforai
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Define la función para responder preguntas sobre las leyes de Guatemala
def get_answer(question):
    # Construye la consulta para la API de Afforai
    query = f"{question} guatemala leyes"

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
    result = response.json()

    # Busca la respuesta a la pregunta
    answer = None
    for message in result["data"]["messages"]:
        if message["role"] == "assistant":
            answer = message["content"]
            break

    return answer

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
