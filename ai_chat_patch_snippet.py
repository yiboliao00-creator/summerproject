# ai_chat_patch_snippet.py
# Drop this in your repo or copy-paste into your Streamlit app's chatbot section.

import os, streamlit as st
from langchain_core.prompts import ChatPromptTemplate

# Prefer Groq (free tier) if key is present; otherwise show a friendly warning.
try:
    from langchain_groq import ChatGroq
    _groq_import_ok = True
except Exception:
    _groq_import_ok = False

def make_llm():
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if _groq_import_ok and api_key:
        # Small, fast, and good enough for coursework demos.
        return ChatGroq(model_name="llama-3.1-8b-instant",
                        api_key=api_key,
                        temperature=0.2,
                        max_tokens=512)
    st.warning("No free LLM configured. Add GROQ_API_KEY in Settings → Secrets on Streamlit Cloud.")
    return None

def ask_ai(user_question: str):
    system = (
        "You are a concise teaching assistant for synthetic data. "
        "Explain clearly, with short examples when helpful."
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", "{question}")
    ])
    llm = make_llm()
    if not llm:
        return None
    chain = prompt | llm
    result = chain.invoke({"question": user_question})
    return getattr(result, "content", str(result))

# Example Streamlit UI wiring:
# st.header("AI Education Assistant (Free via Groq)")
# q = st.text_input("Ask me anything about synthetic data...")
# if q:
#     ans = ask_ai(q)
#     if ans:
#         st.write(ans)
