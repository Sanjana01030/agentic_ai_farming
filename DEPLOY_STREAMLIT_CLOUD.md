# Deploy to Streamlit Community Cloud

## Quick Deployment Steps

1. **Go to** [share.streamlit.io](https://share.streamlit.io/)

2. **Sign in** with your GitHub account

3. **Click "New app"**

4. **Fill in the details:**
   - Repository: `Sanjana01030/agentic_ai_farming`
   - Branch: `main`
   - Main file path: `chatbot_app.py`

5. **Click "Deploy"**

That's it! Your app will be live in 2-3 minutes.

## Requirements

✅ Already done:
- `requirements.txt` is configured
- `runtime.txt` specifies Python version
- Repository is public on GitHub

## What Will Work

✅ Weather prediction
✅ Crop yield prediction (heuristic-based)
✅ Pest risk prediction (rule-based)
✅ Analytics dashboard
✅ UI and translations

⚠️ **Ollama chat will NOT work** (same limitation as Render)
- Ollama requires local server
- Consider using Streamlit secrets with OpenAI/Gemini API instead

ℹ️ **ML Models**: App uses fallback predictions since `.pkl` files are not in git.
- Predictions are still accurate using heuristic algorithms
- For ML-based predictions, train models locally with `python generate_models.py`

## App URL

Your app will be accessible at:
```
https://[your-app-name].streamlit.app
```

## Free Tier Limits

- 1 GB RAM
- 1 CPU core
- Unlimited public apps
- Perfect for this farming assistant!
