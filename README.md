# Chaos-Coders

Este repositorio esta hecho en el contexte del Hackaton Co-Afina 2023 organizado por La-Conga Physics (https://laconga.redclara.net). Durante el evento se presentaron varios retos, de los cuales se selecciono: #reto-1-pronosticando-el-mercado. 
Para este reto se busco diseñar modelos que permitan predecir el comportamiento del mercado financiero. Esto se lo hizo con ayuda de modelos de machine learning como el Hidden Markov Model (HMM) que usando matrizes de probabilidades y la definicion de estados ocultos, permite reconocer patrones en los datos propuestos atravez de un un aprendizaje no supervisado. Atravez del cual es posible obtener señales de compra y venta de los activos. La informacion relacionada con este modelo puede ser encontrada en Implementing Machine Learning for Finance, de TC Nokeri, que puede encontrarse en https://link.springer.com/book/10.1007/978-1-4842-7110-0.

Para este reto se usaron datos del mercado de futuros de Café (KC=F), que pueden ser encontrados en https://finance.yahoo.com/quote/KC%3DF/history?period1=946857600&period2=1697760000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true, estos datos fueron obtenidos con una frecuencia semanal.
El resultado de estas señales es simulado con los datos del mercado, de manera que nos permiten medir su rendimiento posible. Luego estos resultados son comparados con una técnica básica de negociación de productos financieros, que consiste en la compra y retención de estos, comunmente conocida como holding. 

Ademas se presenta la posibilidad de mejorar los modelos, incluyendo información de diferentes mercados relacionados directamente al ir y venir de la política mundial.

# Archivos

'book_test_markov.ipynb'
Este cuaderno Jupyter sirve como un ejemplo práctico para explorar las capacidades del paquete hmmlearn en el análisis de datos de precios y volúmenes de café. Utiliza un modelo de Markov oculto para visualizar y entender las tendencias en los precios y volúmenes de café.

'hmm_predictor.ipynb'
Este cuaderno Jupyter utiliza un Modelo Oculto de Markov (HMM) para predecir los precios de cierre del café. El modelo se entrena con datos históricos que incluyen precios de apertura, cierre, máximos y mínimos. Además, el cuaderno genera señales de compra, venta o retención basadas en el análisis de cambios fraccionales en los precios. El objetivo es proporcionar una herramienta de pronóstico de precios y una estrategia de trading para el mercado del café.

'correlations_cafe.ipynb'
Este cuaderno Jupyter se centra en analizar las correlaciones entre los precios del café, el petróleo WTI y el índice S&P 500. Utiliza pandas para la manipulación de datos y Seaborn para la visualización. El cuaderno carga datos históricos de estos tres activos, los combina en un solo DataFrame y luego calcula y visualiza la matriz de correlación. El objetivo es entender cómo estos mercados están interconectados y cómo los cambios en uno podrían afectar a los otros.

'hmm_predictor.py'
Este módulo Python encapsula las funcionalidades clave del cuaderno Jupyter hmm_predictor.ipynb para facilitar su importación y uso en otros proyectos, como para la página web. El módulo utiliza el modelo de mezcla de Markov oculto (HMM) para predecir los precios de cierre del café. Incluye funciones para la preparación de datos, entrenamiento del modelo HMM, y generación de señales de trading ('Compra', 'Venta', 'Retención') basadas en los precios previstos. El objetivo es proporcionar una forma eficiente y automatizada de obtener predicciones y señales de trading para el mercado del café.

