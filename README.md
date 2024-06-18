# Generador de Proyectos .NET con Python y Tkinter

Este proyecto permite crear nuevos proyectos de ASP.NET Core a través de una interfaz gráfica construida con `tkinter` en Python.

## Requisitos

- Python 3.x
- .NET SDK
- PyInstaller (opcional, para generar ejecutables)

## Instalación

1. **Instalar Python**: [Descargar e instalar Python](https://www.python.org/downloads/)
2. **Instalar .NET SDK**: [Descargar e instalar .NET SDK](https://dotnet.microsoft.com/download)
3. **Instalar PyInstaller** (opcional):

    ```sh
    pip install pyinstaller
    ```

## Uso

### Ejecutar el Script
Ejecutar en la linea de comandos 
```sh
python generator.py
```

### Generar el ejecutable
Para generar un ejecutable de este script, usa PyInstaller:
```sh
pyinstaller --onefile --windowed generator.py
```
* Nota: El ejecutable se encontrará en la carpeta /dist

## Notas
 - **Permisos en macOS y Linux:** Puede que necesites dar permisos de ejecución del archivo generado:
   ```sh
    chmod +x dist/generator
   ```
- **Solución de problemas:** Asegúrate de tener todas las dependencias instaladas y prueba el ejecutable en un entorno similar al de los usuarios finales.

## Enlaces Útiles

- [Documentación de Python](https://docs.python.org/3/)
- [Documentación de .NET](https://docs.microsoft.com/dotnet/)
- [PyInstaller](https://pyinstaller.org/)
