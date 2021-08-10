# Charges an OBJ file

from glTypes import newColor
import struct
from PIL import Image

class Obj(object):
  def __init__(self, filename):
    with open(filename, "r") as f:
      self.lines = f.read().splitlines()

    self.vertices = []
    self.textcoords = []
    self.normals = []
    self.faces = []
    self.read()

  def read(self):
    for line in self.lines:
      if line:
        prefix, value = line.split(" ", 1)
        if prefix == "v": # Vertex
          self.vertices.append(list(map(float, value.split(" "))))
        elif prefix == "vt": # Text coordinate
          self.textcoords.append(list(map(float, value.split(" "))))
        elif prefix == "vn": # Normal vector
          self.normals.append(list(map(float, value.split(" "))))
        elif prefix == "f": # Face
          self.faces.append([ list(map(int, vertex.split("/"))) for vertex in value.split(" ") ])

class TextureBMP(object):
  def __init__(self, filename):
    self.filename = filename
    self.read()

  def read(self):
    with open(self.filename, "rb") as image:
      image.seek(10)
      headerSize = struct.unpack("=l", image.read(4))[0]

      image.seek(18) # 14 + 4
      self.width = struct.unpack("=l", image.read(4))[0]
      self.height = struct.unpack("=l", image.read(4))[0]

      image.seek(headerSize)
      
      self.pixels = []
      for x in range(self.width):
        self.pixels.append([])
        for y in range(self.height):
          b = ord(image.read(1)) / 255
          g = ord(image.read(1)) / 255
          r = ord(image.read(1)) / 255
          self.pixels[x].append(newColor(r,g,b))
        
  def getColor(self, tx, ty):
    if 0 <= tx < 1 and 0 <= ty < 1:
      x = round(tx * self.width)
      y = round(ty * self.height)
      return self.pixels[y][x]
    else:
      return newColor(0,0,0)

class Texture(object):
  def __init__(self, filename):
    self.filename = filename
    self.read()

  def read(self):
    self.image = Image.open(self.filename)
    imagePixels = self.image.load()
    self.pixels = []
    for x in range(self.image.size[0]):
      self.pixels.append([])
      for y in range(self.image.size[1]):
        r = imagePixels[x,y][0] / 255
        g = imagePixels[x,y][1] / 255
        b = imagePixels[x,y][2] / 255
        self.pixels[x].append(newColor(r, g, b))

  def getColor(self, tx, ty):
    if 0 <= tx < 1 and 0 <= ty < 1:
      x = round((tx) * self.image.size[0])
      y = round((1-ty) * self.image.size[1])
      if x < self.image.size[0] and y < self.image.size[1]:
        return self.pixels[x][y]
    else:
      return newColor(0,0,0)