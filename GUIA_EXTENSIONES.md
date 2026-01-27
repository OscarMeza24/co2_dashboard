# 🔧 GUÍA DE EXTENSIÓN - Cómo Personalizar el Dashboard

## 📝 Agregar Nueva Métrica

### Paso 1: Actualizar el Dataset
Agrega una columna a `data_co2.csv`:
```csv
Country,Region,Year,CO2,GDP,Population,Renewables
China,Asia,2015,10030,11230,1376000000,3.5
```

### Paso 2: Actualizar app.py
En la sección de estadísticas:
```python
col6 = st.columns(6)[5]
with col6:
    renovables_promedio = df_filtrado_paises['Renewables'].mean()
    st.metric("Renovables (%)", f"{renovables_promedio:.1f}%")
```

---

## 📊 Agregar Nuevo Gráfico

### Ejemplo: Gráfico de Contaminantes por Tipo

```python
def crear_grafico_contaminantes(df, ano):
    """
    Crea un gráfico de pie con distribución de contaminantes.
    
    Args:
        df (pd.DataFrame): Datos para visualizar
        ano (int): Año a visualizar
        
    Returns:
        plotly.graph_objects.Figure: Figura de Plotly
    """
    df_ano = df[df['Year'] == ano].copy()
    
    # Asumir que tienes columnas: CO2, CH4, N2O
    contaminantes_total = {
        'CO2': df_ano['CO2'].sum(),
        'CH4': df_ano.get('CH4', 0).sum(),
        'N2O': df_ano.get('N2O', 0).sum()
    }
    
    fig = px.pie(
        values=list(contaminantes_total.values()),
        names=list(contaminantes_total.keys()),
        title=f"Distribución de Contaminantes - {ano}",
        hole=0.4  # Donut chart
    )
    
    fig.update_layout(height=400, template='plotly_white')
    return fig
```

### Uso en app.py:
```python
# En Sección 3
fig_contaminantes = crear_grafico_contaminantes(df, ano_mapa)
st.plotly_chart(fig_contaminantes, use_container_width=True)
```

---

## 🎛️ Agregar Nuevo Filtro

### Ejemplo: Filtro por Rango de PIB

```python
# En el sidebar
st.markdown("### 💰 Filtro Avanzado")
gdp_min = st.slider("PIB Mínimo (Billones USD):", 0, 30000, 0)
gdp_max = st.slider("PIB Máximo (Billones USD):", 0, 30000, 30000)

# Aplicar filtro
df_filtrado = df_filtrado[
    (df_filtrado['GDP'] >= gdp_min) & 
    (df_filtrado['GDP'] <= gdp_max)
]
```

---

## 📈 Agregar Análisis Estadístico

### Ejemplo: Correlación entre CO2 y PIB

```python
import plotly.figure_factory as ff

st.markdown("## 🔬 Matriz de Correlación")

# Calcular correlación
df_corr = df_filtrado[['CO2', 'GDP', 'Population']].corr()

# Visualizar
fig = ff.create_annotated_heatmap(
    z=df_corr.values,
    x=df_corr.columns,
    y=df_corr.columns,
    colorscale='RdBu',
    zmid=0
)

fig.update_layout(height=400)
st.plotly_chart(fig, use_container_width=True)
```

---

## 📥 Conectar a Base de Datos

### PostgreSQL

```python
import psycopg2
import pandas as pd

@st.cache_resource
def get_db():
    return psycopg2.connect(
        host="localhost",
        database="co2_db",
        user="postgres",
        password="password"
    )

@st.cache_data
def cargar_datos():
    conn = get_db()
    query = "SELECT * FROM emissions"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
```

### MongoDB

```python
import pymongo
from pymongo import MongoClient

@st.cache_resource
def get_mongo_client():
    return MongoClient("mongodb://localhost:27017/")

@st.cache_data
def cargar_datos():
    client = get_mongo_client()
    db = client["co2_database"]
    collection = db["emissions"]
    data = list(collection.find())
    return pd.DataFrame(data)
```

---

## 🎨 Personalizar Tema

### Cambiar Colores Globales

En `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF6B6B"        # Rojo
backgroundColor = "#1E1E2E"    # Gris oscuro
secondaryBackgroundColor = "#2D2D44"
textColor = "#FFFFFF"
font = "monospace"
```

### Temas Predefinidos Streamlit
- `light` (default)
- `dark`

Especificar: `streamlit run app.py --theme.base=dark`

---

## 📱 Hacer Dashboard Responsivo

### Ajustar para Móvil

```python
import streamlit as st

# Detectar dispositivo
if st.get_query_params().get("mobile", False):
    st.set_page_config(layout="centered")
else:
    st.set_page_config(layout="wide")

# Usar columns adaptativamente
if st.get_query_params().get("mobile", False):
    col1 = st.columns(1)
else:
    col1, col2 = st.columns(2)
```

---

## 🚀 Agregar Funcionalidad de Exportación

### Descargar Datos como CSV

```python
import io

st.markdown("### 📥 Descargar Datos")

# Generar CSV
csv = df_filtrado.to_csv(index=False)

st.download_button(
    label="Descargar CSV",
    data=csv,
    file_name=f"co2_data_{pd.Timestamp.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
)
```

### Descargar Gráfico como PNG

```python
# Los gráficos Plotly incluyen automáticamente
# un botón de descarga en la esquina superior derecha
# No requiere código adicional
```

---

## 🔔 Agregar Notificaciones

### Alertas Interactivas

