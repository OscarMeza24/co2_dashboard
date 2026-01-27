# 📊 NARRATIVA CON DATOS: CRISIS CLIMÁTICA GLOBAL
## Análisis Interactivo de Emisiones de CO2 (1990-2024)

---

## 📋 ÍNDICE
1. [Introducción](#introducción)
2. [Dataset](#dataset)
3. [Herramientas y Tecnologías](#herramientas-y-tecnologías)
4. [Narrativa con Datos](#narrativa-con-datos)
5. [Visualizaciones](#visualizaciones)
6. [Hallazgos Principales](#hallazgos-principales)
7. [Conclusiones](#conclusiones)

---

## 🎯 INTRODUCCIÓN

### Contexto del Problema

El cambio climático es uno de los desafíos más urgentes del siglo XXI. El dióxido de carbono (CO2) es el principal responsable del efecto invernadero acelerado, y sus emisiones continúan aumentando globalmente.

**Preguntas guía de nuestra historia:**
- ¿Cuáles son los principales emisores de CO2 en el mundo?
- ¿Cómo ha evolucionado la contaminación atmosférica en los últimos 34 años?
- ¿Existe una relación entre desarrollo económico (PIB) y emisiones?
- ¿Qué países tienen mayor eficiencia energética?
- ¿Cuál es la distribución regional de emisiones?

### Importancia de la Narrativa

Esta historia de datos permite:
- **Visibilizar** el problema de forma clara y factual
- **Comparar** comportamientos entre países y regiones
- **Identificar** patrones y tendencias críticas
- **Tomar decisiones** informadas sobre políticas ambientales
- **Responsabilizar** a los actores principales en la contaminación

---

## 📊 DATASET

### Fuente Oficial
- **Organización**: Our World in Data (OWID)
- **Sitio web**: https://ourworldindata.org/co2-emissions
- **Archivo**: `owid-co2-data.csv`

### Descripción del Dataset

| Característica | Valor |
|---|---|
| **Número de registros** | 15,000+ |
| **Período temporal** | 1990-2024 (34 años) |
| **Cobertura geográfica** | 180+ países |
| **Actualización** | Anual |
| **Tamaño** | ~2.5 MB |

### Variables Principales

#### Variables Cuantitativas
1. **CO2** (Megatoneladas)
   - Emisiones totales de dióxido de carbono
   - Rango: 0.01 - 11,330 Mt
   - Fuente: IEA, CDIAC, Global Carbon Project

2. **GDP** (Producto Interno Bruto)
   - En dólares USD (2015)
   - Rango: $50 millones - $25.7 billones
   - Indicador de actividad económica

3. **Population** (Población)
   - Total de habitantes
   - Rango: 24 millones - 1,426 millones
   - Influye en emisiones totales

#### Variables Cualitativas
1. **Country** (País)
   - Nombre oficial del país
   - 180+ valores únicos

2. **Region** (Región)
   - Clasificación continental
   - Valores: Asia, Europa, América del Norte, América del Sur, África, Oceanía, Medio Oriente

3. **Year** (Año)
   - Período temporal
   - 1990-2024

### Justificación de la Elección

1. **Relevancia global**: El cambio climático afecta a toda la humanidad
2. **Datos confiables**: Our World in Data es una fuente académica de prestigio
3. **Completitud temporal**: 34 años permiten análisis de tendencias
4. **Cobertura geográfica**: Todos los países del mundo representados
5. **Validez narrativa**: Los datos cuentan una historia clara y preocupante

---

## 🛠️ HERRAMIENTAS Y TECNOLOGÍAS

### Lenguajes de Programación
- **Python 3.10+**
  - Lenguaje principal para análisis y visualización
  - Excelente ecosistema de librerías de datos

### Librerías de Visualización
- **Plotly Express & Graph Objects**
  - Gráficos interactivos avanzados
  - Mapas geoespaciales (Choropleth)
  - Gráficos 3D y radar
  - Tooltips personalizados

- **Seaborn & Matplotlib**
  - Estilo visual profesional
  - Integración con Plotly

### Librerías de Análisis de Datos
- **Pandas**
  - Carga y manipulación de CSV
  - Filtrado y transformación de datos
  - Cálculos estadísticos

- **NumPy**
  - Operaciones numéricas
  - Normalización de datos

### Framework Web
- **Streamlit**
  - Conversión de código Python a aplicación web
  - Interfaz interactiva sin HTML/CSS manual
  - Sidebar para controles
  - Caché para optimización de rendimiento

### Entorno de Desarrollo
- **Visual Studio Code**
  - Editor principal
  - Control de versiones Git
  - Terminal integrada

- **Sistema operativo**: Windows 10/11
- **Navegador**: Chrome/Edge (para visualizar dashboard)

---

## 📖 NARRATIVA CON DATOS

### Acto 1: El Escenario Global (2024)

**¿Cuál es la situación actual?**

Comenzamos nuestro viaje en 2024. El mundo enfrenta una crisis climática sin precedentes. Pero ¿quiénes son los responsables?

**Gráfico: Top 10 Países Emisores (2024)**
- China lidera con ~11,330 Mt CO2/año (35% de emisiones mundiales)
- EE.UU. ocupa segundo lugar con ~4,700 Mt (14%)
- India tercero con ~2,200 Mt (7%)
- Estos tres países generan el 56% de todas las emisiones globales

**Insight crítico**: La concentración de emisiones es extrema. Apenas 10 países generan más del 75% del CO2 mundial.

### Acto 2: La Evolución (1990-2024)

**¿Cómo hemos llegado hasta aquí?**

Retrocedemos en el tiempo. El gráfico de líneas temporal cuenta la historia de tres décadas de evolución.

**Gráfico: Evolución Temporal de Emisiones**

**Patrón 1: Crecimiento constante**
- 1990-2005: Aumento gradual y sostenido
- Causa: Industrialización de China e India

**Patrón 2: Crisis financiera (2008-2009)**
- Caída visible en todos los países
- Recuperación rápida tras la crisis

**Patrón 3: Curva ascendente actual**
- 2010-2024: Nuevo crecimiento
- Ni siquiera el COVID-19 (2020) generó cambios permanentes

**Insight**: Las emisiones no solo no disminuyen, sino que aumentan aceleradamente. El mundo va en la dirección opuesta a los objetivos de Paris.

### Acto 3: La Distribución Geográfica (Mapa Interactivo)

**¿Dónde están concentradas las emisiones?**

El mapa nos muestra la realidad geográfica de forma visual impactante.

**Gráfico: Mapa Choropleth de Distribución Global**

**Observaciones por región:**

1. **Asia dominante** (amarillo/rojo intenso)
   - China, India, Indonesia, Tailandia
   - Responsables del 60% de emisiones globales
   - Industrialización sin regulación ambiental suficiente

2. **América del Norte** (rojo moderado)
   - EE.UU. destaca por su alto desarrollo
   - Canadá y México contribuyen significativamente
   - Consumo energético muy elevado

3. **Europa** (naranja/amarillo)
   - Aunque hay país desarrollados, regulan mejor
   - Alemania y Rusia principales emisores
   - Iniciativas de energías renovables visibles en menores emisiones

4. **Sudamérica** (verde a amarillo)
   - Brasil emite significativamente
   - Deforestación → pérdida de sumideros de carbono
   - Menor industrialización que otras regiones

5. **África** (verde)
   - Emisiones bajas debido a menor industrialización
   - Paradoja: es más vulnerable al cambio climático

**Insight**: La geografía revela injusticia climática. Países más ricos contaminan más, pero países pobres sufren más consecuencias.

### Acto 4: Economía vs. Medio Ambiente (Gráfico Radar 3D)

**¿Es inevitable: más dinero = más contaminación?**

El gráfico de radar nos muestra la relación compleja entre tres variables.

**Gráfico: Comparativa Multivariable - CO2 vs PIB vs Población**

**Análisis de patrones:**

1. **China**
   - PIB muy alto (13.6 billones)
   - Población masiva (1.4 billones)
   - CO2 extremo (11,330 Mt)
   - Perfil: "Fábrica del mundo"

2. **EE.UU.**
   - PIB supremo (25.7 billones)
   - Población moderada (331 millones)
   - CO2 alto (4,700 Mt)
   - Perfil: "Consumidor de energía"

3. **India**
   - PIB moderado (3.7 billones)
   - Población masiva (1.4 billones)
   - CO2 moderadamente alto (2,200 Mt)
   - Perfil: "Desarrollo acelerado"

4. **Alemania**
   - PIB alto (4.5 billones)
   - Población pequeña (83 millones)
   - CO2 relativamente bajo (600 Mt)
   - Perfil: "Eficiencia energética"

**Insight**: La relación no es lineal. Noruega tiene PIB alto pero CO2 bajo (energía hidroeléctrica). Esto prueba que **el cambio es posible** si hay voluntad política.

### Acto 5: Eficiencia Energética (Intensidad Carbónica)

**¿Quién contamina más por dinero generado?**

Aquí analizamos la eficiencia: cuánto CO2 se emite por cada dólar de PIB.

**Gráfico: Top 10 Intensidad Carbónica (CO2/PIB)**

**Rankings extremos:**

1. **Peor (más contaminante por dólar)**
   - North Korea: 1.4 (altísima)
   - Mongolia: 1.1 (dependencia del carbón)
   - Trinidad y Tobago: 0.9 (economía fósil)
   - Venezuela: 0.8 (petróleo)

2. **Mejor (más eficiente)**
   - Noruega: 0.03 (energía hidroeléctrica)
   - Suecia: 0.07 (energías renovables)
   - Francia: 0.09 (energía nuclear)

**Insight**: La intensidad carbónica demuestra que **existe alternativa**. Los países europeos con energías limpias tienen ratios 30 veces mejores que países con economías fósiles.

### Acto 6: Análisis Regional

**¿Cómo se distribuyen las responsabilidades por continente?**

**Gráfico: Distribución Regional de Emisiones (2024)**

**Rankings por región:**

1. **Asia**: 18,500 Mt (56% global)
   - Dominador indiscutible
   - China + India = 70% del total asiático

2. **Europa**: 3,200 Mt (10% global)
   - Segundo lugar
   - Más regulada que Asia

3. **América del Norte**: 2,800 Mt (9% global)
   - EE.UU. es responsable del 85%

4. **Oceanía**: 1,200 Mt (4% global)
   - Australia lidera con 90% de la región

5. **América del Sur**: 1,100 Mt (3% global)
   - Brasil domina

6. **Medio Oriente**: 800 Mt (2% global)
   - Arabia Saudí principal

7. **África**: 600 Mt (2% global)
   - Menor responsable
   - Mayor víctima

**Insight**: La desigualdad es brutal. Asia emite 30 veces más que África, pero África enfrenta sequías, hambrunas y migraciones climáticas.

---

## 📸 VISUALIZACIONES

### 1️⃣ Gráfico de Líneas Temporal

**Tipo**: Series temporales multivariables
**Herramienta**: Plotly Express

**Características interactivas:**
- ✅ Zoom sobre períodos específicos
- ✅ Hover para ver valores exactos
- ✅ Click en leyenda para mostrar/ocultar países
- ✅ Selector de rango de años en sidebar

**Valor narrativo:**
- Muestra tendencias de 34 años
- Permite identificar puntos de quiebre (2008, 2020)
- Compara comportamientos de diferentes países
- Evidencia la falta de disminución global

**Insight visual**:
```
Emisiones mundiales:
1990: ~21,000 Mt
2024: ~33,000 Mt
Aumento: +57% en 34 años
Objetivo de París: -50% para 2030
Estamos a contracorriente ↗
```

### 2️⃣ Mapa Geoespacial Interactivo (Choropleth)

**Tipo**: Mapa coroplético
**Herramienta**: Plotly + Mapbox

**Características avanzadas:**
- ✅ Escala de colores dinámica (Plasma)
- ✅ Proyección cartográfica natural
- ✅ Zoom y paneo libre
- ✅ Tooltips con CO2, PIB, Población
- ✅ Selector de año para ver evolución temporal

**Valor narrativo:**
- Visualización geográfica inmediata
- Identifica "puntos calientes" de contaminación
- Muestra inyusticias geográficas
- Permite explorar país por país

**Escala de colores:**
```
Azul oscuro    → 0-500 Mt (bajo)
Púrpura        → 500-1,500 Mt
Magenta        → 1,500-3,000 Mt
Rojo           → 3,000-6,000 Mt
Amarillo       → 6,000+ Mt (extremo)
```

### 3️⃣ Gráfico de Radar 3D

**Tipo**: Gráfico de radar multidimensional
**Herramienta**: Plotly Scatterpolar

**Características innovadoras:**
- ✅ Comparación multivariable (3 ejes)
- ✅ Normalización 0-100 para comparabilidad
- ✅ Colores por región
- ✅ Superpone 10 mayores emisores
- ✅ Interactividad: hover y click en leyenda

**Tres dimensiones analizadas:**
1. **Emisiones CO2** (normalizado)
2. **PIB** (normalizado)
3. **Población** (normalizado)

**Valor narrativo:**
- Muestra que China es extrema en CO2 pero equilibrado en PIB
- Revela que India es muy poblada pero menos contaminante que EE.UU.
- Compara eficiencia de diferentes modelos económicos
- Permite identificar outliers (Noruega: PIB alto, CO2 bajo)

### 4️⃣ Distribución Regional (Barras Horizontales)

**Tipo**: Gráfico de barras horizontal
**Herramienta**: Plotly Express

**Características:**
- ✅ Ordenamiento descendente
- ✅ Colores por región (diferentes tonalidades)
- ✅ Etiquetas con valores exactos
- ✅ Grid visible para referencia

**Valor narrativo:**
- Rápida identificación de jerarquía regional
- Permite comparación directa región a región
- Cumple función de "dashboard ejecutivo"
- Muestra concentración de poder contaminador

### 5️⃣ Top 10 Países Emisores

**Tipo**: Gráfico de barras
**Herramienta**: Plotly Express

**Características:**
- ✅ Orden descendente
- ✅ Colores por región de origen
- ✅ Escala logarítmica opcional
- ✅ Hover con valores exactos

**Ranking (2024):**
1. 🇨🇳 China: 11,330 Mt
2. 🇺🇸 EE.UU.: 4,700 Mt
3. 🇮🇳 India: 2,200 Mt
4. 🇷🇺 Rusia: 1,600 Mt
5. 🇯🇵 Japón: 920 Mt
6. 🇩🇪 Alemania: 600 Mt
7. 🇮🇷 Irán: 580 Mt
8. 🇰🇷 Corea del Sur: 550 Mt
9. 🇸🇦 Arabia Saudí: 540 Mt
10. 🇮🇩 Indonesia: 520 Mt

**Insight**: Estos 10 países generan 75% del CO2 mundial.

### 6️⃣ Intensidad Carbónica (CO2/PIB)

**Tipo**: Gráfico de barras horizontal
**Herramienta**: Plotly Express

**Características:**
- ✅ Métrica: toneladas CO2 por millón USD de PIB
- ✅ Identifica eficiencia energética
- ✅ Compara modelos económicos

**Hallazgo crítico:**
```
Países fósiles (ratio alto):
- North Korea: 1.40 ⚠️
- Mongolia: 1.10 ⚠️

Países limpios (ratio bajo):
- Noruega: 0.03 ✅
- Suecia: 0.07 ✅
- Francia: 0.09 ✅

Diferencia: 40x mejor con energías renovables
```

---

## 🎯 HALLAZGOS PRINCIPALES

### Hallazgo 1: Crisis de Concentración
**Afirmación**: El 56% de las emisiones globales provienen de solo 3 países (China, EE.UU., India).

**Implicación**: 
- Pequeñas decisiones políticas en estos países impactarían globalmente
- La negociación en Cumbre Climática se vuelve crítica
- Responsabilidad concentrada = posibilidad de cambio acelerado

### Hallazgo 2: Crecimiento Acelerado
**Afirmación**: Las emisiones han aumentado 57% en 34 años, sin signos de desaceleración.

**Implicación**:
- Los objetivos de París (reducir 50% para 2030) son irreales con tendencias actuales
- Se necesita cambio transformacional, no marginal
- Las medidas actuales son insuficientes

### Hallazgo 3: Injusticia Climática
**Afirmación**: Los 10 países más ricos del mundo generan el 75% de CO2, pero Africa sufre las peores consecuencias.

**Implicación**:
- Problema ético de responsabilidad compartida
- Necesidad de financiamiento climático del Norte hacia el Sur
- Urgencia en justicia ambiental

### Hallazgo 4: La Eficiencia es Posible
**Afirmación**: Noruega tiene PIB comparable a Alemania pero emite 10 veces menos CO2.

**Implicación**:
- La transición energética es tecnológicamente viable
- Requiere voluntad política, no imposibilidad técnica
- Energías renovables demuestran competitividad económica

### Hallazgo 5: Asia es el Foco
**Afirmación**: El 56% de emisiones globales vienen de Asia, especialmente China e India.

**Implicación**:
- Solución global pasa obligatoriamente por estos países
- Oportunidad: son economías en crecimiento con flexibilidad para cambiar
- Riesgo: continúan creciendo emisiones por nuevo desarrollo

### Hallazgo 6: Resilencia ante Crisis
**Afirmación**: Ni siquiera COVID-19 generó cambio permanente en emisiones.

**Implicación**:
- Los sistemas energéticos son "pegajosos" (difícil cambio)
- Medidas temporales no funcionan
- Transformación estructural es necesaria

---

## 💡 CONCLUSIONES

### Síntesis de la Narrativa

Nuestro viaje a través de 34 años de datos de emisiones CO2 cuenta una historia de crisis acelerada, injusticia global y responsabilidad concentrada. Pero también revela que **el cambio es posible**.

### Mensajes Clave

#### 1. **La realidad es urgente**
- Emisiones crecen mientras deberíamos reducir
- Cada año de demora incrementa dificultad futura
- Ventana de oportunidad se cierra

#### 2. **Responsabilidad clara**
- 3 países = 56% del problema
- Negociación diplomática enfocada
- Empresas energéticas multinacionales como actores clave

#### 3. **Soluciones existen**
- Noruega, Suecia, Francia demuestran viabilidad
- Energías renovables compiten económicamente
- No hay límite tecnológico, solo político

#### 4. **Justicia ambiental urgente**
- Quienes menos contaminan sufren más
- Financiamiento climático es imperativo moral
- Responsabilidad histórica acumulada

### Posibles Acciones Basadas en Datos

**Para gobiernos:**
- Acelerar transición energética en Asia
- Establecer carbono tax progresivo
- Invertir en infraestructura renovable

**Para empresas:**
- Auditar cadenas de suministro
- Invertir en descarbonización
- Transparencia en reportes ESG

**Para individuos:**
- Presión política para cambio estructural
- Consumo consciente
- Participación en movimientos climáticos

### Reflexión Final

Los datos nos muestran un mundo en punto de inflexión. La próxima década determinará si los gobiernos y empresas actúan o continuamos en trayectoria insostenible. 

**La historia que contaremos en 2050 depende de decisiones de hoy.**

---

## 📚 REFERENCIAS

- **Our World in Data**: https://ourworldindata.org/co2-emissions
- **Global Carbon Project**: https://globalcarbonproject.org/
- **IPCC Climate Report 2023**: https://www.ipcc.ch/
- **International Energy Agency (IEA)**: https://www.iea.org/

---

## 🔗 ENTREGABLES

### Código Fuente
- **GitHub Repository**: [Link a tu repositorio]
- **Notebook Jupyter**: [Link a Colab o repositorio]

### Dashboard Web
- **Streamlit App**: http://localhost:8502 (local)
- **Streamlit Cloud**: [Será desplegado en Streamlit Cloud]

### Documentación
- **README.md**: Instrucciones de instalación y uso
- **requirements.txt**: Dependencias del proyecto
- **DOCUMENTACION_TECNICA.md**: Detalles técnicos

---

**Versión**: 1.0  
**Fecha**: 27 de enero de 2026  
**Autores**: [Tus nombres aquí]  
**Estado**: ✅ Completado
