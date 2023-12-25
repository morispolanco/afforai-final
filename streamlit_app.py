import streamlit as st
import requests

# Define the API endpoint
api_endpoint = "https://datos.gob.gt/api/3/action/datastore_search"

# Set the resource ID
resource_id = "leyes_publicadas"

# Inicia la aplicación Streamlit
st.title("Responder preguntas sobre las leyes de Guatemala")
st.write("Ingrese su pregunta:")
question = st.text_input("Pregunta")

# Procesa la pregunta
processed_question = question.replace(" ", "+")

# Define la función para obtener la respuesta a la pregunta
def get_answer(question):
    # Set the query parameters
    query_params = {
        "resource_id": resource_id,
        "q": question,
    }

    # Make the API request
    response = requests.get(api_endpoint, params=query_params)

    # Get the JSON response
    json_response = response.json()

    # Busca la respuesta a la pregunta
    answer = None
    for result in json_response["result"]["records"]:
        if result["titulo"].lower().find(question.lower()) != -1:
            answer = result["contenido"]
            break

    return answer

# Obtiene la respuesta a la pregunta
answer = get_answer(processed_question)

# Muestra el resultado
if answer:
    st.success(answer)
else:
    st.error("Lo siento, no puedo responder a esa pregunta.")
