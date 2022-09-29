from deepface import DeepFace
ruta="./../faces/david.jpeg"
obj=DeepFace.analyze(img_path="C:/Users/David/Documents/GitHub/apertura-puertas-reconocimiento-facial/faces/david.jpeg",actions=['age','gender','race', 'emotion'])
print("El resultado del análisis es: ")
print(obj)