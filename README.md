Script para Eliminar Fondo de Imágenes y Reemplazarlo
Este script utiliza la API de remove.bg para eliminar el fondo de una imagen y luego reemplazarlo por otro fondo de tu elección.

Requisitos
Python 3.x instalado.
Biblioteca requests instalada: pip install requests
Una clave API válida de remove.bg
Uso
Coloca la imagen que deseas procesar (por ejemplo, hiramcito.jpg) en el mismo directorio que el script.
Coloca la imagen de fondo (por ejemplo, nuevo_fondo.jpg) en el mismo directorio.
Reemplaza api_key con tu propia clave API de remove.bg.
Ejecuta el script con:
python nombre_del_script.py
La imagen resultante será guardada como imagen_final.png.

Notas
El fondo se redimensiona automáticamente para coincidir con el tamaño de la imagen sin fondo.
El script asume que ambas imágenes están en el mismo directorio y que la imagen de fondo tiene el mismo tamaño que la imagen recortada.
