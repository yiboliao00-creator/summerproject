# Groq Free Chatbot Kit

Use a **completely free** LLM (Groq free tier) with your Streamlit app.

## Steps
1) Replace your project's `requirements.txt` with the one in this folder (or add the four lines at the bottom).
   - Adds: `langchain-groq` and `groq`.
2) In Streamlit Cloud → Manage app → **Settings → Secrets**, add:
   ```toml
   GROQ_API_KEY = "grq_..."
   ```
3) Copy the code from `ai_chat_patch_snippet.py` into your app where the chatbot runs.
   - It will use Groq if the key is present; otherwise it shows a helpful warning.
4) Push to GitHub. Streamlit will redeploy automatically.

## Notes
- This avoids `localhost:11434` (Ollama). No local server needed on Streamlit Cloud.
- The model used is `llama-3.1-8b-instant` via Groq. It's fast and suitable for coursework.
- Keep prompts short to stay within free-tier limits.
