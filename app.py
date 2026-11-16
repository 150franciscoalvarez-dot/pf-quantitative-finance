import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

#descargar precios desde yahoo finance
tickers = ["IVV", "ILF", "SOXX"]# SP500, LATAM, SEMICONDUTORES
vector_W = [0.5, 0.3, 0.2]
vector_W = np.array(vector_W).reshape(-1,1)
#========
#APP
#========
st.title("Calculadora Riesgo De Mercado")
#descarga de datos
st.multiselect(label= "tickers", options=["IVV", "ILF", "SOXX"],key="tickers", default="SOXX")
tickers = st.session_state["tickers"]
#seleccionar pesos
st.multiselect(label= "Pesos", options=[0.5,0.3,0.2],key="pesos")
vector_W = st.session_state["pesos"]
vector_W = np.array(vector_W).reshape(-1,1)


#descargar desde yaho finanzas
if len(tickers) > 0:
    df_price = yf.download(tickers, start ="2024-01-01", end="2026-09-30")["Close"]
    df_price = df_price[tickers]
    st.dataframe(df_price)
    df_ret = df_price.pct_change().dropna()
#matriz de varianza covarizanza
df_cov = df_ret.cov()
#calcular la varianza del portafolio
w = vector_W
w_t = w.T
sigma = df_cov.values
varianza = np.dot(sigma, w)
varianza = np.dot(w_t, varianza)[0][0]
desv = varianza**(1/2)
volatilidad_anual = desv*(252**(1/2))#anualizacion
reporte_volatilidad = f"La volatilidad anual del portafolio: {volatilidad_anual*100:.04}%"
st.write(reporte_volatilidad)


