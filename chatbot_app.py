import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import ollama

from agents.weather_agent import predict_weather
from agents.crop_agent import predict_yield, MODEL_AVAILABLE as CROP_MODEL_AVAILABLE
from agents.pest_agent import predict_pest_risk, MODEL_AVAILABLE as PEST_MODEL_AVAILABLE
from agents.llm_agent import ask_llm
from utils.translator import thanglish_to_tamil, tamil_to_english

st.set_page_config(page_title="AI Farming Assistant", layout="wide")

# ---------------- UI STYLE ----------------

st.markdown("""
<style>

.stApp{
background:#E8F7EE;
color:#083d2b;
}

html,body,p,span,label,h1,h2,h3,h4{
color:#083d2b !important;
}

/* sidebar pastel */

section[data-testid="stSidebar"]{
background:#F2FBF6;
}

/* inputs */

input,textarea{
background:#F6FFFB !important;
color:#083d2b !important;
}

/* number input */

div[data-baseweb="input"]{
background:#F6FFFB !important;
}

/* title */

.title{
text-align:center;
font-size:42px;
font-weight:700;
color:#083d2b;
}

/* crop field */

.field{
position:fixed;
bottom:0;
left:0;
width:100%;
height:110px;
background:linear-gradient(#8ED8B6,#5FBF9F);
}

.grass{
position:absolute;
bottom:15px;
width:100%;
text-align:center;
font-size:38px;
animation:sway 4s infinite ease-in-out;
}

@keyframes sway{
0%{transform:translateX(-6px)}
50%{transform:translateX(6px)}
100%{transform:translateX(-6px)}
}

</style>

<div class="field">
<div class="grass">🌾 🌾 🌾 🌾 🌾 🌾 🌾 🌾 🌾 🌾 🌾</div>
</div>

""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown('<div class="title">🌱 AI Farming Assistant</div>', unsafe_allow_html=True)

# Show model status warning if using fallback
if not CROP_MODEL_AVAILABLE or not PEST_MODEL_AVAILABLE:
    st.warning("⚠️ Running in fallback mode: ML models not found. Using heuristic predictions. For better accuracy, train and include model files.", icon="⚠️")

# ---------------- NAVIGATION ----------------

menu = st.radio(
"",
["Chat Assistant", "Analytics Dashboard", "Help / Support"],
horizontal=True
)

# ---------------- SIDEBAR FARM SETTINGS ----------------

st.sidebar.header("🌾 Farm Settings")



area = st.sidebar.number_input("Cultivation Area", value=1000)
fertilizer = st.sidebar.number_input("Fertilizer Usage", value=500)
pesticide = st.sidebar.number_input("Pesticide Usage", value=100)

N = st.sidebar.number_input("Nitrogen", value=70)
P = st.sidebar.number_input("Phosphorus", value=40)
K = st.sidebar.number_input("Potassium", value=30)

pH = st.sidebar.number_input("Soil pH", value=6.5)

city = st.sidebar.text_input("City", value = "Chennai")


# ---------------- ANALYTICS FUNCTIONS ----------------

def rainfall_chart(region):

    months=["Jan","Feb","Mar","Apr","May","Jun"]
    rainfall=[random.randint(20,120) for _ in months]

    df=pd.DataFrame({"Month":months,"Rainfall":rainfall})

    fig=plt.figure()

    plt.plot(df["Month"],df["Rainfall"])
    plt.title(f"Rainfall Trend in {region}")
    plt.xlabel("Month")
    plt.ylabel("Rainfall (mm)")

    return fig


def rainfall_heatmap(region):

    data=[[random.randint(10,120) for _ in range(7)] for _ in range(6)]

    fig=plt.figure()

    plt.imshow(data)
    plt.colorbar(label="Rainfall")
    plt.title(f"Rainfall Heatmap for {region}")

    return fig


def yield_chart(region):

    months=["Jan","Feb","Mar","Apr","May","Jun"]
    yield_data=[random.randint(200,500) for _ in months]

    df=pd.DataFrame({"Month":months,"Yield":yield_data})

    fig=plt.figure()

    plt.plot(df["Month"],df["Yield"])
    plt.title(f"Crop Yield Trend in {region}")
    plt.xlabel("Month")
    plt.ylabel("Yield")

    return fig

# ---------------- ANALYTICS ----------------

if menu=="Analytics Dashboard":

    st.header("Regional Analytics")

    region=st.text_input("Region",city)

    col1,col2=st.columns(2)

    with col1:
        st.subheader("Rainfall Trend")
        st.pyplot(rainfall_chart(region))

    with col2:
        st.subheader("Crop Yield Trend")
        st.pyplot(yield_chart(region))

    st.subheader("Rainfall Heatmap")
    st.pyplot(rainfall_heatmap(region))

# ---------------- CHAT ----------------

if menu=="Chat Assistant":

    query = st.text_input("Ask your farming question")

    if st.button("Ask AI"):

        try:

            tamil_text = thanglish_to_tamil(query)
            english_question = tamil_to_english(tamil_text)

            weather = predict_weather(city)

            if "weather" in english_question.lower() or "rain" in english_question.lower():

                response=f"""
Weather in {city}

Temperature: {weather['avg_temp']} °C  
Rainfall: {weather['total_rainfall_mm']} mm  
Humidity: {weather['avg_humidity_percent']} %
"""

            elif "yield" in english_question.lower():

                result=predict_yield(
                    area,
                    fertilizer,
                    pesticide,
                    weather["avg_temp"],
                    weather["total_rainfall_mm"],
                    weather["avg_humidity_percent"],
                    N,
                    P,
                    K,
                    pH
                )

                response=f"Estimated Crop Yield: {round(result,2)}"

            elif "pest" in english_question.lower():

                pest=predict_pest_risk(
                    weather["avg_temp"],
                    weather["avg_humidity_percent"]
                )

                response=f"Pest Risk Level: {pest}"

            else:

                response=ask_llm(english_question)

            st.write(response)

        except Exception as e:

            st.error(str(e))

# ---------------- HELP ----------------

if menu=="Help / Support":

    st.header("Help")

    st.write("Ask questions like:")

    st.write("Will it rain tomorrow")
    st.write("nalaiku mazhai varuma")
    st.write("predict rice yield")

    st.write("Support: support@aifarming.ai")