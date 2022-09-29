#Importar librería
from deepface import DeepFace
from numpy import identity
import pandas as pd

#Buscar rostro
print("Buscando rostro")

#df = DeepFace.find(img_path = "img1.jp",db_path="/home/david/Documentos/github/apertura-puertas-reconocimiento-facial/bd")
df = DeepFace.find (img_path = "/home/david/Documentos/github/apertura-puertas-reconocimiento-facial/faces/zooey.jpg", db_path = "/home/david/Documentos/github/apertura-puertas-reconocimiento-facial/bd", enforce_detection = "false")
print("Resultado")
print(df)
print("Selección")
print(df.identity[0])