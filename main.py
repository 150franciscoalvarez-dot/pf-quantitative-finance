
import pandas as pd
import numpy as np
import yfinance as yf

#descargar precios desde yahoo finance
tickers = ["IVV", "ILF", "SOXX"]# SP500, LATAM, SEMICONDUTORES
vector_W = [0.5, 0.3, 0.2]
vector_W = np.array(vector_W).reshape(-1,1)# vector de pesos
df_price = yf.download(tickers,start ="2024-01-01", end="2026-09-30")["Close"]
print(df_price)
#calcular retornos diarios
df_ret = df_price.pct_change().dropna()
print(df_ret)
#matriz de varianza covarizanza
df_cov = df_ret.cov()
#calcular la varianza del portafolio
w = vector_W
w_t = w.T
sigma = df_cov.values
print("W", w.shape)
print("w_t", w_t.shape)
print("Sigma", sigma.shape)
varianza = np.dot(sigma, w)
varianza = np.dot(w_t, varianza)
varianza = varianza[0][0]
print(varianza)
#calcular desviacion estandar
desv = varianza**(1/2)
volatilidad_anual = desv*(252**(1/2))
print(desv)
print(f"La volatilidad del portafolio es: {volatilidad_anual*100:.04}%")
#calcular la media del portafolio
vector_ret = df_ret.mean()
vector_ret = vector_ret.values
vector_ret = vector_ret.reshape(-1,1)
print(vector_ret.shape)
mu = np.dot(w_t , vector_ret )[0][0]
mu_anual = mu * 252
print(f"La media anual del portafolio: {mu_anual*100:04}%")

#calcular value at risk (Var) al 95% de confianza
var_95 = mu_anual- 1.64*volatilidad_anual

print(f"La media anual del portafolio: {var_95*100:04}%")

