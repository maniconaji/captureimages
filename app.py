import os
import shutil

n = 0
name_camera = "GC21 Video"

def create_folder(path_images):
    # función para crear carpeta para almacenar información relevante obtenida 
    if os.path.isdir(path_images) == False:
        os.mkdir(path_images)
    else:
        pass

while True:
    if n == 0:
        run     = "si"
        n       += 1
        fecha   = str(input("Inserte fecha en formato DD-MM-YYYY:"))
        create_folder("imagenes/"+fecha)
    else:
        pass

    if run.lower() == "si":
        camaraprop = str(input('Ingrese si desea cambiar parámetros de camara:'))
        Cu_c        = str(input('Ingrese concentración de Cu: '))
        Fe_c        = str(input('Ingrese concentración de Fe: '))
        n_replica   = str(input('Inserte número de replica:'))
        
        nombrearchivo = "imagenes/"+fecha+"/"+Cu_c+"gL_"+Fe_c+"gL_12V_N00"+n_replica+"F%04d.jpg"

        if camaraprop.lower() == "si":
            command = 'ffmpeg -y -rtbufsize 2048M -f dshow -show_video_device_dialog true -i video="{0}" -t 10 -vf "scale=3840:2160,fps=1" {1}'.format(name_camera, nombrearchivo)
            # print(command)
            os.system(command)
        else:
            command = 'ffmpeg -y -rtbufsize 2048M -f dshow -show_video_device_dialog false -i video="{0}" -t 10 -vf "scale=3840:2160,fps=1" {1}'.format(name_camera, nombrearchivo)
            # print(command)
            os.system(command)
    else:
        break

    run = str(input('Ingrese si desea ejecutar o volver a ejecutar el programa:'))