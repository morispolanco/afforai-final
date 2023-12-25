
import streamlit as st
import requests
from googleapiclient.discovery import build
import json

# Carga las credenciales de la API de Afforai
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Define la función para buscar la información de la ley
def get_law_information(law_name):
    # Inicializa el cliente de Google Cloud Translation
    translation_client = build("translate", "v3")

    # Traducir el nombre de la ley al español
    translated_name = translation_client.translate(law_name, target="es").get("translatedText")

    # Construye la consulta para la API de Afforai
    query = f"{translated_name} guatemala ley"

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

    # Busca la información de la ley
    law_information = None
    for link in result["data"]["links"]:
        if link["link"] and "ley" in link["link"].lower():
            law_information = link["link"]
            break

    # Extrae la información de la ley
    if law_information:
        match = re.search
