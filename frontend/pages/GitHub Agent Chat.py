import requests
import streamlit as st


st.write("GitHub Agent Chat")

prompt = st.text_input("Prompt:")

if st.button("Ask"):
    with st.spinner("Generating response..."):
        json = dict(
            prompt=prompt,
        )
        response = requests.post("http://127.0.0.1:8000/v1/github_agent", json=json, timeout=None)
        if response.status_code != 200:
            st.error(f"Request failed with status code {response.status_code}")
            print(response.content)
            st.stop()
        response = response.json()['response']
    st.write(response)