# Universidad del Valle de Guatemala
# Grafica por Computadora - CC3044
# Julio Herrera 19402
# SR4: Triangulos

from src.objLoader import TextureBMP, Texture
from src.glTypes import V2, V3, newColor
from src.gl import Renderer

width = 1920
height = 1080
rend = Renderer(width, height)

rend.glTriangleStandard(V2(10,70), V2(50,160), V2(70,80), newColor(1,0,0))
rend.glTriangleStandard(V2(180,50), V2(150,1), V2(70,180), newColor(1,0,0))
rend.glTriangleStandard(V2(180,150), V2(120,160), V2(130,180), newColor(1,0,0))
rend.glLoadModel("models/face/face.obj", TextureBMP("models/face/face.bmp"), V3(width/2, height/2, 0), V3(450, 450, 450))
rend.glFinish("outputs/faceTexture.bmp")

rend.glClear()
rend.glLoadModel("models/piranha/piranha.obj", Texture("models/piranha/npc072_body.png"), V3(width/2, height/2 - 450, 0), V3(300, 300, 300))
rend.glFinish("outputs/piranha.bmp")

rend.glClear()
rend.glLoadModel("models/lugia/lugia.obj", Texture("models/lugia/Lugia-TextureMap.jpg"), V3(width/2, height/2, 0), V3(150, 150, 150))
rend.glFinish("outputs/lugia.bmp")
