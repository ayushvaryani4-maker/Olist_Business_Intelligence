import streamlit as st
from google import genai


def ask_gemini(prompt):

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return interaction.output_text