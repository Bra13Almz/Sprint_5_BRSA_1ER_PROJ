import pandas as pd
import plotly.express as px
import streamlit as st



st.title('Mi primer app')

st.header('Hacer clic en los botones para generar un histograma o un gráfico de dispersión respectivamente')



car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histogramas') 

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


disp_button = st.button('Construir gráfico de dispersión') 

if disp_button:
    st.write('Creación de gráfico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)








