# estebansierra-st0263

# Introducción
Este proyecto es una implementación de un sistema de compartición de archivos peer-to-peer (P2P) utilizando Python.

Requisitos
Antes de ejecutar el proyecto, asegúrate de tener los siguientes requisitos instalados en tu entorno:
Python 3.6 o superior
pip (gestor de paquetes de Python)
Librerías adicionales especificadas en el archivo requirements.txt


# Instalación
Para instalar y configurar el proyecto localmente, sigue los siguientes pasos:

## Clona el repositorio:

git clone https://github.com/tali0517/estebansierra-st0263.git
cd estebansierra-st0263/p2psharing

## Crea un entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate

## Instala las dependencias:
pip install -r requirements.txt
Uso
Para ejecutar el sistema de compartición de archivos P2P, puedes seguir los siguientes pasos:

## Inicia el nodo servidor:

python server.py
Esto iniciará el servidor que se encargará de coordinar las solicitudes de los clientes.

## Inicia un nodo cliente:
python client.py
El cliente permitirá que los usuarios busquen y descarguen archivos desde otros nodos.

## Compartir un archivo:

En la interfaz de cliente, selecciona la opción de compartir un archivo e ingresa la ruta del archivo que deseas compartir.

## Descargar un archivo:
Busca el archivo en la red P2P utilizando la interfaz de cliente y selecciona la opción de descargar.
