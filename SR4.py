# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR4: Triangulos

from gl import Renderer, V2, color
from numpy import sin

width = 200
height = 200

rend = Renderer(width, height)

rend.glTriangle(V2(10,70), V2(50,160), V2(70,80), color(1,0,0))
rend.glTriangle(V2(180,50), V2(150,1), V2(70,180), color(1,0,0))
rend.glTriangle(V2(180,150), V2(120,160), V2(130,180), color(1,0,0))

rend.glFinish("outputs/triangles.bmp")