import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header('Proyecto Spring 6')  # Insertar titulo
build_histogram = st.checkbox('Construir histograma')  # crear un botón

if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Construir un histograma para la columna odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)