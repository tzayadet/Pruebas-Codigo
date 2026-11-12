# Pruebas de código

[![Python checks](https://github.com/tzayadet/Pruebas-Codigo/actions/workflows/python-checks.yml/badge.svg)](https://github.com/tzayadet/Pruebas-Codigo/actions/workflows/python-checks.yml)

Colección pequeña de ejercicios de Python. El repositorio conserva ejemplos de programación básica y transformaciones de texto con fines didácticos.

## Scripts

| Archivo | Descripción |
|---|---|
| `calculadora_basica.py` | Calculadora de consola con suma, resta, multiplicación y división. |
| `codificador.py` | Cifrado César (+3) y sustitución afín reversible, con conservación de mayúsculas y signos. |
| `decodificador_sistema_1.py` | Interfaz independiente para descodificar el ejemplo César (+3). |
| `build_exe.bat` | Compila un script Python a ejecutable Windows mediante PyInstaller. |

## Ejecución

Requisito: Python 3.10 o superior.

```bash
python calculadora_basica.py
python codificador.py
python decodificador_sistema_1.py
```

Para generar un ejecutable en Windows, instala PyInstaller y pasa el script como argumento:

```powershell
py -m pip install pyinstaller
.\build_exe.bat calculadora_basica.py
```

El resultado se guarda en `dist/`.

## Sobre los métodos de sustitución

Los métodos César y afín son ejercicios clásicos de criptografía histórica. Son vulnerables y **no proporcionan confidencialidad**. No deben utilizarse para proteger contraseñas, comunicaciones ni información real.

El segundo método utiliza una transformación afín con multiplicador 5, cuyo inverso modular es 21 en módulo 26. Se evita el multiplicador 2 del ejercicio anterior porque no tiene inverso modular módulo 26 y, por tanto, no permite descodificar todos los caracteres.

## Pruebas

```bash
python -m unittest discover -s tests -v
```

## Tecnologías

- Python estándar
- Funciones, bucles y control de flujo
- Manipulación de cadenas
- Aritmética modular
- Pruebas con `unittest`
