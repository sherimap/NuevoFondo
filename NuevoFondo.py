#!/usr/bin/env python3

import requests
from PIL import Image

# Configuración de la API y rutas de archivo
input_path = 'hiramcito.jpg'
output_path = 'hiramcito.png'
api_key = '7NfqCXM4m6tfTNKXcLuUkoYG'  # Reemplázala por tu clave de remove.bg
background_path = 'nuevo-fondo.jpg'  # Ruta del fondo con el que quieres reemplazar el fondo original

# Leer la imagen y enviar la solicitud para eliminar el fondo
with open(input_path, 'rb') as file:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': file},
        data={'size': 'auto'},
        headers={'X-Api-Key': api_key},
    )

# Manejar la respuesta
if response.status_code == 200:
    with open(output_path, 'wb') as out_file:
        out_file.write(response.content)
    print(f"Fondo eliminado. Imagen guardada en {output_path}")

    # Abrir la imagen sin fondo
    image = Image.open(output_path).convert("RGBA")  # Asegurarse de que tiene un canal alpha

    # Abrir el fondo
    background = Image.open(background_path).convert("RGBA")

    # Redimensionar el fondo para que coincida con el tamaño de la imagen sin fondo
    background = background.resize(image.size)

    # Combinar las dos imágenes (montar la imagen sin fondo sobre el fondo)
    combined = Image.alpha_composite(background, image)

    # Guardar la imagen combinada
    combined.save('imagen_final.png')
    print("Imagen final guardada como imagen_final.png")

else:
    print(f"Error: {response.status_code} - {response.text}")




