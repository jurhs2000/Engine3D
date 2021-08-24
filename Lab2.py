# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# Lab2: Shaders

import functools
from src.shaders import flat, gourad, phong, unlit, toon, coolShader, textureBlend, gradient
from src.objLoader import Texture, TextureBMP
from src.glTypes import V3, newColor
from src.gl import Renderer

width = 1920
height = 1080
rend = Renderer(width, height)

#rend.active_shader = toon
#rend.active_texture = Texture("models/lugia/Lugia-TextureMap.jpg")
#modelPosition = V3(0, 0, -10)
#rend.directional_light = V3(1, 0, -0.5)
#rend.glLookAt(V3(0, 0, -10), V3(0, 0, 0))
#rend.glLoadModel(
#    "models/lugia/lugia.obj",
#    translate=modelPosition,
#    scale=V3(1,1,1),
#    rotate=V3(0,0,0)
#)
#rend.glFinish("outputs/toonShader.bmp")

rend.glClear()
rend.active_shader = functools.partial(gradient, upColor=newColor(1, 0, 0), downColor=newColor(0, 0, 1))
rend.active_texture = Texture("models/lugia/Lugia-TextureMap.jpg")
modelPosition = V3(0, 0, -10)
rend.directional_light = V3(1, 0, -0.5)
rend.glLookAt(V3(0, 0, -10), V3(0, 0, 0))
rend.glLoadModel(
    "models/lugia/lugia.obj",
    translate=modelPosition,
    scale=V3(1,1,1),
    rotate=V3(0,0,0)
)
rend.glFinish("outputs/gradientShader.bmp")
