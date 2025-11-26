import csv
import os

def obtener_ruta_csv():
    # Ruta absoluta de este archivo
    ruta_actual = os.path.abspath(__file__)

    # Carpeta del proyecto: subir un nivel desde /src/
    carpeta_proyecto = os.path.dirname(os.path.dirname(ruta_actual))

    # Carpeta data al mismo nivel que src
    carpeta_data = os.path.join(carpeta_proyecto, "data")

    # Crear carpeta si no existe
    os.makedirs(carpeta_data, exist_ok=True)

    # Ruta completa del archivo personas.csv
    return os.path.join(carpeta_data, "personas.csv")

def inicializar_csv():
    ruta = obtener_ruta_csv()

    if not os.path.exists(ruta):
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Nombre", "Número"])

def guardar_persona(nombre, numero):
    try:
        ruta = obtener_ruta_csv()
        with open(ruta, "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre, numero])
        return True
    except Exception as e:
        print("Error al guardar:", e)
        return False