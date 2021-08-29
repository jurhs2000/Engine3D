import functools
from src.shaders import *
from src.objLoader import Texture, TextureBMP
from src.glTypes import V3, newColor
from src.gl import Renderer

width = 1920
height = 1080
rend = Renderer(width, height)

rend.active_texture = Texture("models/face/face.bmp")
rend.normal_map = Texture("models/face/face_normal.bmp")
rend.active_shader = normalMap

modelPosition = V3(0, 0, -10)
rend.directional_light = V3(0.9,0,-0.7)
rend.glLookAt(modelPosition, V3(0, 0, 0))
rend.glLoadModel(
    "models/face/face.obj",
    translate=modelPosition,
    scale=V3(3,3,3),
    rotate=V3(10,-10,0)
)
rend.glFinish("outputs/normal.bmp")