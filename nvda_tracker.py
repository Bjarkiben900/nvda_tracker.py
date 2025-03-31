import streamlit as st
import yfinance as yf
import datetime
import openai

# --- STILLINGAR ---
st.set_page_config(page_title="NVIDIA Hlutabréfa Tracker", layout="centered")

# --- TITILL ---
st.title("📈 NVIDIA Hlutabréfa Tracker + AI Greining")

# --- DAGSETNINGAR FYRIR GRAF ---
end = datetime.date.today()
start = end - datetime.timedelta(days=30)

# --- HLUTABRÉFA GÖGN ---
ticker = "NVDA"
data = yf.download(ticker, start=start, end=end)

# --- GRAF ---
st.subheader("Verðsúga síðustu 30 daga")
st.line_chart(data['Close'])

# --- NÚVERANDI VERÐ ---
latest_price = data['Close'][-1]
previous_price = data['Close'][-2]
change = latest_price - previous_price
percent = (change / previous_price) * 100

st.metric(label="NVIDIA Lokaði (lokadagur)", value=f"${latest_price:.2f}", delta=f"{change:.2f} ({percent:.2f}%)")

# --- AI GREINING (SIMPLIFIED MOCKUP) ---
def get_ai_explanation(price_change):
    if price_change > 2:
        return "Verðið hækkaði mögulega út af bjartsýni um AI markaðinn og auknum fjárfestingum í tölvubúnaði."
    elif price_change < -2:
        return "Verðið lækkaði líklega vegna neikvæðra efnahagsfrétta íað vön um minni AI-vöxt."
    else:
        return "Engin stór verðbreyting - markarðurinn er stabiill um NVIDIA um þessar mundir."

# --- AI SPÁ (mockup) ---
def get_ai_prediction():
    return "AI spáir að næstu vikur gætu séð aukningu í verði vegna NVIDIA framleiðslufunda og AI-tengdra ráðstefna."

st.subheader("🧠 AI Skýring")
st.info(get_ai_explanation(change))

st.subheader("🤔 AI Kúup-ráðgjöf")
st.success(get_ai_prediction())

st.caption("Byggt af Bjarkiben900 x ChatGPT")
