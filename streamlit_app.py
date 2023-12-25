import streamlit as st
import requests
from googleapiclient.discovery import build
import json

# Carga las credenciales de la API de Afforai
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Define la función para buscar el precio más bajo
def get_lowest_price(product_name):
    # Inicializa el cliente de Google Cloud Translation
    translation_client = build("translate", "v3")

    # Traducir el nombre del producto al español
    translated_name = translation_client.translate(product_name, target="es").get("translatedText")

    # Construye la consulta para la API de Afforai
    query = f"{translated_name} precio guatemala"

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

    # Busca el enlace con el precio más bajo
    lowest_price_link = None
    for link in result["data"]["links"]:
        if link["link"] and "precio" in link["link"].lower():
            lowest_price_link = link["link"]
            break

    # Extrae el precio más bajo
    if lowest_price_link:
        match = re.search(r"precio:\s*(\d+)", lowest_price_link)
        if match:
            return int(match.group(1))
    return None

# Inicia la aplicación Streamlit
st.title("Responder preguntas sobre las leyes de Guatemala")
st.write("Ingrese su pregunta:")
product_name = st.text_input("Pregunta")

# Busca la respuesta
response = get_response(product_name)

# Muestra el resultado
if response:
    st.success(response)
else:
    st.error("No se encontró información sobre su pregunta.")
else:
    st.error(f"No se encontró información sobre el precio de {product_name} en Guatemala.")
