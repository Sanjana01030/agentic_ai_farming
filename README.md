# 🌱 AI Farming Assistant

An intelligent farming assistant powered by AI that helps farmers with weather predictions, crop yield forecasting, pest risk assessment, and farming advice.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55.0-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌾 Features

- **🌤️ Weather Predictions** - Get real-time weather data for your region
- **📊 Crop Yield Forecasting** - Predict crop yields based on soil and weather conditions
- **🐛 Pest Risk Assessment** - Evaluate pest risks based on environmental factors
- **📈 Analytics Dashboard** - Visualize rainfall trends and crop yield data
- **💬 Multilingual Support** - Supports English, Tamil, and Thanglish (Tamil in English script)
- **🤖 AI Chat Assistant** - Ask farming questions in natural language

## 🚀 Live Demo

Deploy your own instance in minutes:

### Option 1: Streamlit Community Cloud (Recommended)

1. Visit [share.streamlit.io](https://share.streamlit.io/)
2. Sign in with GitHub
3. Click "New app"
4. Configure:
   - Repository: `Sanjana01030/agentic_ai_farming`
   - Branch: `main`
   - Main file: `chatbot_app.py`
5. Click "Deploy"

Your app will be live at: `https://[your-app-name].streamlit.app`

### Option 2: Render

See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for detailed instructions.

## 📦 Installation

### Prerequisites

- Python 3.11+
- pip package manager

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/Sanjana01030/agentic_ai_farming.git
cd agentic_ai_farming
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run chatbot_app.py
```

Note: The app will work with fallback predictions. For ML-based predictions, optionally generate models:
```bash
python generate_models.py
```

5. **Open your browser**
```
http://localhost:8501
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, FastAPI
- **ML Models**: scikit-learn
- **AI/LLM**: Ollama (local), configurable for cloud APIs
- **Translation**: deep-translator, indic-transliteration
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib

## 📁 Project Structure

```
agentic_farming_ai/
├── agents/               # AI agent modules
│   ├── crop_agent.py    # Crop yield prediction
│   ├── weather_agent.py # Weather forecasting
│   ├── pest_agent.py    # Pest risk assessment
│   ├── llm_agent.py     # LLM integration
│   └── orchestrator.py  # Agent coordination
├── api/                  # FastAPI endpoints
│   └── main.py
├── data/                 # Datasets
│   ├── crops/
│   ├── weather/
│   └── yield/
├── ml/                   # ML model training scripts
│   ├── train_crop_model.py
│   ├── train_weather_model.py
│   └── train_pest_model.py
├── models/               # Trained model files
├── utils/                # Utility functions
│   └── translator.py
├── chatbot_app.py        # Main Streamlit app
├── requirements.txt      # Python dependencies
└── runtime.txt          # Python version specification
```

## 🎯 Usage Examples

### Weather Query
```
"What's the weather in Chennai?"
"nalaiku mazhai varuma?" (Will it rain tomorrow?)
```

### Crop Yield
```
"Predict rice yield"
"What will be my crop production?"
```

### Pest Risk
```
"Is there pest risk?"
"Check for pest problems"
```

## ⚙️ Configuration

### Farm Settings (Sidebar)

- **Cultivation Area**: Total land area
- **Fertilizer Usage**: Amount of fertilizer applied
- **Pesticide Usage**: Amount of pesticide applied
- **NPK Values**: Nitrogen, Phosphorus, Potassium levels
- **Soil pH**: Soil acidity/alkalinity
- **City**: Location for weather data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👥 Authors

- **Sanjana** - Initial work - [Sanjana01030](https://github.com/Sanjana01030)

## 🙏 Acknowledgments

- Agriculture datasets from public sources
- Streamlit community for excellent documentation
- Open source ML libraries

## 📞 Support

For support, email support@aifarming.ai or open an issue in the repository.

## ⚠️ Known Limitations

- **Ollama**: The LLM chat feature requires Ollama server running locally. For cloud deployment, consider using OpenAI, Google Gemini, or similar APIs.
- **ML Models**: The app uses fallback heuristic predictions when ML models are not available. Models are not included in the repository due to `.gitignore`. The app will work without them, but for better accuracy, run `python generate_models.py` locally to create them.

## 🔮 Future Enhancements

- [ ] Add more crop types
- [ ] Integrate satellite imagery analysis
- [ ] Real-time IoT sensor data integration
- [ ] Mobile app version
- [ ] Multi-region support
- [ ] Historical data comparison
- [ ] Farming calendar and reminders
