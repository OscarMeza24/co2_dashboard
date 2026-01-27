@echo off
REM Script para instalar dependencias y ejecutar el dashboard
REM Este script instala los paquetes necesarios y ejecuta la aplicación Streamlit
REM Optimizado para Python 3.12+

echo.
echo =========================================
echo  Dashboard CO2 - Script de Instalacion
echo =========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor, instala Python 3.8+ desde python.org
    pause
    exit /b 1
)

echo [1/4] Verificando instalacion de Python...
python --version
echo OK: Python instalado

echo.
echo [2/4] Verificando instalacion de pip...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pip no está instalado
    pause
    exit /b 1
)
echo OK: pip instalado

echo.
echo [3/4] Instalando dependencias...
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo OK: Dependencias instaladas

echo.
echo [4/4] Iniciando Dashboard...
echo.
echo Abriendo en navegador: http://localhost:8501
echo Presiona Ctrl+C para detener el servidor
echo.

streamlit run app.py

pause
