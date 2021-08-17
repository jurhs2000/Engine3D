# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR5: Transformations

from src.objLoader import Texture
from src.glTypes import V3
from src.gl import Renderer

width = 1920
height = 1080
rend = Renderer(width, height)

# modelPosition = V3(0, 0, -10)
# rend.glLookAt(modelPosition, V3(5,7,0))
# rend.glLoadModel(
#     "models/lugia/lugia.obj",
#     Texture("models/lugia/Lugia-TextureMap.jpg"),
#     translate=modelPosition,
#     scale=V3(1,1,1),
#     light=V3(0, 0, -1),
#     rotate=V3(0,0,0)
# )
# rend.glFinish("outputs/highAngle.bmp")

# modelPosition = V3(0, 0, -5)
# rend.glLookAt(modelPosition, V3(5,0,0))
# rend.glLoadModel(
#     "models/buckethead/buckethead2.obj",
#     translate=modelPosition,
#     scale=V3(1,1,-1),
#     light=V3(0, 0, 1),
#     rotate=V3(0,0,0)
# )
# rend.glFinish("outputs/mediumShot.bmp")

# modelPosition = V3(0, 0, -5)
# rend.glLookAt(V3(0,2,-5), V3(0,0,0))
# rend.glLoadModel(
#     "models/piranha/piranha.obj",
#     Texture("models/piranha/npc072_body.png"),
#     translate=modelPosition,
#     scale=V3(1,1,1),
#     light=V3(0, 0, -1),
#     rotate=V3(0,0,0)
# )
# rend.glFinish("outputs/lowAngle.bmp")

modelPosition = V3(0, 0, -7)
rend.glLookAt(V3(0, 3.2, -7), V3(0,3.2,0))
rend.glLoadModel(
    "models/sonic/source/sonic.obj",
    translate=modelPosition,
    scale=V3(1,1,1),
    light=V3(0, 0, -1),
    rotate=V3(0,0,0)
)
rend.glFinish("outputs/dutchAngle.bmp")
