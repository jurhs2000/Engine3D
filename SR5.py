# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR5: Transformations

from src.objLoader import Texture, TextureBMP
from src.glTypes import V3
from src.gl import Renderer

width = 1920
height = 1080
rend = Renderer(width, height)

# MEDIUM SHOT
# Loads two models, and take a shot from the center focus on back center using lookAt
rend.glLookAt(V3(0, 0, -10), V3(0,0,0))
rend.glLoadModel(
    "models/lugia/lugia.obj",
    Texture("models/lugia/Lugia-TextureMap.jpg"),
    translate=V3(0, 5, -10), # Place the model upper
    scale=V3(1.5,1.5,1.5), # Scale the model
    light=V3(0, 0, -1),
    rotate=V3(40,-10,0) # Pitch the model on low angle and a bit to right
)
# Renders buckethead takes about 5 minutes
rend.glLoadModel(
    "models/buckethead/buckethead2.obj",
    translate=V3(0, 0, -5),
    scale=V3(0.5,0.5,-0.5),
    light=V3(0, 0, 1),
    rotate=V3(0,0,0)
)
rend.glFinish("outputs/mediumShot.bmp")

# HIGH ANGLE
# Same scene of medium shot, but with an upper angle and a bit from back
rend.glClear()
rend.glLookAt(V3(0, 0, -10), V3(0,3,7))
rend.glLoadModel(
    "models/lugia/lugia.obj",
    Texture("models/lugia/Lugia-TextureMap.jpg"),
    translate=V3(0, 5, -10),
    scale=V3(1.5,1.5,1.5),
    light=V3(0, 0, -1),
    rotate=V3(40,-10,0)
)
# Renders buckethead takes about 5 minutes
rend.glLoadModel(
    "models/buckethead/buckethead2.obj",
    translate=V3(0, 0, -5),
    scale=V3(0.5,0.5,-0.5),
    light=V3(0, 0, 1),
    rotate=V3(0,0,0)
)
rend.glFinish("outputs/highAngle.bmp")

# LOW ANGLE
# Place three models on the scene and take the shot from a low angle
rend.glClear()
rend.glLookAt(V3(0,1.5,-5), V3(0,-1,0), V3(0,1,0))
rend.glLoadModel(
    "models/piranha/piranha.obj",
    Texture("models/piranha/npc072_body.png"),
    translate=V3(3, 0, -5),
    scale=V3(1,1,1),
    light=V3(0, 0, -1),
    rotate=V3(0,0,0)
)
rend.glLoadModel(
    "models/sonic/source/sonic.obj",
    translate=V3(0,-0.3,-5),
    scale=V3(0.5,0.5,0.5),
    light=V3(-1, 1, -1),
    rotate=V3(0,30,0)
)
rend.glLoadModel(
    "models/face/face.obj",
    TextureBMP("models/face/face.bmp"),
    translate=V3(-3,1.5,-5),
    scale=V3(1,1,1),
    light=V3(0, 0, -1),
    rotate=V3(0,0,0)
)
rend.glFinish("outputs/lowAngle.bmp")

# DUTCH ANGLE
# Same scene of medium shot, but taken from one side and with the camera rotated
rend.glClear()
rend.glLookAt(V3(0,1.5,-5), V3(4,1.5,-0.5), V3(0,1,0.7))
rend.glLoadModel(
    "models/piranha/piranha.obj",
    Texture("models/piranha/npc072_body.png"),
    translate=V3(2, 0, -5),
    scale=V3(1,1,1),
    light=V3(0, 0, -1),
    rotate=V3(0,0,0)
)
rend.glLoadModel(
    "models/sonic/source/sonic.obj",
    translate=V3(-2,-0.3,-6),
    scale=V3(0.5,0.5,0.5),
    light=V3(-1, 1, -1),
    rotate=V3(0,30,0)
)
rend.glLoadModel(
    "models/face/face.obj",
    TextureBMP("models/face/face.bmp"),
    translate=V3(-3.5,1.5,-5.4),
    scale=V3(1,1,1),
    light=V3(0, 0, -1),
    rotate=V3(0,0,0)
)
rend.glFinish("outputs/dutchAngle.bmp")
