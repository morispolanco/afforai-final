import streamlit as st
import requests
import json

# Load Afforai API credentials
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Define the function to answer questions about the laws of Guatemala
def get_legal_information(question):
    # Construct the query for the Afforai API
    query = f"leyes guatemala {question}"

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
st.title("Questions about the laws of Guatemala")
st.write("Enter your question:")
question = st.text_input("Question")

# Answer the question
legal_information = get_legal_information(question)

# Display the result
if legal_information:
    st.success(legal_information)
else:
    st.warning("No legal information found for the provided question.")
