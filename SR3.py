# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR3: Obj Models

from gl import Renderer, V2, color
from numpy import sin

width = 1920
height = 1080

rend = Renderer(width, height)
rend.glLoadModel("models/teaport.obj", V2(width/2, height/2 - 350), V2(200, 200))
rend.glFinish("outputs/teaport.bmp")

rend.glClear()
rend.glLoadModel("models/face.obj", V2(width/2, height/2), V2(400, 400))
rend.glFinish("outputs/face.bmp")

rend.glClear()
rend.glLoadModel("models/gengar.obj", V2(width/2, height/2 - 500), V2(450, 450))
rend.glFinish("outputs/gengar.bmp")

rend.glClear()
rend.glLoadModel("models/cuphead.obj", V2(width/2, height/2 - 460), V2(110, 110))
rend.glFinish("outputs/cuphead.bmp")
