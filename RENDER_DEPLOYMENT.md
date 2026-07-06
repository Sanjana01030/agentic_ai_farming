# Render Deployment Instructions

## Configuration

### Build Command
```
pip install -r requirements.txt
```

### Start Command
```
streamlit run chatbot_app.py --server.port=$PORT --server.address=0.0.0.0
```

## Important Notes

⚠️ **Ollama Limitation**: This application uses Ollama for LLM functionality. Ollama requires a local server which is **not available on Render's web service**. 

### What Will Work
- Weather prediction ✅
- Crop yield prediction ✅
- Pest risk prediction ✅
- Analytics dashboard ✅
- UI and basic functionality ✅

### What Will NOT Work
- General chat questions that require LLM (will show error)

### Workaround Options

1. **Use external Ollama server**: Set up Ollama on a separate server and configure the connection
2. **Disable LLM feature**: Comment out the LLM section in the chat
3. **Switch to cloud API**: Replace Ollama with OpenAI, Gemini, or another cloud LLM API

## Environment Variables

No environment variables are required for the core functionality (weather, crop, pest predictions).

## Python Version

The deployment uses Python 3.11.9 as specified in `runtime.txt`.
