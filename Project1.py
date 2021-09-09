# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# Proyecto 1: Software Renderer

import functools
from src.shaders import *
from src.objLoader import Texture, TextureBMP
from src.glTypes import V3, newColor
from src.gl import Renderer

width = 1920
height = 1080
#width = 192
#height = 108
rend = Renderer(width, height)

rend.background = Texture("textures/mbg2.png")
rend.glClearBackground()
rend.directional_light = V3(0, -0.5, -1)
#rend.glLookAt(V3(0, 0, -10), V3(0, 1.5, -2.5)) # Camara 1
#rend.glLookAt(V3(0, 0, -10), V3(0, 0.5, -2.5)) # Camara 2
#rend.glLookAt(V3(0, 0, -10), V3(-2, 10, -2.5)) # Camara 3
#rend.glLookAt(V3(0, 0, -10), V3(7, 4, -15)) # Camara 4
rend.glLookAt(V3(0, 0, -10), V3(-0.5, 4, -12)) # Camara 5

rend.active_shader = toon
rend.active_texture = Texture("models/smw/textures/lambert1_albedo.jpeg")
modelPosition = V3(0, 0, -10)
rend.glLoadModel(
    "models/smw/source/smw.obj",
    translate=modelPosition,
    scale=V3(1,1,1),
    rotate=V3(0,0,0)
)

rend.active_shader = normalMap
rend.active_texture = Texture("models/mario/textures/Mario_Base_Color.png")
rend.normal_map = Texture("models/mario/textures/Mario_Normal_DirectX.png")
modelPosition = V3(0, 0.03, -5.8)
rend.glLoadModel(
    "models/mario/source/mario.obj",
    translate=modelPosition,
    scale=V3(0.05,0.05,0.05),
    rotate=V3(0,0,0)
)


rend.active_shader = normalMap
rend.active_texture = Texture("models/piranha/npc072_body.png")
rend.normal_map = Texture("models/piranha/npc072_body_nml.png")
modelPosition = V3(-2.9, 0.03, -9.5)
rend.glLoadModel(
    "models/piranha/piranha.obj",
    translate=modelPosition,
    scale=V3(0.4,0.4,0.4),
    rotate=V3(0,45,0)
)

rend.active_shader = functools.partial(gradient, upColor=newColor(1, 0, 0), downColor=newColor(0, 0, 1))
rend.active_texture = Texture("models/brick/textures/Brick_Texture.png")
modelPosition = V3(0.5, 1, -5.8)
rend.glLoadModel(
    "models/brick/source/brick.obj",
    translate=modelPosition,
    scale=V3(0.15,0.15,0.15),
    rotate=V3(0,0,0)
)

rend.active_shader = noise
rend.active_texture = None
modelPosition = V3(1.5, 1, -5.8)
rend.glLoadModel(
    "models/brick/source/question.obj",
    translate=modelPosition,
    scale=V3(0.02,0.02,0.02),
    rotate=V3(45,45,0)
)

rend.active_shader = coolShader
rend.active_texture = Texture("models/brick/textures/red.jpg")
modelPosition = V3(-0.5, 1, -5.8)
rend.glLoadModel(
    "models/brick/source/red.obj",
    translate=modelPosition,
    scale=V3(0.15,0.15,0.15),
    rotate=V3(45,45,0)
)

rend.active_shader = textureBlend
rend.active_texture = Texture("models/bowser/textures/DryKoopaAll.png")
rend.active_texture_2 = Texture("models/bowser/textures/DryKoopaAllGlow.png")
modelPosition = V3(0, 1.47, -12)
rend.glLoadModel(
    "models/bowser/source/pose.obj",
    translate=modelPosition,
    scale=V3(0.07,0.07,0.07),
    rotate=V3(0,-20,0)
)

rend.active_shader = functools.partial(highlighter, highColor=newColor(0.5,0.2,1))
rend.active_texture = Texture("models/boo/textures/BooTexture.png")
modelPosition = V3(-5, 2, -10)
rend.glLoadModel(
    "models/boo/source/boo.obj",
    translate=modelPosition,
    scale=V3(1,1,1),
    rotate=V3(90,45,-60)
)

rend.active_shader = functools.partial(cut, axis='z', interval=40)
rend.active_texture = Texture("models/fish/fish.jpg")
modelPosition = V3(2.5,-0.4, -6)
rend.glLoadModel(
    "models/fish/fish.obj",
    translate=modelPosition,
    scale=V3(0.2,0.2,0.2),
    rotate=V3(0,20,-40)
)

rend.glFinish("outputs/Proyecto1.bmp")