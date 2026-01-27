"""
Dashboard Interactivo de Emisiones de CO2
Autor: Sistema de Visualización Autónoma
Descripción: Dashboard que visualiza emisiones de CO2 por país con análisis interactivos
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# ============================================================================
# CONFIGURACIÓN DE STREAMLIT
# ============================================================================

st.set_page_config(
    page_title="Dashboard CO2 Global",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

@st.cache_data
def cargar_datos():
    """
    Carga el dataset de CO2 desde Our World in Data (owid-co2-data.csv).
    
    Returns:
        pd.DataFrame: DataFrame con los datos de CO2
    """
    # Cargar el dataset de Our World in Data
    df = pd.read_csv('owid-co2-data.csv')
    
    # Renombrar columnas para consistencia
    if 'country' in df.columns:
        df = df.rename(columns={'country': 'Country'})
    if 'year' in df.columns:
        df = df.rename(columns={'year': 'Year'})
    if 'co2' in df.columns and 'Co2' not in df.columns:
        df = df.rename(columns={'co2': 'CO2'})
    if 'gdp' in df.columns:
        df = df.rename(columns={'gdp': 'GDP'})
    if 'population' in df.columns:
        df = df.rename(columns={'population': 'Population'})
    
    # Agregar región basada en el país
    def asignar_region(pais):
        regiones = {
            # Asia
            'China': 'Asia', 'India': 'Asia', 'Japan': 'Asia', 'South Korea': 'Asia',
            'Indonesia': 'Asia', 'Thailand': 'Asia', 'Vietnam': 'Asia', 'Philippines': 'Asia', 'Malaysia': 'Asia',
            'Pakistan': 'Asia', 'Bangladesh': 'Asia', 'Myanmar': 'Asia', 'Sri Lanka': 'Asia', 'Cambodia': 'Asia',
            'Hong Kong': 'Asia', 'Taiwan': 'Asia', 'Singapore': 'Asia', 'Nepal': 'Asia', 'Laos': 'Asia',
            'Mongolia': 'Asia', 'North Korea': 'Asia', 'Papua New Guinea': 'Asia', 'Brunei': 'Asia',
            'Timor-Leste': 'Asia', 'Bhutan': 'Asia', 'Maldives': 'Asia', 'Fiji': 'Oceania',
            # Europe
            'Russia': 'Europe', 'Germany': 'Europe', 'United Kingdom': 'Europe', 'Italy': 'Europe', 'France': 'Europe', 'Spain': 'Europe', 'Poland': 'Europe', 'Ukraine': 'Europe',
            'Turkey': 'Europe', 'Greece': 'Europe', 'Czech Republic': 'Europe', 'Hungary': 'Europe',
            'Romania': 'Europe', 'Netherlands': 'Europe', 'Belgium': 'Europe', 'Austria': 'Europe', 'Switzerland': 'Europe',
            'Sweden': 'Europe', 'Norway': 'Europe', 'Denmark': 'Europe', 'Finland': 'Europe', 'Portugal': 'Europe',
            'Slovakia': 'Europe', 'Bulgaria': 'Europe', 'Serbia': 'Europe', 'Croatia': 'Europe', 'Lithuania': 'Europe',
            'Slovenia': 'Europe', 'Latvia': 'Europe', 'Estonia': 'Europe', 'Bosnia': 'Europe', 'Albania': 'Europe',
            'Macedonia': 'Europe', 'Moldova': 'Europe', 'Belarus': 'Europe', 'Georgia': 'Europe', 'Armenia': 'Europe',
            'Azerbaijan': 'Europe', 'Iceland': 'Europe', 'Luxembourg': 'Europe', 'Malta': 'Europe', 'Cyprus': 'Europe',
            # North America
            'United States': 'North America', 'Canada': 'North America', 'Mexico': 'North America',
            'Costa Rica': 'North America', 'Panama': 'North America', 'Guatemala': 'North America',
            'Honduras': 'North America', 'El Salvador': 'North America', 'Nicaragua': 'North America', 'Belize': 'North America',
            'Jamaica': 'North America', 'Trinidad and Tobago': 'North America', 'Cuba': 'North America', 'Dominican Republic': 'North America',
            # South America
            'Brazil': 'South America', 'Argentina': 'South America', 'Colombia': 'South America',
            'Chile': 'South America', 'Peru': 'South America', 'Venezuela': 'South America',
            'Ecuador': 'South America', 'Bolivia': 'South America', 'Paraguay': 'South America', 'Uruguay': 'South America',
            'Guyana': 'South America', 'Suriname': 'South America',
            # Africa
            'South Africa': 'Africa', 'Nigeria': 'Africa', 'Egypt': 'Africa',
            'Morocco': 'Africa', 'Kenya': 'Africa', 'Uganda': 'Africa', 'Ethiopia': 'Africa', 'Ghana': 'Africa',
            'Algeria': 'Africa', 'Tunisia': 'Africa', 'Angola': 'Africa', 'Cameroon': 'Africa', 'Ivory Coast': 'Africa',
            'Sudan': 'Africa', 'Tanzania': 'Africa', 'Zimbabwe': 'Africa', 'Zambia': 'Africa', 'Botswana': 'Africa',
            'Senegal': 'Africa', 'Mali': 'Africa', 'Burkina Faso': 'Africa', 'Niger': 'Africa', 'Chad': 'Africa',
            'Mozambique': 'Africa', 'Malawi': 'Africa', 'Rwanda': 'Africa', 'Benin': 'Africa', 'Togo': 'Africa',
            'Gabon': 'Africa', 'Republic of Congo': 'Africa', 'Democratic Republic of Congo': 'Africa',
            # Middle East
            'Saudi Arabia': 'Middle East', 'Iran': 'Middle East', 'United Arab Emirates': 'Middle East',
            'Qatar': 'Middle East', 'Kuwait': 'Middle East', 'Bahrain': 'Middle East', 'Oman': 'Middle East', 
            'Iraq': 'Middle East', 'Israel': 'Middle East', 'Jordan': 'Middle East', 'Lebanon': 'Middle East',
            'Syria': 'Middle East', 'Yemen': 'Middle East', 'Palestine': 'Middle East',
            # Oceania
            'Australia': 'Oceania', 'New Zealand': 'Oceania', 'Fiji': 'Oceania', 'Samoa': 'Oceania',
            'Vanuatu': 'Oceania', 'Kiribati': 'Oceania', 'Solomon Islands': 'Oceania',
        }
        region = regiones.get(pais, None)
        return region  # Retorna None si no está en la lista
    
    if 'Region' not in df.columns:
        df['Region'] = df['Country'].apply(asignar_region)
    
    # IMPORTANTE: Excluir países sin región asignada (aquellos que hubieran sido "Otros")
    df = df[df['Region'].notna()].copy()
    
    # Filtrar solo datos con CO2 válidos y año >= 1990
    df = df[(df['CO2'].notna()) & (df['Year'] >= 1990)].copy()
    df = df.sort_values(['Country', 'Year']).reset_index(drop=True)
    
    return df


def obtener_estadisticas(df_filtrado):
    """
    Calcula estadísticas principales para el dashboard.
    
    Args:
        df_filtrado (pd.DataFrame): DataFrame filtrado
        
    Returns:
        dict: Diccionario con estadísticas
    """
    return {
        'co2_total': df_filtrado['CO2'].sum(),
        'co2_promedio': df_filtrado['CO2'].mean(),
        'gdp_total': df_filtrado['GDP'].sum(),
        'poblacion_total': df_filtrado['Population'].sum(),
        'paises': df_filtrado['Country'].nunique()
    }


def crear_grafico_lineas_temporal(df, paises_seleccionados, titulo):
    """
    Crea un gráfico de líneas temporal con filtro por país.
    
    Args:
        df (pd.DataFrame): Datos para visualizar
        paises_seleccionados (list): Lista de países a mostrar
        titulo (str): Título del gráfico
        
    Returns:
        plotly.graph_objects.Figure: Figura de Plotly
    """
    df_filtrado = df[df['Country'].isin(paises_seleccionados)]
    
    fig = px.line(
        df_filtrado,
        x='Year',
        y='CO2',
        color='Country',
        title=titulo,
        markers=True,
        hover_data={'Year': True, 'CO2': ':.0f', 'Country': True},
        labels={'Year': 'Año', 'CO2': 'Emisiones CO2 (Mt)'}
    )
    
    # Calcular rango dinámico con margen del 10%
    max_co2 = df_filtrado['CO2'].max()
    margin = max_co2 * 0.1
    
    fig.update_layout(
        hovermode='x unified',
        plot_bgcolor='rgba(249, 250, 251, 0.5)',
        paper_bgcolor='white',
        font=dict(size=11, color='#334155', family='Arial'),
        height=500,
        xaxis_title='Año',
        yaxis_title='Emisiones CO2 (Megatoneladas)',
        title_font=dict(size=16, color='#1e40af'),
        template='plotly_white',
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(59, 130, 246, 0.1)',
            zeroline=False,
            showline=True,
            linewidth=1,
            linecolor='rgba(59, 130, 246, 0.2)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(59, 130, 246, 0.1)',
            zeroline=False,
            showline=True,
            linewidth=1,
            linecolor='rgba(59, 130, 246, 0.2)',
            range=[0, max_co2 + margin]
        )
    )
    
    fig.update_traces(
        hovertemplate='<b>%{fullData.name}</b><br>Año: %{x}<br>CO2: %{y:,.0f} Mt<extra></extra>',
        line=dict(width=2.5)
    )
    
    return fig


def crear_mapa_geoespacial(df, ano_seleccionado):
    """
    Crea un mapa geoespacial interactivo con datos por país.
    
    Args:
        df (pd.DataFrame): Datos para visualizar
        ano_seleccionado (int): Año a visualizar
        
    Returns:
        plotly.graph_objects.Figure: Figura de Plotly
    """
    df_ano = df[df['Year'] == ano_seleccionado].copy()
    
    # Calcular el rango basado en TODO el dataset histórico para que sea consistente en el tiempo
    p95_global = df['CO2'].quantile(0.95)
    
    fig = px.choropleth(
        df_ano,
        locations="Country",
        locationmode="country names",
        color="CO2",
        hover_name="Country",
        hover_data={'CO2': ':,.0f', 'Country': False, 'Population': ':,.0f', 'GDP': ':,.0f'},
        title=f"DISTRIBUCIÓN GLOBAL DE CO2 - AÑO {ano_seleccionado}",
        color_continuous_scale="Plasma",
        labels={'CO2': 'CO2 (Mt)'},
        range_color=(0, p95_global)
    )
    
    fig.update_layout(
        geo=dict(
            showland=True,
            landcolor='rgb(242, 244, 248)',
            projection_type='natural earth',
            coastlinecolor='rgba(59, 130, 246, 0.2)',
            bgcolor='white',
            countrycolor='rgba(59, 130, 246, 0.1)'
        ),
        height=600,
        template='plotly_white',
        paper_bgcolor='white',
        title_font=dict(size=16, color='#1e40af'),
        font=dict(color='#334155')
    )
    
    return fig


def crear_grafico_radar(df, ano_seleccionado, region_seleccionada):
    """
    Crea un gráfico de radar comparativo de países/regiones.
    Compara CO2, PIB y Población de forma normalizada.
    
    Args:
        df (pd.DataFrame): Datos para visualizar
        ano_seleccionado (int): Año a visualizar
        region_seleccionada (str): Región a filtrar
        
    Returns:
        plotly.graph_objects.Figure: Figura de Plotly
    """
    df_filtrado = df[df['Year'] == ano_seleccionado].copy()
    
    if region_seleccionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['Region'] == region_seleccionada]
    
    # Filtrar valores nulos
    df_filtrado = df_filtrado.dropna(subset=['CO2', 'GDP', 'Population', 'Country'])
    
    # Seleccionar los 10 países principales por emisiones
    df_filtrado = df_filtrado.nlargest(10, 'CO2')
    
    # Normalizar variables a escala 0-100 para mejor visualización
    def normalizar(serie):
        minimo = serie.min()
        maximo = serie.max()
        if maximo == minimo:
            return pd.Series([50] * len(serie))
        return ((serie - minimo) / (maximo - minimo)) * 100
    
    df_radar = df_filtrado[['Country', 'CO2', 'GDP', 'Population']].copy()
    df_radar['CO2_norm'] = normalizar(df_filtrado['CO2'])
    df_radar['GDP_norm'] = normalizar(df_filtrado['GDP'])
    df_radar['Pop_norm'] = normalizar(df_filtrado['Population'])
    
    # Crear figura
    fig = go.Figure()
    
    # Categorías del radar
    categories = ['Emisiones CO2', 'PIB', 'Población']
    
    # Agregar traza para cada país
    colores = px.colors.qualitative.Set2
    for idx, (_, fila) in enumerate(df_radar.iterrows()):
        valores = [fila['CO2_norm'], fila['GDP_norm'], fila['Pop_norm']]
        
        fig.add_trace(go.Scatterpolar(
            r=valores,
            theta=categories,
            fill='toself',
            name=fila['Country'],
            line=dict(width=2),
            marker=dict(size=8),
            fillcolor=colores[idx % len(colores)],
            opacity=0.6
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color='#334155'),
                gridcolor='rgba(59, 130, 246, 0.15)'
            ),
            angularaxis=dict(
                tickfont=dict(size=11, color='#1e40af'),
                gridcolor='rgba(59, 130, 246, 0.2)'
            ),
            bgcolor='rgba(245, 247, 250, 0.3)'
        ),
        height=700,
        template='plotly_white',
        paper_bgcolor='white',
        title_font=dict(size=16, color='#1e40af'),
        font=dict(color='#334155'),
        title=f"COMPARATIVA DE INDICADORES - {ano_seleccionado}",
        showlegend=True,
        legend=dict(
            x=1.05,
            y=1,
            font=dict(size=10, color='#334155')
        ),
        hovermode='closest'
    )
    
    return fig


def crear_grafico_distribucion_regional(df, ano_seleccionado):
    """
    Crea un gráfico de distribución de CO2 por región.
    
    Args:
        df (pd.DataFrame): Datos para visualizar
        ano_seleccionado (int): Año a visualizar
        
    Returns:
        plotly.graph_objects.Figure: Figura de Plotly
    """
    df_ano = df[df['Year'] == ano_seleccionado].copy()
    df_regional = df_ano.groupby('Region')['CO2'].sum().reset_index().sort_values('CO2', ascending=True)
    
    fig = px.bar(
        df_regional,
        x='CO2',
        y='Region',
        orientation='h',
        title=f"DISTRIBUCIÓN REGIONAL DE EMISIONES CO2 - {ano_seleccionado}",
        labels={'CO2': 'Emisiones CO2 (Mt)', 'Region': 'Región'},
        color='CO2',
        color_continuous_scale='Turbo'
    )
    
    # Rango dinámico del eje X
    max_co2_region = df_regional['CO2'].max()
    margin = max_co2_region * 0.15
    
    fig.update_layout(
        height=400,
        template='plotly_white',
        paper_bgcolor='white',
        plot_bgcolor='rgba(245, 247, 250, 0.7)',
        hovermode='closest',
        title_font=dict(size=16, color='#1e40af'),
        font=dict(color='#334155'),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(59, 130, 246, 0.1)',
            showline=True,
            linewidth=1,
            linecolor='rgba(59, 130, 246, 0.2)',
            range=[0, max_co2_region + margin]
        ),
        yaxis=dict(
            showgrid=False,
            showline=True,
            linewidth=1,
            linecolor='rgba(59, 130, 246, 0.2)'
        )
    )
    
    return fig


# ============================================================================
# INTERFAZ PRINCIPAL
# ============================================================================

# Encabezado con estética moderna y sutil
st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 50%, #f0f4f8 100%);
    }
    
    [data-testid="stMainBlockContainer"] {
        background-color: transparent;
    }
    
    .main-header {
        font-size: 2.8em;
        background: linear-gradient(135deg, #2563eb 0%, #0ea5e9 50%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 10px;
        font-weight: 900;
        letter-spacing: 2px;
    }
    
    .sub-header {
        font-size: 1.1em;
        color: #475569;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    .cyber-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #3b82f6, #2563eb, transparent);
        margin: 30px 0;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
    }
    
    .section-title {
        font-size: 1.7em;
        color: #1e40af;
        margin: 30px 0 20px 0;
        padding-bottom: 15px;
        border-bottom: 2px solid #3b82f6;
        text-shadow: 0 0 8px rgba(59, 130, 246, 0.1);
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    
    .stat-card {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(14, 165, 233, 0.08) 100%);
        border: 1px solid rgba(59, 130, 246, 0.2);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.1);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        border-color: rgba(59, 130, 246, 0.4);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.15);
        transform: translateY(-2px);
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(14, 165, 233, 0.05) 100%);
        border: 1px solid rgba(59, 130, 246, 0.15);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.08);
    }
    </style>
    <div class="main-header">DASHBOARD GLOBAL CO2</div>
    <div class="sub-header">Sistema Interactivo de Monitoreo de Emisiones de Carbono</div>
    <div class="cyber-divider"></div>
""", unsafe_allow_html=True)

