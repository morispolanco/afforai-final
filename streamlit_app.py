import streamlit as st
import requests
from googleapiclient.discovery import build
import json

# Carga las credenciales de la API de Afforai
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Define la función para buscar información sobre leyes en Guatemala
def get_law_information(query):
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

    # Busca la información relevante sobre leyes
    law_information = result.get("data", {}).get("answer")
    
    return law_information

# Inicia la aplicación Streamlit
st.title("Información sobre leyes en Guatemala")
st.write("Ingrese su pregunta sobre las leyes en Guatemala:")
user_query = st.text_input("Pregunta")

# Busca información sobre leyes
law_information = get_law_information(user_query)

# Muestra el resultado
if law_information:
    st.success(f"Aquí está la información sobre las leyes en Guatemala:\n\n{law_information}")
else:
    st.error("Lo siento, no se encontró información sobre esa pregunta en relación a las leyes de Guatemala.")
