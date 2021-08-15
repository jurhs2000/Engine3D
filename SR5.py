# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR5: Transformations

from src.objLoader import TextureBMP
from src.glTypes import V3
from src.gl import Renderer

width = 1920
height = 1080
rend = Renderer(width, height)

modelPosition = V3(0, 0, -10)

rend.glLookAt(modelPosition, V3(5,0,0))

rend.glLoadModel(
    "models/face/face.obj",
    TextureBMP("models/face/face.bmp"),
    translate=modelPosition,
    scale=V3(3,3,3),
    light=V3(0, 0, -1),
    rotate=V3(10,50,10)
)
rend.glFinish("outputs/faceTransform.bmp")
