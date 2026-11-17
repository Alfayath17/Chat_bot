import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-3.5-flash"


@st.cache_resource
def get_client():
    return genai.Client()


# Conversation memory lives in session_state so it survives Streamlit reruns
if "conversation" not in st.session_state:
    st.session_state.conversation = []


def chat(user_message):
    conversation = st.session_state.conversation
    conversation.append({"role": "user", "parts": [{"text": user_message}]})

    try:
        response = get_client().models.generate_content(
            model=MODEL,
            contents=conversation,
        )
        reply = response.text
    except Exception as e:
        conversation.pop()  # drop the failed user turn so history stays valid
        return f"Sorry, something went wrong: {e}"

    conversation.append({"role": "model", "parts": [{"text": reply}]})
    return reply


st.set_page_config(page_title="Chatbot with Memory", page_icon="💬")
st.title("💬 Chatbot with Memory")
st.caption(f"Powered by Google Gemini ({MODEL}) — it remembers everything you say in this session.")

with st.sidebar:
    st.header("Conversation")
    st.write(f"Messages: {len(st.session_state.conversation)}")
    if st.button("Clear chat"):
        st.session_state.conversation = []
        st.rerun()

# Show the history
for message in st.session_state.conversation:
    role = "assistant" if message["role"] == "model" else "user"
    with st.chat_message(role):
        st.markdown(message["parts"][0]["text"])

# New input
if user_message := st.chat_input("Type your message..."):
    with st.chat_message("user"):
        st.markdown(user_message)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = chat(user_message)
        st.markdown(reply)
