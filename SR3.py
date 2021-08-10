# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR3: Obj Models

from glTypes import V3, newColor
from gl import Renderer
from numpy import sin

width = 1920
height = 1080

rend = Renderer(width, height)
rend.glLoadModel("models/teaport/teaport.obj", translate=V3(width/2, height/2 - 350, 0), scale=V3(200, 200, 200))
rend.glFinish("outputs/teaport.bmp")

rend.glClear()
rend.glLoadModel("models/face/face.obj", translate=V3(width/2, height/2, 0), scale=V3(400, 400, 400))
rend.glFinish("outputs/face.bmp")

rend.glClear()
rend.glLoadModel("models/gengar/gengar.obj", translate=V3(width/2, height/2 - 500, 0), scale=V3(450, 450, -450), light=V3(0,0,1))
rend.glFinish("outputs/gengar.bmp")

rend.glClear()
rend.glLoadModel("models/cuphead/cuphead2.obj", translate=V3(width/2, height/2 - 460, 0), scale=V3(110, 110, 110), light = V3(1.0,1.0,1.0))
rend.glFinish("outputs/cuphead.bmp")
