# 🚀 GUÍA RÁPIDA DE INICIO - Dashboard CO2

## Paso 1: Preparar el Entorno

### Opción A: Windows (Recomendado)

Simplemente haz doble clic en `run_dashboard.bat`. El script:
1. Verifica que Python está instalado
2. Instala todas las dependencias automáticamente
3. Abre el dashboard en tu navegador

### Opción B: Línea de Comandos (Todos los SO)

```bash
# Navega a la carpeta del proyecto
cd ruta/a/co2_dashboard

# Instala dependencias
pip install -r requirements.txt

# Inicia el dashboard
streamlit run app.py
```

## Paso 2: Usar el Dashboard

### Controles Principales (Sidebar Izquierdo)

1. **Región**: Selecciona la región geográfica
2. **Países**: Elige 1-5 países para comparar
3. **Año Inicial**: Desde qué año analizar (default: 2015)
4. **Año Final**: Hasta qué año analizar (default: 2022)
5. **Año para Mapa**: Año específico para visualizaciones geoespaciales

### Secciones del Dashboard

#### 📈 Resumen Estadístico
Métricas generales de los datos filtrados:
- CO2 Total (Megatoneladas)
- CO2 Promedio
- PIB Total (Billones USD)
- Población Total
- Número de Países

#### 📊 Sección 1: Evolución Temporal
**Gráfico de Líneas Interactivo**
- Una línea por país seleccionado
- Muestra tendencias a lo largo de los años
- Hover para ver valores exactos
- Zoom: Doble clic para acercar
- Tabla con datos completos debajo

#### 🗺️ Sección 2: Distribución Geoespacial
**Mapa Geoespacial del Mundo**
- Código de colores: Verde (bajo) → Rojo (alto)
- Interactivo: Zoom y pan con el ratón
- Información al pasar el cursor

**Gráfico de Barras Horizontales**
- Distribución por región (Asia, Europa, etc.)
- Valores ordenados para fácil comparación

#### 🔗 Sección 3: Relación Multivariable
**Gráfico 3D de Burbujas**
- X: Emisiones CO2
- Y: PIB (Producto Interno Bruto)
- Z: Población
- Tamaño de burbuja: Proporcional a población
- Color: Por región

**Interacción 3D**:
- Rotación: Arrastra con botón izquierdo
- Zoom: Rueda del ratón
- Pan: Shift + Arrastra

#### 🔍 Análisis Adicional
**Top 10 Países Emisores**
- Ranking de mayores contaminadores

**Intensidad Carbónica**
- Ratio CO2/PIB
- Indica eficiencia económica en términos ambientales

## Datos del Dataset

### Cobertura Geográfica
- **Asia**: China, India, Japón, Corea del Sur
- **Europa**: Rusia, Alemania, Reino Unido
- **América del Norte**: Estados Unidos, Canadá, México
- **América del Sur**: Brasil
- **Oceanía**: Australia

### Período
2015 - 2022 (8 años de datos)

### Métricas Incluidas
- CO2: Emisiones en Megatoneladas
- GDP: Producto Interno Bruto en Billones USD
- Population: Población total

## Ejemplos de Uso

### Ejemplo 1: Comparar Emisiones Globales
1. Selecciona **Región**: "Todas"
2. Selecciona **Países**: China, India, EE.UU.
3. Deja **Años**: 2015-2022
4. Observa cómo China lidera en emisiones

### Ejemplo 2: Analizar Región de Europa
1. Selecciona **Región**: "Europe"
2. Selecciona **Países**: Alemania, Reino Unido, Rusia
3. Observa las tendencias regionales
4. Compara intensidad carbónica

### Ejemplo 3: Explorar Año 2022
1. Usa **Año para Mapa**: 2022
2. Observa el mapa geoespacial
3. Revisa Top 10 Emisores actuales
4. Analiza relaciones en gráfico 3D

## Personalizar el Dashboard

### Agregar Nuevos Países
Edita `data_co2.csv`:
1. Abre con Excel o editor de texto
2. Agrega filas con formato: Country,Region,Year,CO2,GDP,Population
3. Guarda y recarga el dashboard (presiona F5 o reinicia)

### Cambiar Años
- Modifica `data_co2.csv` con nuevos años
- El dashboard ajustará automáticamente los sliders

### Ajustar Colores
Edita `app.py` línea ~245 (crear_mapa_geoespacial):
```python
color_continuous_scale="RdYlGn_r"  # Cambia este valor
```

Opciones: "Viridis", "Plasma", "Inferno", "Magma", "RdBu", "RdYlGn", etc.

## Solución de Problemas

### El dashboard no inicia
```bash
# Verifica Python
python --version

# Reinstala dependencias
pip install --upgrade -r requirements.txt

# Intenta nuevamente
streamlit run app.py
```

### Los datos no se cargan
- Asegúrate que `data_co2.csv` está en la misma carpeta que `app.py`
- El archivo CSV debe tener exactamente 6 columnas

### El dashboard es lento
- Reduce el rango de años (usa sliders)
- Selecciona menos países (máximo 5)
- Cierra otras aplicaciones

### Puerto 8501 ya en uso
```bash
streamlit run app.py --server.port 8502
```

## Atajos de Teclado en Streamlit

- `R`: Recargar la aplicación
- `C`: Limpiar cache
- `Ctrl+C`: Detener servidor (en terminal)

## Nextmovimientos Recomendados

1. ✅ Ejecuta el dashboard: `streamlit run app.py`
2. ✅ Experimenta con los filtros
3. ✅ Analiza las tendencias en los gráficos
4. ✅ Exporta gráficos (botón de cámara)
5. ✅ Personaliza con tus propios datos

## 📞 Soporte Rápido

| Problema | Solución |
|----------|----------|
| Python no encontrado | Instala desde python.org |
| pip no funciona | `python -m pip install` |
| Módulos faltantes | `pip install -r requirements.txt` |
| Datos no cargados | Verifica `data_co2.csv` existe |
| Gráficos no se ven | Recarga con `R` o `Ctrl+Shift+R` |

---

**¡Listo!** Disfruta explorando las emisiones globales de CO2 🌍
