import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage, AIMessage
import uuid

# Utility function to generate unique thread IDs
def generate_thread_id():
    return str(uuid.uuid4())


def extract_text(message):
    content = getattr(message, "content", "")

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                text = item.get("text")
                if text:
                    parts.append(text)
        return "\n".join(parts).strip()

    return str(content).strip()


# ---------------- SESSION STATE ----------------
if "message_history" not in st.session_state:
    st.session_state.message_history = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = generate_thread_id()


# ---------------- SIDEBAR ----------------
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    st.session_state.message_history = []
    st.session_state.thread_id = generate_thread_id()
    st.rerun()

st.sidebar.header("Thread ID")
st.sidebar.text(st.session_state.thread_id)


# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.message_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---------------- INPUT ----------------
user_input = st.chat_input("Type your message here...")

if user_input:
    # Save user message
    st.session_state.message_history.append(
        {"role": "user", "content": user_input}
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    CONFIG = {"configurable": {"thread_id": st.session_state.thread_id}}

    # ---------------- ASSISTANT RESPONSE ----------------
    with st.chat_message("assistant"):
        placeholder = st.empty()
        response_text = ""

        try:
            result = chatbot.invoke(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
            )

            for message in reversed(result.get("messages", [])):
                if isinstance(message, AIMessage):
                    response_text = extract_text(message)
                    break

            if response_text:
                placeholder.markdown(response_text)
                st.session_state.message_history.append(
                    {"role": "assistant", "content": response_text}
                )
            else:
                error_text = (
                    "No assistant response was returned. Check your OpenAI API key "
                    "and backend configuration."
                )
                placeholder.error(error_text)
                st.session_state.message_history.append(
                    {"role": "assistant", "content": error_text}
                )
        except Exception as exc:
            error_text = f"Backend error: {exc}"
            placeholder.error(error_text)
            st.session_state.message_history.append(
                {"role": "assistant", "content": error_text}
            )
