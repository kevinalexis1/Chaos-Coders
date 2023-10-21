
import pandas as pd
from sklearn.model_selection import train_test_split
import sys
import numpy as np
from hmmlearn import hmm
import itertools
#from tqdm import tqdm
import matplotlib.pyplot as plt


# Ruta al archivo CSV
csv_path = "/home/mazroj/Chaos-Coders/coffee.csv"  # Reemplaza con la ruta a tu archivo CSV
test_size = 0.3  # Porcentaje de datos para el conjunto de prueba

try:
    # Usa pandas para leer el archivo CSV
    used_data = pd.read_csv(csv_path)
except FileNotFoundError:
    print("Archivo CSV no encontrado. Por favor, verifica la ruta del archivo.")
    sys.exit()

def predictor(used_data, test_size, n_components ):
    # No mezcles los datos ya que es una serie temporal
    _train_data, test_data = train_test_split(used_data, test_size=test_size, shuffle=False)

    # Elimina las columnas que no se usan
    train_data = _train_data.drop(["Volume", "Adj Close"], axis=1)  # Ajusta los nombres de las columnas según tu dataset
    test_data = test_data.drop(["Volume", "Adj Close"], axis=1)  # Ajusta los nombres de las columnas según tu dataset

    # Establece el atributo days
    days = len(test_data)

    # Extrae las características: precios de apertura, cierre, máximo y mínimo
    open_price = np.array(train_data["Open"])
    close_price = np.array(train_data["Close"])
    high_price = np.array(train_data["High"])
    low_price = np.array(train_data["Low"])

    # Calcula los cambios fraccionales en los precios alto, bajo y de cierre para usar como conjunto de observaciones
    frac_change = (close_price - open_price) / open_price
    frac_high = (high_price - open_price) / open_price
    frac_low = (open_price - low_price) / open_price

    # Apila las características en columnas
    features = np.column_stack((frac_change, frac_high, frac_low))

    # Inicializa el modelo HMM
    #n_components = 3  # Número de estados en el modelo, ajusta según tus necesidades
    hmm_1 = hmm.GMMHMM(n_components=n_components)

    # Registro de la extracción de características
    #_logger.info(">>> Extracting Features"3
    observations = features  # Usa las características que has calculado
    #_logger.info("Features extraction Completed <<<")

    # Ajusta el modelo HMM usando la función 'fit' de hmmlearn
    hmm_1.fit(observations)

    # Parámetros para los intervalos
    n_intervals_frac_change = 15  # Ajusta según tus necesidades
    n_intervals_frac_high = 15  # Ajusta según tus necesidades
    n_intervals_frac_low = 15  # Ajusta según tus necesidades

    # Crea arrays de NumPy con números espaciados uniformemente para cada rango
    frac_change_range = np.linspace(-0.1, 0.1, n_intervals_frac_change)
    frac_high_range = np.linspace(0, 0.1, n_intervals_frac_high)
    frac_low_range = np.linspace(0, 0.1, n_intervals_frac_low)

    # Calcula todos los resultados posibles utilizando el producto cartesiano
    possible_outcomes = np.array(
        list(itertools.product(frac_change_range, frac_high_range, frac_low_range))
    )

    # Parámetros
    day_index = 20  # Índice del día actual, ajusta según tus necesidades
    n_latency_days = 2  # Número de días de latencia, ajusta según tus necesidades

    # Usa los datos anteriores de n_latency_days para las predicciones
    previous_data_start_index = max(0, day_index - n_latency_days)
    previous_data_end_index = max(0, day_index - 1)
    previous_data = test_data.iloc[previous_data_start_index:previous_data_end_index]

    # Supongamos que 'features' son las características extraídas
    # features = np.column_stack((frac_change, frac_high, frac_low))  # Descomenta esta línea si necesitas calcular las características
    previous_data_features = features  # Usa las características que has calculado

    outcome_score = []

    # Evalúa todos los resultados posibles y selecciona el más probable para usar en la predicción
    for possible_outcome in possible_outcomes:
        total_data = np.row_stack((previous_data_features, possible_outcome))
        outcome_score.append(hmm_1.score(total_data))

    # Obtén el índice del resultado más probable y devuélvelo
    most_probable_outcome = possible_outcomes[np.argmax(outcome_score)]

    # Parámetros
    day_index_1 = len(test_data)-1 # Índice del día para el que quieres hacer la predicción, ajusta según tus necesidades

    # Obtén el precio de apertura para el día dado
    open_price = test_data.iloc[day_index_1]["Open"]

    # Supongamos que 'most_probable_outcome' contiene los cambios fraccionales más probables en [frac_change, frac_high, frac_low]
    predicted_frac_change, pred_frac_high, pred_frac_low = most_probable_outcome

    # Calcula el precio de cierre previsto
    predicted_close_price = open_price * (1 + predicted_frac_change)

    #print(predicted_close_price)

    # Obtén la fecha correspondiente al day_index
    date_at_day_index = test_data.iloc[day_index_1]['Date']  # Reemplaza 'Fecha' con el nombre de tu columna de fechas
    #print(date_at_day_index)

    return predicted_close_price

n_components = 3
predictor(used_data, test_size, n_components)