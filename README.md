# Patched Streamlit App (cloud-friendly LLM)

- Prefers hosted LLMs (OpenAI or Groq) when keys are present.
- Falls back to local Ollama only if reachable (for local development).
- Avoids connection errors on Streamlit Cloud.

## Configure a hosted LLM (Streamlit Cloud)
In the app → **Manage app → Secrets**, add **one** of the following:

### OpenAI
```
OPENAI_API_KEY="sk-..."
```

### Groq
```
GROQ_API_KEY="..."
```

Redeploys happen automatically on `git push`.

## Local Ollama (optional)
Run `ollama serve` and pull a model (e.g., `ollama pull phi3:mini`). The app will auto-detect `http://localhost:11434`.

