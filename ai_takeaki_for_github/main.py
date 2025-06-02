
import streamlit as st
from query import ask_ai

st.set_page_config(page_title="AIたけあき", layout="centered")
st.title("🤖 AIたけあき")
st.caption("あなたの分身として、過去の文章をもとに応答します。")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role, text = message
    with st.chat_message(role):
        st.markdown(text)

query = st.chat_input("質問を入力してください")
if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append(("user", query))

    with st.chat_message("assistant"):
        response = ask_ai(query)
        st.markdown(response)
    st.session_state.messages.append(("assistant", response))
