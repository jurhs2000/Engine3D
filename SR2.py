# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR2: Lines

from gl import Renderer, V2, color
from numpy import sin

width = 800
height = 600

rend = Renderer(width, height)
rend.glClearColor(0.8, 0.8, 0.8)
rend.glClear()
rend.glColor(0.5, 0.7, 0.9)

for x in range(0, width, 5):
  rend.glLine(V2(x, 0), V2(width, x))

# Horizontal, left to right
rend.glLine(V2(100,100), V2(500, 100), color(1,0,0))
# Horizontal, right to left
rend.glLine(V2(500,110), V2(100, 110), color(0,1,0))
# Vertical, top to bottom
rend.glLine(V2(305,400), V2(305, 120), color(1,0,0))
# Vertical, bottom to top
rend.glLine(V2(295,120), V2(295, 400), color(0,1,0))
# Diagonal, top left to bottom right
rend.glLine(V2(-1,1), V2(1,-1), color(1,0,0), True)
# Diagonal, bottom left to top right
rend.glLine(V2(-1,-1), V2(1,1), color(0,1,0), True)

# Stablishing a viewport
rend.glViewPort(400, 200, 200, 200)

# Vertex with new viewport
rend.glVertex(0, 0, color(0, 0, 1))
rend.glVertex(-1, -1, color(0, 0, 1))
rend.glVertex(-1, 1, color(0, 0, 1))
rend.glVertex(1, -1, color(0, 0, 1))
rend.glVertex(1, 1, color(0, 0, 1))

for x in range(width - 1):
  y0 = int((sin(x / 10) * 50) + height/2)
  y1 = int((sin((x+1) / 10) * 50) + height/2)
  rend.glLine(V2(x,y0), V2((x+1),y1), color(0.5, 0, 0.5))

# Diagonal, bottom right to top left
rend.glLine(V2(1,-1), V2(-1,1), color(0.5,0.5,0), True)
# Diagonal, top right to bottom left
rend.glLine(V2(1,1), V2(-1,-1), color(0,0.5,0.5), True)

# Stablishing a viewport
rend.glViewPort(50, 350, 200, 200)

for x in range(21):
  # left to right
  rend.glLine(V2(((x/10)-1), -1), V2(1, ((x/10)-1)), color(0.4, 0.5, 0.3), True)
  # top to bottom
  rend.glLine(V2(-1, ((x/10)-1)*-1), V2(((x/10)-1), -1), color(0.4, 0.5, 0.3), True)
  # bottom to top
  rend.glLine(V2(-1, ((x/10)-1)), V2(((x/10)-1), 1), color(0.4, 0.5, 0.3), True)
  # left to right
  rend.glLine(V2(((x/10)-1), 1), V2(1, ((x/10)-1)*-1), color(0.4, 0.5, 0.3), True)

# Stablishing a viewport
rend.glViewPort(450, 425, 150, 150)

for x in range(21):
  # right to left
  rend.glLine(V2(1, ((x/10)-1)), V2(((x/10)-1), -1), color(0.8, 0.1, 0.3), True)
  # bottom to top
  rend.glLine(V2(((x/10)-1), -1), V2(-1, ((x/10)-1)*-1),  color(0.8, 0.1, 0.3), True)
  # top to bottom
  rend.glLine(V2(((x/10)-1), 1), V2(-1, ((x/10)-1)), color(0.8, 0.1, 0.3), True)
  # right to left
  rend.glLine(V2(1, ((x/10)-1)*-1), V2(((x/10)-1), 1), color(0.8, 0.1, 0.3), True)

# Stablishing a viewport
rend.glViewPort(0, 0, width, height)

rend.glColor(0.2, 0.4, 1)

# polygon 1
rend.glLine(V2(10, 10), V2(110, 10))
rend.glLine(V2(110, 10), V2(110, 110))
rend.glLine(V2(110, 110), V2(10, 110))
rend.glLine(V2(10, 110), V2(10, 10))

# polygon 2
rend.glLine(V2(120, 120), V2(90, 200))
rend.glLine(V2(90, 200), V2(160, 240))
rend.glLine(V2(160, 240), V2(230, 200))
rend.glLine(V2(230, 200), V2(200, 120))
rend.glLine(V2(200, 120), V2(120, 120))

# polygon 3
rend.glLine(V2(250, 200), V2(350, 350))
rend.glLine(V2(350, 350), V2(400, 250))
rend.glLine(V2(400, 250), V2(250, 200))

# polygon 4
rend.glLine(V2(300, 80), V2(250, 180))
rend.glLine(V2(250, 180), V2(450, 180))
rend.glLine(V2(450, 180), V2(500, 80))
rend.glLine(V2(500, 80), V2(300, 80))

# polygon 5
for x in range(200):
  y0 = int(pow(x-100, 2))
  y1 = int(pow(x+1-100, 2))
  rend.glLine(V2(x+400,y0), V2((x+400+1),y1), color(0.9, 0.3, 0.1))

for x in range(400):
  y0 = int(pow(((x-200)/20), 3))
  y1 = int(pow((((x-200)+1)/20), 3))
  rend.glLine(V2(x+100,y0+300), V2((x+100+1),y1+300), color(0.9, 0.3, 0.1))

rend.glFinish("SR2.bmp")