# Cargar datos
df = cargar_datos()

# ============================================================================
# SECCIÓN DE CONTEXTO E INFORMACIÓN
# ============================================================================

with st.expander("ℹ️ CONTEXTO E INFORMACIÓN - Haz clic para expandir", expanded=True):
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.markdown("""
        <div class="info-box">
        <h3 style="color: #1e40af; margin-top: 0;">¿Qué es el CO2 y por qué importa?</h3>
        <p style="color: #334155; line-height: 1.8;">
        El <b>dióxido de carbono (CO2)</b> es un gas de efecto invernadero que se libera 
        principalmente por la quema de combustibles fósiles (carbón, petróleo, gas natural).
        </p>
        <p style="color: #334155; line-height: 1.8;">
        <b>Impacto ambiental:</b>
        • Aumento de temperaturas globales
        • Cambio climático acelerado
        • Eventos climáticos extremos
        • Afectación de ecosistemas
        </p>
        <p style="color: #334155; line-height: 1.8;">
        <b>Monitorear las emisiones</b> es crucial para entender 
        el progreso hacia objetivos de descarbonización global.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_info2:
        st.markdown("""
        <div class="info-box">
        <h3 style="color: #1e40af; margin-top: 0;">Cómo usar este Dashboard</h3>
        <p style="color: #334155; line-height: 1.8;">
        <b>Panel de Control (Izquierda):</b>
        • Selecciona una región geográfica
        • Elige países específicos para analizar
        • Ajusta el rango de años
        </p>
        <p style="color: #334155; line-height: 1.8;">
        <b>Secciones:</b>
        • <b>Evolución Temporal:</b> Trend histórico de emisiones
        • <b>Distribución Geoespacial:</b> Mapa global interactivo
        • <b>Relación Multivariable:</b> Análisis CO2 vs PIB vs Población
        • <b>Análisis Avanzado:</b> Top emisores e intensidad carbónica
        </p>
        <p style="color: #334155; line-height: 1.8;">
        <b>Datos:</b> Our World in Data (1990-2024)
        </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div class='cyber-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# PANEL LATERAL - CONTROLES INTERACTIVOS
# ============================================================================

with st.sidebar:
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 50%, #e8ecf1 100%);
        border-right: 1px solid rgba(59, 130, 246, 0.15);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #1e40af;
    }
    
    .sidebar-title {
        font-size: 1.2em;
        color: #1e40af;
        text-shadow: 0 0 8px rgba(59, 130, 246, 0.1);
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 15px;
    }
    </style>
    <div class="sidebar-title">PANEL DE CONTROL</div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Selector de región
    regiones = ['Todas'] + sorted(df['Region'].unique().tolist())
    region_filtro = st.selectbox(
        "Selecciona Región:",
        regiones,
        help="Elige una región para filtrar los datos"
    )
    
    # Selector de países
    if region_filtro == 'Todas':
        paises_disponibles = sorted(df['Country'].unique().tolist())
    else:
        paises_disponibles = sorted(df[df['Region'] == region_filtro]['Country'].unique().tolist())
    
    paises_seleccionados = st.multiselect(
        "Selecciona Países:",
        paises_disponibles,
        default=paises_disponibles[:3],
        help="Elige los países para visualizar en los gráficos"
    )
    
    # Rango de años
    col_año1, col_año2 = st.columns(2)
    
    with col_año1:
        ano_min = st.slider(
            "Año Inicial:",
            1990,
            2024,
            1990,
            step=1,
            help="Año inicial para filtrar datos"
        )
    
    with col_año2:
        ano_max = st.slider(
            "Año Final:",
            1990,
            2024,
            2022,
            step=1,
            help="Año final para filtrar datos"
        )
    
    # Año específico para mapas
    ano_mapa = st.slider(
        "Año para Mapa:",
        1990,
        2024,
        2022,
        step=1,
        help="Selecciona el año para visualizar en el mapa"
    )
    
    st.markdown("---")
    st.markdown("""
    <div class="info-box">
    <div class="sidebar-title">INFORMACIÓN DE DATOS</div>
    <p style="color: #1e40af; font-size: 0.85em; line-height: 1.8;">
    <b>Fuente:</b> Our World in Data<br>
    <b>Registros:</b> """ + str(len(df)) + """<br>
    <b>Países:</b> """ + str(df['Country'].nunique()) + """<br>
    <b>⏰ Período:</b> """ + str(int(df['Year'].min())) + """-""" + str(int(df['Year'].max())) + """<br>
    <b>Regiones:</b> """ + str(df['Region'].nunique()) + """
    </p>
    </div>
    """, unsafe_allow_html=True)

