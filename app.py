import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# Título de la aplicación
st.header("Panel de Control de Ventas de Vehículos")

# Casillas de verificación para mostrar gráficos
show_hist = st.checkbox("Mostrar Histograma")
show_scatter = st.checkbox("Mostrar Gráfico de Dispersión")

if show_hist:
    st.write("Histograma de odómetro")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write("Gráfico de dispersión entre odómetro y precio")
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="type")
    st.plotly_chart(fig_scatter, use_container_width=True)
