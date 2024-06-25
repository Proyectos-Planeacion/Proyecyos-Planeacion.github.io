import pandas  as pd, time, os

print("Descargando Diccionarios...")
tiempo = time.time()


#rep box Rosas


def Return_Consumo_Rose(directorio):
    ruta_usuario = os.path.expanduser("~")
    ruta_Aplicaciones = r"\Documents\Proyectos_Planeacion"
    directorio = ruta_usuario + ruta_Aplicaciones
    df = pd.read_csv(directorio + r"")
    