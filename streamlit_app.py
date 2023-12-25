import streamlit as st
import requests
import json

# Replace with your own API key and session ID
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

def ask_question(question):
    url = "https://api.afforai.com/api/api_completion"
    data = {
        "apiKey": api_key,
        "sessionID": session_id,
        "history": [{"role": "user", "content": question}],
        "powerful": False,
        "google": True
    }
    response = requests.post(url, json=data)
    response_data = response.json()
    answer = response_data["completions"][0]["content"]
    return answer

st.title("Preguntas sobre las leyes de Guatemala")

question = st.text_input("Introduce tu pregunta aquí:")
if question:
    answer = ask_question(question)
    st.write("Respuesta:")
    st.write(answer)