# Aplicar filtros globales
df_filtrado = df[(df['Year'] >= ano_min) & (df['Year'] <= ano_max)]

if paises_seleccionados:
    df_filtrado_paises = df_filtrado[df_filtrado['Country'].isin(paises_seleccionados)]
else:
    df_filtrado_paises = df_filtrado

# ============================================================================
# SECCIÓN 1: ESTADÍSTICAS GENERALES
# ============================================================================

# ============================================================================
# SECCIÓN 1: ESTADÍSTICAS GENERALES
# ============================================================================

st.markdown("""<div class="section-title">RESUMEN ESTADÍSTICO EN TIEMPO REAL</div>""", unsafe_allow_html=True)

with st.expander("Explicación de métricas", expanded=False):
    st.markdown("""
    **CO2 Total:** Suma total de emisiones de CO2 (en Megatoneladas) del período y países seleccionados.
    
    **CO2 Promedio:** Promedio de emisiones por país. Indica el nivel típico de emisión.
    
    **PIB Total:** Producto Interno Bruto agregado. Refleja la actividad económica.
    
    **Población:** Total de habitantes en los países analizados.
    
    **Países Analizados:** Cantidad de naciones incluidas en la selección actual.
    """)

col1, col2, col3, col4, col5 = st.columns(5)

