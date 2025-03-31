# NVDA hlutabréfa tracker + einfalt AI app

import streamlit as st
import yfinance as yf
from datetime import date, timedelta

# --- Titill og dagssetningar ---
st.title("📈 NVIDIA (NVDA) hlutabréf - einfalt yfirlit")

today = date.today()
start = today - timedelta(days=30)

# --- Sækja gögn frá Yahoo Finance ---
data = yf.download("NVDA", start=start, end=today)

# --- Sýna graf ---
st.subheader("Verð síðustu 30 daga")
st.line_chart(data['Close'])

# --- Sýna núverandi verð og breytingu ---
current = data['Close'][-1]
previous = data['Close'][-2]
change = current - previous
percent = (change / previous) * 100

st.metric("Lokaði verð (síðasti dagur)", f"${current:.2f}", f"{percent:.2f}%")

# --- Einföld AI textaúskýring ---
if change > 0:
    ai_text = "AI segir: Verðið hefur hækkað - mögulega út af aukinni bjartsýni í AI markaði."
elif change < 0:
    ai_text = "AI segir: Verðið hefur lækkað - mögulega vegna efnahagsfrétta eða tölvuiðnaðar."
else:
    ai_text = "AI segir: Engin breyting - markarðurinn stabiill."

st.info(ai_text)

st.caption("Byggt af Bjarka & ChatGPT")
