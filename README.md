# 🌍 Dashboard Interactivo de Emisiones CO2

Un dashboard completo desarrollado con **Streamlit** y **Plotly** para analizar emisiones de dióxido de carbono a nivel global (2015-2022).

## 📋 Características

### ✨ Visualizaciones Interactivas
1. **Gráfico de Líneas Temporal** - Evolución de emisiones por país con filtros
   - Zoom y pan interactivo
   - Tooltips detallados
   - Múltiples series de datos

2. **Mapa Geoespacial Interactivo** - Distribución global de emisiones
   - Código de colores (rojo = mayor emisión, verde = menor)
   - Proyección natural de la Tierra
   - Datos al pasar el cursor

3. **Gráfico 3D de Burbujas** - Relación CO2 vs PIB vs Población
   - Interacción 3D completa (rotación, zoom)
   - Tamaño de burbuja proporcional a población
   - Codificación por color por región

4. **Gráficos Adicionales**
   - Distribución regional de emisiones (barras horizontales)
   - Top 10 países emisores
   - Intensidad carbónica (CO2/PIB)

### 🎛️ Controles Interactivos en Sidebar
- Selector de región
- Multiselector de países
- Sliders para rango de años
- Selector de año para mapas

### 📊 Panel de Estadísticas
- CO2 Total y Promedio
- PIB Total
- Población Total
- Número de países analizados

## 🚀 Instalación y Uso

### 1. Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes Python)

### 2. Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el Dashboard

```bash
streamlit run app.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📁 Estructura del Proyecto

```
co2_dashboard/
├── app.py                 # Aplicación principal de Streamlit
├── data_co2.csv          # Dataset con datos de emisiones
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

## 📊 Fuentes de Datos

El archivo `data_co2.csv` contiene:
- **Country**: Nombre del país
- **Region**: Región geográfica (Asia, Europa, América del Norte/Sur, Oceanía)
- **Year**: Año (2015-2022)
- **CO2**: Emisiones en Megatoneladas (Mt)
- **GDP**: Producto Interno Bruto en Billones USD
- **Population**: Población total

### Países Incluidos
- China, India, Estados Unidos, Rusia, Japón
- Alemania, Reino Unido, Brasil, México, Canadá
- Australia, Corea del Sur

## 🔧 Estructura del Código

### Funciones Principales

#### `cargar_datos()`
Carga el dataset CSV con caché para optimizar rendimiento.

#### `obtener_estadisticas(df_filtrado)`
Calcula métricas principales: CO2 total/promedio, PIB, población, países únicos.

#### `crear_grafico_lineas_temporal(df, paises, titulo)`
Crea gráfico de líneas con múltiples series y tooltips interactivos.

#### `crear_mapa_geoespacial(df, ano)`
Genera choropleth interactivo con escala de color continua.

#### `crear_grafico_burbujas_3d(df, ano, region)`
Construye scatter plot 3D con codificación multivariable.

#### `crear_grafico_distribucion_regional(df, ano)`
Produce gráfico de barras horizontales con distribución por región.

## 🎨 Características de Diseño

- **Tema**: Plotly White con fondo claro
- **Colores**: Escalas Viridis y RdYlGn para mejor interpretación
- **Tipografía**: Limpia y legible en todos los gráficos
- **Responsive**: Adaptable a diferentes tamaños de pantalla
- **Interactivo**: Todos los gráficos soportan zoom, pan y hover

## 📈 Cómo Usar el Dashboard

### Workflow Típico

1. **Selecciona Región** - En el sidebar, elige una región (o "Todas")
2. **Elige Países** - Multiselecciona los países de interés (máximo 3-5 recomendado)
3. **Ajusta Años** - Usa los sliders para definir el rango temporal
4. **Analiza Visualizaciones**:
   - Evolución: Observa tendencias en el gráfico de líneas
   - Distribución: Compara emisiones globales en el mapa
   - Relación: Explora la correlación en el gráfico 3D
5. **Explora Top Emisores**: Revisa ranking y intensidad carbónica

### Tips de Interacción

- **Zoom**: Utiliza la rueda del ratón o doble clic
- **Pan**: Arrastra para mover la vista
- **Leyenda**: Haz clic en series para mostrar/ocultar
- **Hover**: Pasa el cursor para ver datos detallados
- **Descarga**: Usa el ícono de cámara para exportar gráficos

## 🔄 Actualizar con Nuevos Datos

Para actualizar con nuevos datos:

1. Reemplaza `data_co2.csv` con tu dataset (debe tener las mismas columnas)
2. Asegúrate de mantener el formato: Country, Region, Year, CO2, GDP, Population
3. Reinicia Streamlit: presiona `Ctrl+C` y ejecuta `streamlit run app.py` nuevamente

## 🐛 Solución de Problemas

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install streamlit
```

### El dashboard es muy lento
- Reduce el número de años en el slider
- Selecciona menos países
- Cierra otras aplicaciones

### Los datos no se cargan
- Verifica que `data_co2.csv` está en el mismo directorio que `app.py`
- Comprueba que el formato CSV es correcto

## 📝 Requisitos Completados

✅ Carga de dataset CSV con 6 columnas  
✅ 3 visualizaciones principales con Plotly Express  
✅ Tooltips, zoom y segmentadores en cada gráfico  
✅ Selectbox y sliders para filtrado  
✅ Secciones clara (Evolución, Distribución, Relación)  
✅ Código modular, limpio y comentado  
✅ Pandas para manejo de datos  
✅ Ejecutable con `streamlit run app.py`  

## 🛠️ Tecnologías Utilizadas

- **Streamlit**: Framework para aplicaciones web de datos
- **Plotly**: Biblioteca de gráficos interactivos
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Computación numérica
- **Python 3**: Lenguaje de programación

## 📄 Licencia

Proyecto educativo - Uso libre

## ✍️ Autor

Dashboard interactivo desarrollado como proyecto autónomo de visualización.

---

**¿Preguntas?** Revisa el código en `app.py` o consulta la documentación oficial:
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly Docs](https://plotly.com/python/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
