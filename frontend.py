"""
Entry point for Frontend
"""

import streamlit as st
import requests

from core.config import settings

st.title("Named Entity Recognition (NER) Predictor")
st.write("Enter a sentence, and the model will predict named entities.")

# User input
sentence = st.text_area("Enter a sentence:")

if st.button("Predict"):
    if sentence:
        try:
            response = requests.post(
                f"{settings.API_URL}/predict", params={"sentence": sentence}
            )
            if response.status_code == 200:
                result = response.json()
                tokens = result["data"]["tokens"]
                tags = result["data"]["tags"]

                # Display results
                st.subheader("Prediction Results")
                for token, tag in zip(tokens, tags):
                    st.write(f"**{token}**: `{tag}`")
            else:
                st.error("Error: Unable to get a response from the API.")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a sentence before predicting.")
