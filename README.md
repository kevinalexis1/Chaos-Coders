# Chaos-Coders

Este repositorio esta hecho en el contexte del Hackaton Co-Afina 2023 organizado por La-Conga Physics (https://laconga.redclara.net). Durante el evento se presentaron varios retos, de los cuales se selecciono: #reto-1-pronosticando-el-mercado. 
Para este reto se busco diseñar modelos que permitan predecir el comportamiento del mercado financiero. Esto se lo hizo con ayuda de modelos de machine learning como el Hidden Markov Model (HMM) que usando matrizes de probabilidades y la definicion de estados ocultos, permite reconocer patrones en los datos propuestos atravez de un un aprendizaje no supervisado. Atravez del cual es posible obtener señales de compra y venta de los activos.

Para este reto se usaron datos del mercado de futuros de Café (KC=F), que pueden ser encontrados en https://finance.yahoo.com/quote/KC%3DF/history?period1=946857600&period2=1697760000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true, estos datos fueron obtenidos con una frecuencia semanal.
El resultado de estas señales es simulado con los datos del mercado, de manera que nos permiten medir su rendimiento posible. Luego estos resultados son comparados con una técnica básica de negociación de productos financieron, que consiste en la compra y retención de estos, comunmente conocida como holding. 

Ademas se presenta la posibilidad de mejorar los modelos, incluyendo información de diferentes mercados relacionados directamente al ir y venir de la política mundial. 