```python
# Alerta si hay pico de contaminación
co2_2022 = df[df['Year'] == 2022]['CO2'].mean()

if co2_2022 > 5000:
    st.warning(f"⚠️ Alerta: Emisiones promedio en 2022 superan 5000 Mt: {co2_2022:.0f}")
elif co2_2022 < 3000:
    st.success(f"✅ Buena noticia: Emisiones promedio en 2022 están bajo control: {co2_2022:.0f}")
else:
    st.info(f"ℹ️ Emisiones promedio en 2022: {co2_2022:.0f} Mt")
```

---

## 🤖 Agregar Predicción con IA

### Usar Prophet para Forecast

```python
# Instalar: pip install prophet

from prophet import Prophet

def predecir_co2_futuro(df, pais, periodos=5):
    """Predice CO2 futuro usando Prophet"""
    df_pais = df[df['Country'] == pais][['Year', 'CO2']].copy()
    df_pais.columns = ['ds', 'y']
    df_pais['ds'] = pd.to_datetime(df_pais['ds'], format='%Y')
    
    model = Prophet(yearly_seasonality=True)
    model.fit(df_pais)
    
    future = model.make_future_dataframe(periods=periodos, freq='YS')
    forecast = model.predict(future)
    
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

# Usar en app.py
pais_pred = st.selectbox("Selecciona país para predicción:", paises_disponibles)
forecast = predecir_co2_futuro(df, pais_pred)

fig = px.line(forecast, x='ds', y='yhat', 
              title=f"Predicción CO2 - {pais_pred}",
              labels={'ds': 'Año', 'yhat': 'CO2 Predicho (Mt)'})
st.plotly_chart(fig, use_container_width=True)
```

---

## 📊 Agregar Comparación de Años

### Slider de Comparación

```python
col1, col2 = st.columns(2)

with col1:
    ano1 = st.slider("Año 1:", 2015, 2022, 2015)
with col2:
    ano2 = st.slider("Año 2:", 2015, 2022, 2022)

# Calcular diferencia
df_ano1 = df[df['Year'] == ano1].set_index('Country')
df_ano2 = df[df['Year'] == ano2].set_index('Country')

df_comparacion = pd.DataFrame({
    f'CO2 {ano1}': df_ano1['CO2'],
    f'CO2 {ano2}': df_ano2['CO2'],
    'Cambio': df_ano2['CO2'] - df_ano1['CO2'],
    '% Cambio': ((df_ano2['CO2'] - df_ano1['CO2']) / df_ano1['CO2'] * 100)
})

st.dataframe(df_comparacion)
```

---

## 🔗 Agregar Enlaces Externos

```python
st.markdown("""
### 📚 Enlaces Útiles
- [IPCC Reportes](https://www.ipcc.ch/)
- [Naciones Unidas - Cambio Climático](https://www.un.org/climate/)
- [Datos Abiertos](https://data.worldbank.org/)
""")
```

---

## 🎓 Agregar Sección Educativa

```python
with st.expander("🎓 ¿Qué es CO2?"):
    st.markdown("""
    El **dióxido de carbono (CO2)** es un gas de efecto invernadero 
    que contribuye al calentamiento global.
    
    ### Fuentes principales:
    - 🔥 Combustión de combustibles fósiles
    - 🏭 Procesos industriales
    - 🚗 Transporte
    - 🌾 Agricultura
    
    ### Efectos:
    - 🌡️ Aumento de temperatura
    - 🌊 Subida del nivel del mar
    - 🌍 Cambios en ecosistemas
    """)
```

---

## 🧪 Agregar Modo de Prueba

```python
st.sidebar.markdown("---")

if st.sidebar.checkbox("🔬 Modo Desarrollo"):
    st.markdown("### 🧪 Panel de Debugging")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ver Estructura de Datos"):
            st.write(df.info())
    
    with col2:
        if st.button("Ver Estadísticas Descriptivas"):
            st.write(df.describe())
    
    if st.checkbox("Ver Cache Stats"):
        st.write(st.caching_stats)
```

---

## 🔄 Versión con Actualización en Tiempo Real

```python
import time

st.markdown("## 🔄 Auto-refresh (desarrollo)")
auto_refresh = st.checkbox("Actualizar cada 60 segundos")

if auto_refresh:
    st.markdown("🔄 Actualizando datos...")
    time.sleep(60)
    st.rerun()
```

---

## 📊 Ejemplo Completo: Dashboard Mejorado

```python
# Combinar múltiples extensiones
st.set_page_config(layout="wide", page_title="CO2 Pro")

df = cargar_datos()

with st.sidebar:
    st.title("⚙️ Configuración")
    
    modo = st.radio("Modo:", ["Análisis", "Predicción", "Comparación"])
    
if modo == "Análisis":
    # Código actual
    pass
    
elif modo == "Predicción":
    pais = st.selectbox("País:", df['Country'].unique())
    forecast = predecir_co2_futuro(df, pais)
    st.plotly_chart(...)
    
elif modo == "Comparación":
    ano1 = st.slider("Año 1", 2015, 2022, 2015)
    ano2 = st.slider("Año 2", 2015, 2022, 2022)
    # Mostrar comparación
```

---

## 📞 Soporte para Extensiones

**¿Necesitas ayuda?**
1. Consulta la documentación oficial de Streamlit
2. Revisa ejemplos en GitHub
3. Busca en Stack Overflow con etiqueta `streamlit`

**Librerías Útiles Complementarias:**
- `streamlit-aggrid` - Tablas avanzadas
- `streamlit-plotly-events` - Manejo de eventos Plotly
- `streamlit-folium` - Mapas Folium
- `streamlit-lottie` - Animaciones Lottie
- `streamlit-echarts` - Gráficos ECharts

---

**¡Happy coding! 🚀**
