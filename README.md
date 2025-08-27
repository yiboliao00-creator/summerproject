# Streamlit Deployment Pack

This folder is ready to push to GitHub and deploy on **Streamlit Community Cloud**.
Your main app file is `ivey_synthetic_data_app.py`.

## Deploy on Streamlit Cloud (easiest)
1. Push this folder to GitHub (as a new repo).
2. Go to https://share.streamlit.io → **New app**.
3. Select your repo, branch `main`, **Main file path** = `ivey_synthetic_data_app.py`.
4. Deploy. Any future `git push` auto-redeploys.

## Optional: Deploy on Google Cloud Run (faster, autoscaling)
1. Install Google Cloud SDK and run `gcloud auth login`.
2. From this folder:
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/ivey-synth-app
   gcloud run deploy ivey-synth-app      --image gcr.io/YOUR_PROJECT_ID/ivey-synth-app      --platform managed --region YOUR_REGION --allow-unauthenticated      --memory 2Gi --cpu 2 --concurrency 20 --min-instances 0 --max-instances 50
   ```

## Notes
- If the app logs show `ModuleNotFoundError`, add that package to `requirements.txt`, commit & push.
- The "AI Education Assistant" tab relies on a local Ollama model. On cloud, it will show the setup message.
- Keep large datasets **out** of the repo; load from cloud storage and cache in the app.
