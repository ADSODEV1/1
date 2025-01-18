import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("📍 Validación de Direcciones y Cobertura")

# Subir el archivo Excel (.xlsx)
uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if uploaded_file:
    # Cargar el archivo Excel
    data = pd.read_excel(uploaded_file)

    # Verificar las columnas necesarias
    required_columns = {"Direccion", "Ciudad", "Cobertura", "Estrato"}
    if not required_columns.issubset(data.columns):
        st.error(f"El archivo debe contener las columnas: {', '.join(required_columns)}")
    else:
        # Solicitar la dirección y ciudad
        direccion = st.text_input("Ingrese la dirección:")
        ciudad = st.text_input("Ingrese la ciudad:")

        # Botón para realizar la búsqueda
        if st.button("Enviar"):
            if direccion and ciudad:
                # Filtrar los datos de acuerdo con la dirección y ciudad
                resultado = data[(data["Direccion"] == direccion) & (data["Ciudad"] == ciudad)]
                if not resultado.empty:
                    cobertura = resultado["Cobertura"].iloc[0]
                    estrato = resultado["Estrato"].iloc[0]
                    st.success(f"✅ Cobertura: {cobertura}\n🏠 Estrato: {estrato}")
                else:
                    st.error("❌ No se encontraron datos para la dirección y ciudad ingresadas.")
            else:
                st.warning("Por favor ingrese tanto la dirección como la ciudad.")