stats = obtener_estadisticas(df_filtrado_paises)

metric_style = """
<div class="stat-card">
    <div style="color: #1e40af; font-size: 0.8em; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 10px;">
        {label}
    </div>
    <div style="color: #0ea5e9; font-size: 1.8em; font-weight: 900; text-shadow: 0 0 8px rgba(14, 165, 233, 0.2);">
        {value}
    </div>
</div>
"""

with col1:
    st.markdown(metric_style.format(label="CO2 Total", value=f"{stats['co2_total']:,.0f}"), unsafe_allow_html=True)

with col2:
    st.markdown(metric_style.format(label="CO2 Promedio", value=f"{stats['co2_promedio']:,.0f}"), unsafe_allow_html=True)

with col3:
    st.markdown(metric_style.format(label="💰 PIB Total", value=f"${stats['gdp_total']/1e12:.2f}T"), unsafe_allow_html=True)

with col4:
    st.markdown(metric_style.format(label="👥 Población", value=f"{stats['poblacion_total']/1e9:.2f}B"), unsafe_allow_html=True)

with col5:
    st.markdown(metric_style.format(label="Países", value=f"{stats['paises']}"), unsafe_allow_html=True)

st.markdown("<div class='cyber-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# SECCIÓN 1: EVOLUCIÓN TEMPORAL
# ============================================================================

# ============================================================================
# SECCIÓN 2: EVOLUCIÓN TEMPORAL
# ============================================================================

st.markdown("""<div class="section-title">EVOLUCIÓN TEMPORAL DE EMISIONES</div>""", unsafe_allow_html=True)

with st.expander("Qué muestra este gráfico", expanded=False):
    st.markdown("""
    Este gráfico de **líneas temporales** muestra cómo han cambiado las emisiones de CO2 
    para cada país seleccionado a lo largo del tiempo (1990-2024).
    
    **Interpretación:**
    - **Línea hacia arriba** = Aumento de emisiones (generalmente indica crecimiento económico/industrial)
    - **Línea hacia abajo** = Reducción de emisiones (progreso hacia descarbonización)
    - **Línea plana** = Emisiones estables
    
    **Información útil:**
    - Puedes pasar el mouse sobre los puntos para ver valores exactos
    - Cada color representa un país diferente
    - Útil para identificar tendencias y patrones de cada nación
    """)

if paises_seleccionados:
    fig_lineas = crear_grafico_lineas_temporal(
        df,
        paises_seleccionados,
        f"EVOLUCIÓN DE EMISIONES CO2 - AÑOS {ano_min} a {ano_max}"
    )
    st.plotly_chart(fig_lineas, use_container_width=True)
else:
    st.warning("Selecciona al menos un país en los controles laterales para visualizar el gráfico temporal.")

# Tabla de datos
st.markdown("""<div style="color: #1e40af; font-size: 1.2em; font-weight: 700; margin: 20px 0 15px 0; letter-spacing: 1px;">TABLA DE DATOS - EVOLUCIÓN TEMPORAL</div>""", unsafe_allow_html=True)
if paises_seleccionados:
    df_tabla = df_filtrado_paises[['Country', 'Region', 'Year', 'CO2', 'GDP', 'Population']].sort_values(
        by=['Country', 'Year']
    )
    st.dataframe(df_tabla, use_container_width=True, hide_index=True)
else:
    st.info("Selecciona países para visualizar la tabla de datos")

st.markdown("<div class='cyber-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# SECCIÓN 2: DISTRIBUCIÓN GEOESPACIAL
# ============================================================================

# ============================================================================
# SECCIÓN 3: DISTRIBUCIÓN GEOESPACIAL
# ============================================================================

st.markdown("""<div class="section-title">DISTRIBUCIÓN GEOESPACIAL</div>""", unsafe_allow_html=True)

with st.expander("Cómo interpretar el mapa", expanded=False):
    st.markdown("""
    El **mapa de coropletas** muestra las emisiones de CO2 por país usando colores.
    
    **Escala de colores:**
    - **Azul oscuro** = Emisiones muy bajas (países en desarrollo, baja industrialización)
    - **Azul/Púrpura** = Emisiones bajas a moderadas
    - **Magenta/Rojo** = Emisiones altas (países industrializados, gran población)
    - **Amarillo** = Emisiones extremadamente altas (China, USA, India)
    
    **Datos mostrados:**
    - El mapa se actualiza según el año seleccionado en el slider
    - Puedes hacer zoom y arrastrar para explorar regiones específicas
    - Al pasar el mouse ves emisiones exactas, población y PIB
    
    **Nota:** El rango de colores es consistente para todos los años, 
    permitiendo comparaciones visuales entre períodos.
    """)

col_mapa1, col_mapa2 = st.columns([3, 1])

with col_mapa1:
    fig_mapa = crear_mapa_geoespacial(df, ano_mapa)
    st.plotly_chart(fig_mapa, use_container_width=True)

with col_mapa2:
    st.markdown("""
    <div class="info-box">
    <div style="color: #1e40af; font-size: 1.1em; font-weight: 700; margin-bottom: 15px; letter-spacing: 1px;">SOBRE EL MAPA</div>
    <p style="color: #334155; font-size: 0.9em; line-height: 1.8;">
    <b>Año:</b> """ + str(ano_mapa) + """<br>
    <b>Rojo/Magenta:</b> Mayor emisión<br>
    <b>Amarillo:</b> Emisión media<br>
    <b>Azul:</b> Menor emisión<br>
    <br>
    El mapa muestra la distribución
    global de emisiones usando
    una escala de colores para
    identificar rápidamente
    países con mayores emisiones.
    </p>
    </div>
    """, unsafe_allow_html=True)

# Gráfico de distribución regional
fig_dist_regional = crear_grafico_distribucion_regional(df, ano_mapa)
st.plotly_chart(fig_dist_regional, use_container_width=True)

st.markdown("<div class='cyber-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# SECCIÓN 3: RELACIÓN MULTIVARIABLE (3D)
# ============================================================================

# ============================================================================
# SECCIÓN 4: RELACIÓN MULTIVARIABLE (3D)
# ============================================================================

st.markdown("""<div class="section-title">RELACIÓN MULTIVARIABLE - CO2 vs PIB vs POBLACIÓN</div>""", unsafe_allow_html=True)

with st.expander("Análisis de relaciones complejas", expanded=False):
    st.markdown("""
    Este **gráfico de radar comparativo** muestra las relaciones entre tres dimensiones clave de forma visual e intuitiva.
    
    **Características:**
    - **Comparación visual:** Superpone perfiles de los 10 mayores emisores
    - **Normalización 0-100:** Facilita la comparación entre variables de diferentes escalas
    - **Tres dimensiones:** Emisiones CO2, PIB y Población
    - **Color por país:** Identifica fácilmente cada perfil
    - **Interactividad:** Selecciona/deselecciona países en la leyenda
    
    **Cómo interpretarlo:**
    - **Radios amplios** = Valores altos en esa variable
    - **Radios pequeños** = Valores bajos en esa variable
    - **Perfiles similares** = Países con comportamientos parecidos
    - **Perfiles distintos** = Diferentes modelos de emisión/producción
    
    **Ventajas sobre gráficos 2D:**
    - Comparación simultánea de múltiples variables
    - Identificación rápida de similitudes y diferencias
    - Mejor visualización de patrones regionales
    - Análisis de eficiencia (CO2 vs PIB)
    """)

col_3d1, col_3d2 = st.columns([3, 1])

with col_3d1:
    region_3d = st.selectbox(
        "Selecciona Región para Gráfico de Radar:",
        ["Todas"] + sorted(df['Region'].unique().tolist()),
        key="region_3d_selectbox"
    )
    
    fig_burbujas = crear_grafico_radar(df, ano_mapa, region_3d)
    st.plotly_chart(fig_burbujas, use_container_width=True)

with col_3d2:
    st.subheader("Interpretacion del Radar")
    st.write("**Variables:** Emisiones CO2, PIB, Poblacion")
    st.write("**Escala:** 0-100 (normalizado)")
    st.write("**Lectura:** Radios amplios indican valores altos relativos")

st.markdown("<div class='cyber-divider'></div>", unsafe_allow_html=True)

st.header("Analisis Avanzado")

col_análisis1, col_análisis2 = st.columns(2)

with col_análisis1:
    st.subheader("Top 10 Paises")
    df_top = df[df['Year'] == ano_mapa].nlargest(10, 'CO2')[['Country', 'CO2', 'Region']]
    fig_top = px.bar(df_top, x='CO2', y='Country', orientation='h', color='Region', 
                     title=f"Top 10 Emisores - {ano_mapa}", labels={'CO2': 'Emisiones (Mt)', 'Country': 'Pais'})
    fig_top.update_layout(height=450, template='plotly_white', paper_bgcolor='white', 
                          plot_bgcolor='rgba(245, 247, 250, 0.7)', title_font=dict(size=16, color='#1e40af'),
                          font=dict(color='#334155'), showlegend=False, 
                          xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(59, 130, 246, 0.1)'))
    st.plotly_chart(fig_top, use_container_width=True)

with col_análisis2:
    st.subheader("Intensidad Carbonica")
    df_intensidad = df[df['Year'] == ano_mapa].copy()
    df_intensidad['Intensidad'] = df_intensidad['CO2'] / (df_intensidad['GDP'] + 1)
    df_intensidad_top = df_intensidad.nlargest(10, 'Intensidad')[['Country', 'Intensidad', 'Region']]
    fig_intensidad = px.bar(df_intensidad_top, x='Intensidad', y='Country', orientation='h', color='Region',
                            title=f"Eficiencia Energetica - {ano_mapa}", labels={'Intensidad': 'CO2/PIB', 'Country': 'Pais'})
    fig_intensidad.update_layout(height=450, template='plotly_white', paper_bgcolor='white', 
                                plot_bgcolor='rgba(245, 247, 250, 0.7)', title_font=dict(size=16, color='#1e40af'),
                                font=dict(color='#334155'), showlegend=False,
                                xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(59, 130, 246, 0.1)'))
    st.plotly_chart(fig_intensidad, use_container_width=True)

st.markdown("<div class='cyber-divider'></div>", unsafe_allow_html=True)

with st.expander("Notas Metodologicas y Fuentes", expanded=False):
    col_nota1, col_nota2 = st.columns(2)
    with col_nota1:
        st.subheader("Fuente de Datos")
        st.write("**Our World in Data (OWID)**")
        st.write("Dataset de emisiones de carbono compilado por investigadores de la Universidad de Oxford.")
        st.write("- **Cobertura:** 180+ paises")
        st.write("- **Periodo:** 1750-2024")
    with col_nota2:
        st.subheader("Definiciones")
        st.write("**CO2:** Emisiones totales en megatoneladas")
        st.write("**PIB:** Producto Interno Bruto en USD (2015)")
        st.write("**Poblacion:** Total de habitantes")

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Dashboard CO2**  \nAnalisis Global 1990-2024")
with col2:
    st.write("**Fuente**  \nOur World in Data")
with col3:
    st.write("**Tecnologia**  \nStreamlit + Plotly")
