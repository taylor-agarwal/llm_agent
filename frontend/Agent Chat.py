import requests
import streamlit as st


st.write("Agent Chat")

prompt = st.text_input("Prompt:")

if st.button("Ask"):
    with st.spinner("Generating response..."):
        response = requests.post("http://127.0.0.1:8000/v1/invoke", json={"prompt": prompt})
        if response.status_code != 200:
            st.error(f"Request failed with status code {response.status_code}")
            print(response.content)
            st.stop()
        response = response.json()['response']
    st.write(response)