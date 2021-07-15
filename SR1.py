# Principal program

from gl import Renderer, V2, color
from numpy import sin

width = 800
height = 600

rend = Renderer(width, height)
rend.glClearColor(0.8, 0.8, 0.8)
rend.glClear()
rend.glColor(0.5, 0.7, 0.9)

rend.glVertex(0, 0, color(0, 0, 0))
rend.glVertex(-1, -1, color(0, 0, 0))
rend.glVertex(-1, 1, color(0, 0, 0))
rend.glVertex(1, -1, color(0, 0, 0))
rend.glVertex(1, 1, color(0, 0, 0))

rend.glViewPort(100, 250, 200, 100)

for x in range(width - 1):
  y0 = int((sin(x / 10) * 50) + height/2)
  y1 = int((sin((x+1) / 10) * 50) + height/2)
  rend.glLine(V2(x,y0), V2((x+1),y1), color(1, 0, 0))


rend.glVertex(0, 0, color(0, 0, 1))
rend.glVertex(-1, -1, color(0, 0, 1))
rend.glVertex(-1, 1, color(0, 0, 1))
rend.glVertex(1, -1, color(0, 0, 1))
rend.glVertex(1, 1, color(0, 0, 1))

rend.glFinish("SR1.bmp")