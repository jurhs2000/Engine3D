# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# Lab1: Filling any polygon

from src.glTypes import newColor
from src.gl import Renderer

width = 900
height = 600

rend = Renderer(width, height)

# polygons

polygon1 = [(165, 380), (185, 360), (180, 330), (207, 345),
            (233, 330), (230, 360), (250, 380), (220, 385), 
            (205, 410), (193, 383)]
polygon2 = [(321, 335), (288, 286), (339, 251), (374, 302)]
polygon3 = [(377, 249), (411, 197), (436, 249)]
polygon4 = [(413, 177), (448, 159), (502, 88), (553, 53),
            (535, 36), (676, 37), (660, 52), (750, 145),
            (761, 179), (672, 192), (659, 214), (615, 214),
            (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)]
polygon5 = [(682, 175), (708, 120), (735, 148), (739, 170)]

# code here
rend.glFillPolygon(polygon1, colorBorder=newColor(0.2, 0.1, 1), colorFill=newColor(1, 0.8, 0))
rend.glFillPolygon(polygon2, colorBorder=newColor(1, 0.5, 0), colorFill=newColor(0.06, 0.09, 0.5))
rend.glFillPolygon(polygon3, colorBorder=newColor(0.7, 0.02, 0.8), colorFill=newColor(0.05, 0.9, 0.7))
rend.glFillPolygon(polygon4, colorBorder=newColor(1, 0, 1), colorFill=newColor(0.5, 0.5, 1))
rend.glFillPolygon(polygon5, colorBorder=newColor(1, 0, 1), colorFill=newColor(0, 0, 0))

rend.glFinish("outputs/Lab1.bmp")