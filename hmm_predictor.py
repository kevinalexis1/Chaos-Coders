import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import itertools
import yfinance as yf

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from hmmlearn import hmm
from tqdm import tqdm
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

def get_weekly_data():
    # Descargar los datos de yahoo hasta la fecha actual con intervalo semanal
    data = yf.download('KC=F', start='2016-01-10', end=datetime.now().strftime('%Y-%m-%d'), interval='1wk')
    data.reset_index(inplace=True)

    return data

# Leer los datos
weekly_data = get_weekly_data()

# Definir el tamaño de la prueba
test_size = 0.3

# Dividir la data en train y test
train_data, test_data = train_test_split(weekly_data, test_size=test_size, shuffle=False)

# Eliminar valores NaN
train_data.dropna(inplace=True)
test_data.dropna(inplace=True)

# Parametros
n_components = 3
n_latency_days = 5
n_intervals = 15
days = len(test_data)

# Extraer las características: precios de apertura, cierre, máximo y mínimo
open_price = np.array(train_data["Open"])
close_price = np.array(train_data["Close"])
high_price = np.array(train_data["High"])
low_price = np.array(train_data["Low"])

# Calcular los cambios fraccionales en los precios alto, bajo y de cierre para usar como conjunto de observaciones
frac_change = (close_price - open_price) / open_price
frac_high = (high_price - open_price) / open_price
frac_low = (open_price - low_price) / open_price

# Apilar las características en columnas
features = np.column_stack((frac_change, frac_high, frac_low))

# Inicializar el modelo HMM
hmm_1 = hmm.GMMHMM(n_components)

# Registro de la extracción de características
observations = features

# Ajustar el modelo HMM
hmm_1.fit(observations)

# Crear arrays de NumPy con números espaciados uniformemente para cada rango
frac_change_range = np.linspace(-0.1, 0.1, n_intervals)
frac_high_range = np.linspace(0, 0.1, n_intervals)
frac_low_range = np.linspace(0, 0.1, n_intervals)

# Calcular todos los resultados posibles utilizando el producto cartesiano
possible_outcomes = np.array(
list(itertools.product(frac_change_range, frac_high_range, frac_low_range))
)

outcome_score = []

# Evalúar todos los resultados posibles y seleccionar el más probable
for possible_outcome in possible_outcomes:
    total_data = np.row_stack((features, possible_outcome))
    outcome_score.append(hmm_1.score(total_data))

# Precios de cierre históricos
historical_close_prices = used_data['Close']

# Calcular los cambios fraccionales en los precios de cierre
frac_changes = [(historical_close_prices[i] - historical_close_prices[i-1]) / historical_close_prices[i-1] for i in range(1, len(historical_close_prices))]

# Calcular el promedio y la desviación estándar de los cambios fraacionales
avg_frac_change = np.mean(frac_changes)
std_frac_change = np.std(frac_changes)

# Definir los umbrales de compra y venta basados en el análisis histórico
buy_threshold = avg_frac_change + std_frac_change
sell_threshold = avg_frac_change - std_frac_change

def predict_next_day():
    
    # Usar los días de latencia de la prueba para la predicción
    last_days_data = test_data.iloc[-n_latency_days:]

    most_probable_outcome = possible_outcomes[np.argmax(outcome_score)]

    last_open_price = last_days_data.iloc[-1]["Open"]
    predicted_frac_change, _, _ = most_probable_outcome
    predicted_close_price = last_open_price * (1 + predicted_frac_change)

    # Calcular el cambio fraccional para el siguiente día
    predicted_frac_change = (next_day_predicted_price - test_data['Close'].iloc[-1]) / test_data['Close'].iloc[-1]

    # Definir la señal
    if predicted_frac_change > buy_threshold:
        trade_signal = 'Compra'
    elif predicted_frac_change < sell_threshold:
        trade_signal = 'Venta'
    else:
        trade_signal = 'Retención'

    return predicted_close_price, trade_signal

app = Flask(_name_)
CORS(app)

@app.route('/predict', methods=['GET'])
def predict():
    
    valor_predecido, etiqueta_compra = predict_next_day()

    return jsonify({
        'predicted_value': valor_predecido,
        'action_label': etiqueta_compra,
        'actual_close_prices': actual_close_prices
    })

if _name_ == '_main_':
    app.run(port=5000)


