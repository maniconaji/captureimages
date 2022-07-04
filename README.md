# Obtener imagenes desde la cámara

El presente algoritmo esta construido para obtener imágenes en base al algoritmo ["ffmpeg"](https://ffmpeg.org/) con el fin de mejorar la experiencia de cualquier usuario que desee usarlo. Este permite la captura de imágenes con el algoritmo ffmpeg, el cual funciona de la siguiente manera:
- Va a pedir la fecha, los fps (frames per second) y el nombre de la cmara, siendo estas variables a definir al comienzo del uso del programa.
- Luego solicitará si se desean cambiar las propiedades de la cámara, lo cual debe realizar sí o sí cada vez que se reinicie el equipo.
- Posteriormente pedirá la concentración de los analitos (Cu y Fe).
- Y finalmente, se pide por el número de la replica de la muestra.
- Al final, el programa les solicitará si desean volver a ejecutar el programa.

Observaciones: No usar acento al escribir si. Se acepta como respuesta SI, Si o si.

Requisitos para cambiar detalles en la aplicación: instalar paquete [Auto PY to EXE](https://github.com/brentvollebregt/auto-py-to-exe) y modificar app.py