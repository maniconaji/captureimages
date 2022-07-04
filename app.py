import os
import shutil

n = 0

def create_folder(path_images):
    # función para crear carpeta para almacenar información relevante obtenida 
    if os.path.isdir(path_images) == False:
        os.mkdir(path_images)
    else:
        pass

while True:
    if n == 0:
        print("""
        El actual programa permite la captura de imágenes con el algoritmo ffmpeg, el cual funciona de la siguiente manera:\n
        - Va a pedir la fecha, los fps (frames per second), el nombre de la cámara y el formato de la imagen, siendo estas variables a definir al comienzo del uso del programa.\n
        - Luego solicitará si se desean cambiar las propiedades de la cámara, lo cual debe realizar sí o sí cada vez que se reinicie el equipo.\n
        - Posteriormente pedirá la concentración de los analitos (Cu y Fe).\n
        - Y finalmente, se pide por el número de la replica de la muestra.\n
        - Al final, el programa les solicitará si desean volver a ejecutar el programa.\n\n

        Observaciones: No usar acento al escribir si. Se acepta como respuesta SI, Si o si.
        """)
        # primera ejecución para definir parámetros importantes.
        run     = "si"
        n       += 1
        fecha   = str(input("Inserte fecha en formato DD-MM-YYYY: "))
        fps     = int(input("Inserte fps (frames per second): "))
        name_camera = str(input('Inserte nombre camara: '))
        formato_img = str(input('Inserte formato imagen (recomendaciones: jpg o png): '))
        create_folder("imagenes/"+fecha)
    else:
        pass

    if run.lower() == "si":
        # parámetros que se definen cada vez que se volverá a ejecutar el programa.
        camaraprop = str(input('Ingrese si desea cambiar parámetros de camara: '))
        Cu_c        = str(input('Ingrese concentración de Cu: '))
        Fe_c        = str(input('Ingrese concentración de Fe: '))
        n_replica   = str(input('Inserte número de replica: '))

        # nombre de archivo
        nombrearchivo = "imagenes/"+fecha+"/"+Cu_c+"gL_"+Fe_c+"gL_12V_N00"+n_replica+"F%04d."+formato_img

        # ejecución de ffmpeg
        if camaraprop.lower() == "si":
            command = 'ffmpeg -y -rtbufsize 2048M -f dshow -show_video_device_dialog true  -i video="{0}" -t 120 -vf "fps={2:d}" {1}'.format(name_camera, nombrearchivo, fps)
            # print(command)
            os.system(command)
        else:
            command = 'ffmpeg -y -rtbufsize 2048M -f dshow -show_video_device_dialog false -i video="{0}" -t 120 -vf "fps={2:d}" {1}'.format(name_camera, nombrearchivo, fps)
            # print(command)
            os.system(command)
    else:
        # terminar de usar el programa
        break

    # eliminar ejecución anterior
    os.system("cls")
    
    #pregunta para seguir o parar el programa
    run = str(input('Ingrese si desea volver a ejecutar el programa:'))