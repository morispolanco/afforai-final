import streamlit as st
import requests

# Define la función para procesar la pregunta y obtener la respuesta
def obtener_respuesta(pregunta):
    try:
        # Configura los parámetros de la API
        api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
        session_id = "65489d7c9ad727940f2ab26f"
        url = "https://api.afforai.com/api/api_completion"
        headers = {"Content-Type": "application/json"}
        data = {
            "apiKey": api_key,
            "sessionID": session_id,
            "history": [{"role": "user", "content": pregunta}],
            "powerful": False,
            "google": True
        }

        # Realiza la solicitud POST a la API
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Lanza una excepción si la solicitud falla

        # Extrae la respuesta de la API
        respuesta = response.json()["completions"][0]["data"]["content"]

        return respuesta

    except Exception as e:
        return f"Ocurrió un error al procesar la solicitud: {e}"


# Interfaz de usuario de la aplicación
st.title("Leyes de Guatemala")

pregunta = st.text_input("Ingresa tu pregunta sobre las leyes de Guatemala:")

if pregunta:
    respuesta = obtener_respuesta(pregunta)
    st.write("**Respuesta:**")
    st.write(respuesta)
