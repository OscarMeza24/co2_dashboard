#!/bin/bash

# Script para instalar dependencias y ejecutar el dashboard
# Este script instala los paquetes necesarios y ejecuta la aplicación Streamlit
# Optimizado para Python 3.12+

echo ""
echo "========================================="
echo " Dashboard CO2 - Script de Instalacion"
echo "========================================="
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 no está instalado"
    echo "Por favor, instala Python 3.8+ desde python.org"
    exit 1
fi

echo "[1/4] Verificando instalacion de Python..."
python3 --version
echo "OK: Python instalado"

echo ""
echo "[2/4] Verificando instalacion de pip..."
if ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip3 no está instalado"
    exit 1
fi
echo "OK: pip3 instalado"

echo ""
echo "[3/4] Instalando dependencias..."
pip3 install --upgrade pip setuptools wheel
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias"
    exit 1
fi
echo "OK: Dependencias instaladas"

echo ""
echo "[4/4] Iniciando Dashboard..."
echo ""
echo "Abriendo en navegador: http://localhost:8501"
echo "Presiona Ctrl+C para detener el servidor"
echo ""

streamlit run app.py
