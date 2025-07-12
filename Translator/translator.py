import streamlit as st
import json, requests, sys

f=open("languages.json")
data=json.load(f)


st.title("🔁 Translator")

from_language=st.selectbox("From Language", data.keys())

translate_inp=st.text_input("Text to translate: ", "Type here ...")

to_language=st.selectbox("To Language", data.keys())
st.session_state.text="See here ..."

def translate_text(source_lang, target_lang, text):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": source_lang,
        "tl": target_lang,
        "dt": "t",
        "q": text
    }
    response = requests.get(url, params=params)
    if response.status_code==200:
        return response.json()[0][0][0]
    else:
        st.error("An error occured!")
if translate_inp.title():
    st.session_state.text=translate_text(data[from_language], data[to_language], translate_inp.title())
    translation=st.text_input("Translated text: ", st.session_state.text)