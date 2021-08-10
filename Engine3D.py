# Principal program

from gl import Renderer, V2, newColor
from numpy import sin, cos

width = 960
height = 540

rend = Renderer(width, height)

#rend.glViewPort(50, 50, 100, 50)

rend.glClearColor(0.7, 0.3, 0.1)
rend.glClear()

rend.glColor(0.3, 0.7, 0.9)

rend.glPoint(100, 100)

rend.glLine(V2(500,400), V2(100, 300))
rend.glLine(V2(0,0), V2(50, 530))
rend.glLine(V2(0,0), V2(959, 539))
rend.glLine(V2(200, 100), V2(200, 500))
rend.glLine(V2(200, 100), V2(700, 100))
rend.glLine(V2(600, 500), V2(600, 50))
rend.glLine(V2(800, 50), V2(25, 50))

for x in range(width - 1):
  y0 = int((sin(x / 10) * 50) + height/2)
  y1 = int((sin((x+1) / 10) * 50) + height/2)
  rend.glLine(V2(x,y0), V2((x+1),y1), newColor(1, 0, 0))

for x in range(0, width, 5):
  rend.glLine(V2(x, 0), V2(width, x))

rend.glVertex(0, 0, newColor(0, 0, 0))
rend.glVertex(-1, -1, newColor(0, 0, 0))
rend.glVertex(-1, 1, newColor(0, 0, 0))
rend.glVertex(1, -1, newColor(0, 0, 0))
rend.glVertex(1, 1, newColor(0, 0, 0))


rend.glFinish("outputs/output.bmp")
