# 📊 Dataset Actualizado: Our World in Data

El dashboard ahora utiliza el dataset oficial de **Our World in Data (OWID)** en lugar del ejemplo inicial.

## 🔄 Cambios Realizados

### Dataset Anterior
- **Origen**: Datos de ejemplo
- **Registros**: 100
- **Período**: 2015-2022 (8 años)
- **Países**: 12
- **Columnas**: Country, Region, Year, CO2, GDP, Population

### Dataset Actual (OWID)
- **Origen**: Our World in Data (owid-co2-data.csv)
- **Registros**: Miles de registros
- **Período**: 1750-presente (desde 1990 activo)
- **Países**: 190+ países
- **Columnas**: 85+ métricas diferentes

## 📈 Nuevas Métricas Disponibles

El dataset OWID incluye estas métricas adicionales:

```
Emisiones por Tipo:
├─ co2                    → CO2 total (Mt)
├─ coal_co2               → CO2 del carbón
├─ gas_co2                → CO2 del gas natural
├─ oil_co2                → CO2 del petróleo
├─ cement_co2             → CO2 del cemento
├─ flaring_co2            → CO2 del quemado de gas

Per Cápita:
├─ co2_per_capita         → CO2 por habitante
├─ coal_co2_per_capita    → Carbón per cápita
├─ gas_co2_per_capita     → Gas per cápita
└─ oil_co2_per_capita     → Petróleo per cápita

Eficiencia:
├─ co2_per_gdp            → CO2 por unidad de PIB
├─ co2_per_unit_energy    → CO2 por unidad de energía

Otros Gases:
├─ methane                → Emisiones de metano
├─ nitrous_oxide          → Óxido nitroso
├─ total_ghg              → Total de GEI

Acumulativos:
├─ cumulative_co2         → CO2 acumulado histórico
└─ share_global_co2       → % del CO2 global
```

## 🌍 Cobertura Geográfica

El dashboard ahora cubre automáticamente:
- **Todos los países del mundo** (190+)
- **Todas las regiones** (actualizado automáticamente)
- **Datos desde 1990 hasta hoy**

## ⚙️ Funcionamiento Automático

El código detecta automáticamente qué archivo existe:

```python
# Intenta OWID primero
try:
    df = pd.read_csv('owid-co2-data.csv')
except FileNotFoundError:
    # Fallback al archivo de ejemplo
    df = pd.read_csv('data_co2.csv')
```

## 🚀 Beneficios de OWID

✅ **Datos Verificados**: Revisados por expertos  
✅ **Actualización Regular**: Cada mes se actualiza  
✅ **Cobertura Global**: 190+ países  
✅ **Historial Completo**: Desde 1750 para algunos países  
✅ **Múltiples Métricas**: 85+ indicadores  
✅ **Acceso Libre**: Licencia CC BY 4.0  

## 📥 Cómo Actualizar el Dataset

Si quieres una versión más reciente:

1. Descarga desde: https://github.com/owid/co2-data
2. Extrae: `owid-co2-data.csv`
3. Coloca en: `co2_dashboard/`
4. El dashboard se actualiza automáticamente

## 🔗 Referencias

- **Página OWID CO2**: https://ourworldindata.org/co2-emissions
- **GitHub Repo**: https://github.com/owid/co2-data
- **Metodología**: https://ourworldindata.org/grapher/co2-emissions

---

**¡El dashboard ahora usa datos reales y verificados del mundo! 🌍📊**
