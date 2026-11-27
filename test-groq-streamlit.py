import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")
api_key = os.getenv("api_key_groq")

client = Groq(api_key=os.environ["api_key_groq"])

question = st.text_input("Ask a question about the Groq API:")
if st.button("Submit"):
    rep = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
    )
    st.write(rep.choices[0].message.content)
        
