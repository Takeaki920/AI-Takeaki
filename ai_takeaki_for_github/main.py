import streamlit as st
from query import ask_ai

st.set_page_config(page_title="AIたけあき", layout="centered")

# デザイン適用
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://raw.githubusercontent.com/Takeaki920/AI-Takeaki/main/ai_takeaki_for_github/assets/bg.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem 2rem 1rem 2rem;
        border-radius: 1.25rem;
        box-shadow: 0 0 15px rgba(0,0,0,0.2);
        max-width: 700px;
        margin: auto;
    }}
    .title-box {{
        text-align: center;
        margin-bottom: 1rem;
    }}
    .title-box img {{
        border-radius: 50%;
        width: 100px;
        height: 100px;
        margin-bottom: 0.5rem;
    }}
    .title-box h1 {{
        font-size: 2.5rem;
        color: #333;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-box">
        <img src="https://raw.githubusercontent.com/Takeaki920/AI-Takeaki/main/ai_takeaki_for_github/assets/icon.png">
        <h1>AIたけあき</h1>
    </div>
    """,
    unsafe_allow_html=True
)

query = st.text_input("質問をどうぞ", placeholder="例：明るい未来のためにどうしたらいい？")

if query:
    with st.spinner("考え中..."):
        response = ask_ai(query)
    st.markdown("### 回答")
    st.markdown(f"> {response}")
