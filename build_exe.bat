@echo off
setlocal

if "%~1"=="" (
    echo Uso: build_exe.bat ruta\al\script.py
    echo Ejemplo: build_exe.bat calculadora_basica.py
    exit /b 2
)

where py >nul 2>nul
if errorlevel 1 (
    echo No se encuentra el lanzador de Python "py".
    exit /b 1
)

py -m PyInstaller --onefile "%~1"
if errorlevel 1 (
    echo Error al generar el ejecutable.
    exit /b 1
)

echo Ejecutable generado en la carpeta dist.
endlocal
