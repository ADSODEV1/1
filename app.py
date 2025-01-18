import streamlit as st
import pandas as pd
import io
import requests

# URL de Google Drive (reemplaza el ID con el tuyo)
google_drive_url = 'https://drive.google.com/uc?id=1epDJu6JkZuMOsXc5P77Tzw4vKKBu5hi-'  # Sustituye con tu URL

# Función para descargar el archivo desde Google Drive
def download_file_from_google_drive(url):
    session = requests.Session()
    response = session.get(url)
    return io.BytesIO(response.content)

# Descargar el archivo
file_data = download_file_from_google_drive(google_drive_url)

# Leer el archivo con pandas
data = pd.read_excel(file_data)

# Título de la aplicación
st.title("📍 Validación de Direcciones y Cobertura")

# Mostrar una vista previa de los datos
st.write("### Vista previa de los datos:", data.head())

# Verificar que las columnas necesarias existan
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
