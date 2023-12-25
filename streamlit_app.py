import streamlit as st
import requests
from googleapiclient.discovery import build
import json

# Load Afforai API credentials
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Define the function to answer questions about the laws of Guatemala
def get_legal_information(question):
    # Initialize the Google Cloud Translation client
    translation_client = build("translate", "v3")

    # Translate the question to Spanish
    translated_question = translation_client.translate(question, target="es").get("translatedText")

    # Construct the query for the Afforai API
    query = f"leyes guatemala {translated_question}"

    # Make the request to the Afforai API
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

    # Get the result from the Afforai API
    result = json.loads(response.text)

    # Extract the response
    answer = None
    for text in result["data"]["messages"]:
        if text["role"] == "assistant":
            answer = text["content"]
            break

    return answer

# Start the Streamlit application
st.title("Preguntas sobre las leyes de Guatemala")
st.write("Ingrese su pregunta:")
question = st.text_input("Pregunta")

# Answer the question
legal_information = get_legal_information(question)

# Display the result
if legal_information:
    st.success(legal_information)
else:
    st.warning("No se encontró información legal para la pregunta proporcionada.")
