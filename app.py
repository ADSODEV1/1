if uploaded_file:
    # Cargar el archivo Excel
    data = pd.read_excel(uploaded_file)
    
    # Renombrar las columnas si es necesario
    data.columns = data.columns.str.strip()  # Eliminar espacios adicionales
    
    # Renombrar las columnas a los nombres esperados
    data.rename(columns={
        'Dirección': 'Direccion',
        'Ciudad': 'Ciudad',
        'Cobertura': 'Cobertura',
        'Estrato': 'Estrato'
    }, inplace=True)
    
    # Continuar con el resto del código


