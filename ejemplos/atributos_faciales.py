from deepface import DeepFace
ruta="./../faces/david.jpeg"
obj=DeepFace.analyze(img_path="./faces/david.jpeg",actions=['age','gender','race', 'emotion'])
print("El resultado del análisis es: ")
print(obj)