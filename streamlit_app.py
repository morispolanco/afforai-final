import streamlit as st

# Use the OpenAI API to generate responses
def generate_response(prompt):
  """Generates a response using the OpenAI API."""

  # Set the API key
  api_key = "AIzaSyAD9U7fg3QJGz0eT25PqvH-dKOHOefC2cI"

  # Set the API endpoint
  api_endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText?key=" + api_key

  # Set the request body
  request_body = {
    "requests": [
      {
        "generateTextRequest": {
          "prompt": {
            "text": prompt,
          },
          "max_characters": 2000,
        }
      }
    ]
  }

  # Send the request
  response = requests.post(api_endpoint, json=request_body)

  # Extract the response text
  response_text = response.json()["candidates"][0]["output"]

  # Return the response text
  return response_text

# Create a Streamlit app
st.title("Guatemala Law FAQs")
st.markdown("Ask me anything about the laws of Guatemala and I will try to answer.")

# Get the user's question
question = st.text_input("Ask me a question")

# If the user has entered a question, generate a response
if question:
  response = generate_response(question)
  st.write(response)
