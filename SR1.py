# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR1: Points

from src.glTypes import V2, newColor
from src.gl import Renderer
from numpy import sin

width = 800
height = 600

rend = Renderer(width, height)
rend.glClearColor(0.8, 0.8, 0.8)
rend.glClear()
rend.glColor(0.5, 0.7, 0.9)

# Vertex with default viewport
rend.glVertex(0, 0, newColor(0, 0, 0))
rend.glVertex(-1, -1, newColor(0, 0, 0))
rend.glVertex(-1, 1, newColor(0, 0, 0))
rend.glVertex(1, -1, newColor(0, 0, 0))
rend.glVertex(1, 1, newColor(0, 0, 0))

# Stablishing a viewport
rend.glViewPort(100, 250, 200, 100)

# Drawing inside the viewport
for x in range(width - 1):
  y0 = int((sin(x / 10) * 50) + height/2)
  y1 = int((sin((x+1) / 10) * 50) + height/2)
  rend.glLine(V2(x,y0), V2((x+1),y1), newColor(1, 0, 0))

# Vertex with new viewport
rend.glVertex(0, 0, newColor(0, 0, 1))
rend.glVertex(-1, -1, newColor(0, 0, 1))
rend.glVertex(-1, 1, newColor(0, 0, 1))
rend.glVertex(1, -1, newColor(0, 0, 1))
rend.glVertex(1, 1, newColor(0, 0, 1))

rend.glFinish("outputs/SR1.bmp")