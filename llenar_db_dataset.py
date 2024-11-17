from connect_database import ConnectDatabase
import os

dataset_path = "dataset"

#crear un objeto coneccion a base de datos
db = ConnectDatabase()


# Función para asignar la categoría basada en el nombre de la imagen
def asignar_categoria(nombre_imagen):
    if "cardboard" in nombre_imagen:
        return 1
    elif "glass" in nombre_imagen:
        return 2
    elif "metal" in nombre_imagen:
        return 3
    elif "paper" in nombre_imagen:
        return 4
    elif "plastic" in nombre_imagen:
        return 5
    else:
        return None  # Por si hay alguna imagen que no coincide
    

# Recorrer las carpetas dentro del dataset
for carpeta in os.listdir(dataset_path):
    carpeta_path = os.path.join(dataset_path, carpeta)

     # Ignorar la carpeta "trash"
    if carpeta == "trash":
        continue

    contador = 0

    # Recorrer cada imagen en la carpeta
    for imagen in os.listdir(carpeta_path):
        imagen_path = os.path.join(carpeta_path, imagen)
        
        # Solo agregar archivos que sean imágenes
        if os.path.isfile(imagen_path):
            print(imagen_path)

            #limitamos la carga de solo 10 imagenes para probar
            contador += 1

            if contador >= 10:
                break     
            
            categoria_imagen = asignar_categoria(imagen)

            print(categoria_imagen)
            print(imagen_path)

            # Convertir los backslashes en slashes
            imagen_path = imagen_path.replace("\\", "/")

            vectorCaracteristicas = "0.25,0.34,0.45"
            resultado = db.insert_image(imagen_path,vectorCaracteristicas,categoria_imagen)

            if resultado is True:
                print("Imagen insertada correctamente.")
            else:
                print("Error al insertar la imagen:", resultado)

            
            
            

             