# Youtube video
Video de presentación del proyecto: https://youtu.be/5fAKsmOL_Ls

# Chaos-Coders

Este repositorio esta hecho en el contexte del Hackaton Co-Afina 2023 organizado por La-Conga Physics (https://laconga.redclara.net). Durante el evento se presentaron varios retos, de los cuales se selecciono: #reto-1-pronosticando-el-mercado. 
Para este reto se busco diseñar modelos que permitan predecir el comportamiento del mercado financiero. Esto se lo hizo con ayuda de modelos de machine learning como el Hidden Markov Model (HMM) que usando matrizes de probabilidades y la definicion de estados ocultos, permite reconocer patrones en los datos propuestos atravez de un un aprendizaje no supervisado. Atravez del cual es posible obtener señales de compra y venta de los activos. La informacion relacionada con este modelo puede ser encontrada en Implementing Machine Learning for Finance, de TC Nokeri, que puede encontrarse en https://link.springer.com/book/10.1007/978-1-4842-7110-0.

Para este reto se usaron datos del mercado de futuros de Café (KC=F), que pueden ser encontrados en https://finance.yahoo.com/quote/KC%3DF/history?period1=946857600&period2=1697760000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true, estos datos fueron obtenidos con una frecuencia semanal.
El resultado de estas señales es simulado con los datos del mercado, de manera que nos permiten medir su rendimiento posible. Luego estos resultados son comparados con una técnica básica de negociación de productos financieros, que consiste en la compra y retención de estos, comunmente conocida como holding. 

Ademas se presenta la posibilidad de mejorar los modelos, incluyendo información de diferentes mercados relacionados directamente al ir y venir de la política mundial.

# Archivos

### 'book_test_markov.ipynb'
Este cuaderno Jupyter sirve como un ejemplo práctico para explorar las capacidades del paquete hmmlearn en el análisis de datos de precios y volúmenes de café.

### 'hmm_predictor.ipynb'
Este cuaderno utiliza un Modelo Oculto de Markov para predecir precios de cierre del café y generar señales de trading. Se entrena con datos históricos de precios de apertura, cierre, máximos y mínimos.

### 'correlations_cafe.ipynb'
Este cuaderno analiza las correlaciones entre los precios del café, petróleo WTI y el índice S&P 500. Utiliza pandas y Seaborn para manipular y visualizar datos, con el fin de entender la interconexión entre estos mercados.

### 'hmm_predictor.py'
Este módulo Python encapsula las funcionalidades del cuaderno hmm_predictor.ipynb. Facilita la predicción de precios del café y la generación de señales de trading para su uso en otros proyectos, sobretodo para la pagina web.

### 'coffee_web.html'
Este archivo HTML es la interfaz web de nuestro proyecto de "Predicción Financiera en el Mercado del Café". Para visualizar la página y acceder a sus funcionalidades, por favor descargue el archivo y ábralo con un navegador web.


