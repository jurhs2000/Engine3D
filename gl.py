# Graphics Library

import struct
from collections import namedtuple
from objLoader import Obj

def char(c):
  # 1 byte
  return struct.pack('=c', c.encode('ascii'))

def word(w):
  # 2 bytes
  return struct.pack('=h', w)

def dword(d):
  # 4 bytes
  return struct.pack('=l', d)

def color(r, g, b):
  # values from 0 to 1
  return bytes([ int(b*255), int(g*255), int(r*255) ])

BLACK = color(0, 0, 0)
WHITE = color(1, 1, 1)

V2 = namedtuple('Point2', ['x', 'y'])

class Renderer(object):
  # Constructor
  def __init__(self, width, height):
    self.curr_color = WHITE
    self.clear_color = BLACK
    self.glCreateWindow(width, height)

  def glCreateWindow(self, width, height):
    self.width = width
    self.height = height
    self.glClear()
    self.glViewPort(0, 0, width, height)

  def glViewPort(self, x, y, width, height):
    self.vpX = int(x) if x <= self.width else Exception('x is outside the window')
    self.vpY = int(y) if y <= self.height else Exception('y is outside the window')
    self.vpWidth = (width) if x + width <= self.width else Exception('viewport is outside the window')
    self.vpHeight = (height) if y + height <= self.height else Exception('viewport is outside the window')
    self.vpWidthMax = self.vpX + self.vpWidth
    self.vpHeightMax = self.vpY + self.vpHeight

  def glViewPortClear(self, color = None):
    for x in range(self.vpX, self.vpX + self.vpWidth):
      for y in range(self.vpY, self.vpY + self.vpHeight):
        self.glPoint(x, y, color)

  def glClearColor(self, r, g, b):
    self.clear_color = color(r, g, b)

  def glClear(self):
    # Creates a 2D pixels list and assigns a 3 bytes color for each value
    self.pixels = [ [self.clear_color for y in range(self.height)] for x in range(self.width) ]

  def glColor(self, r, g, b):
    self.curr_color = color(r, g, b)

  def glVertex(self, x, y, color = None):
    if x < -1 or x > 1:
      return

    if y < -1 or y > 1:
      return

    # Calculate pixel respect to viewport
    pixelX = int((x+1) * ((self.vpWidth-1) / 2) + self.vpX)
    pixelY = int((y+1) * ((self.vpHeight-1) / 2) + self.vpY)

    self.pixels[int(pixelX)][int(pixelY)] = color or self.curr_color

  def glPoint(self, x, y, color = None):
    # if the point is not in the viewport, don't draw it
    if (x < self.vpX) or (x >= self.vpWidthMax) or (y < self.vpY) or (y >= self.vpHeightMax):
      return
    
    if (0 <= x < self.width) and (0 <= y < self.height):
      self.pixels[int(x)][int(y)] = color or self.curr_color

  def glLine(self, vertex0, vertex1, color = None, NDC = False, buffer = None):
    x0 = int((vertex0.x + 1) * (self.vpWidth / 2) + self.vpX) if NDC else vertex0.x
    x1 = int((vertex1.x + 1) * (self.vpWidth / 2) + self.vpX) if NDC else vertex1.x
    y0 = int((vertex0.y + 1) * (self.vpHeight / 2) + self.vpY) if NDC else vertex0.y
    y1 = int((vertex1.y + 1) * (self.vpHeight / 2) + self.vpY) if NDC else vertex1.y

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    steep = dy > dx
    if steep:
      x0, y0 = y0, x0
      x1, y1 = y1, x1

    rightToLeft = x0 > x1
    if rightToLeft:
      x0, x1 = x1, x0
      y0, y1 = y1, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    if dx == 0:
      return
    offset = 0
    limit = 0.5
    m = dy/dx
    y = y0

    for x in range(x0, x1 + 1):
      if steep:
        if (buffer != None):
          buffer[y][x] = color or self.curr_color
        else:
          self.glPoint(y, x, color)
      else:
        if (buffer != None):
          buffer[x][y] = color or self.curr_color
        else:
          self.glPoint(x, y, color)

      offset += m
      if offset >= limit:
        y += 1 if y0 < y1 else -1
        limit += 1

    return buffer

  def glLoadModel(self, filename, translate = V2(0.0,0.0), scale = V2(1.0,1.0)):
    model = Obj(filename)
    for face in model.faces:
      vertCount = len(face)
      for vertex in range(vertCount):
        index0 = face[vertex][0] - 1
        index1 = face[(vertex+1) % vertCount][0] - 1
        vert0 = model.vertexes[index0]
        vert1 = model.vertexes[index1]
        x0 = int(vert0[0] * scale.x + translate.x)
        y0 = int(vert0[1] * scale.y + translate.y)
        x1 = int(vert1[0] * scale.x + translate.x)
        y1 = int(vert1[1] * scale.y + translate.y)
        self.glLine(V2(x0, y0), V2(x1, y1))

  def glLineInterceptor(self, buffer, width, height, left, bottom, points, colorFill, colorInterceptor):
    fill = False
    interceptions = 0
    newBuffer = buffer
    for y in range(1, height):
      for x in range(width):
        if (x == width-1):
          if (newBuffer[x][y] == colorInterceptor):
            interceptions += 1
        else:
          if (newBuffer[x][y] == colorInterceptor and newBuffer[x+1][y] == False):
            fill = not fill
            interceptions += 1
          if (fill):
            newBuffer[x][y] = colorFill

      if (interceptions < 2):
        for x in range(width-1):
          if (newBuffer[x][y] == colorFill):
            newBuffer[x][y] = False
      elif (interceptions % 3 == 0):
        fillTri = False
        notFillTri = False
        for x in range(1, width):
          if (newBuffer[x-1][y] == colorFill and newBuffer[x][y] == colorInterceptor and (x+left, y+bottom) in points):
            fillTri = True
            notFillTri = False
          if (newBuffer[x-1][y] == colorInterceptor and newBuffer[x][y] == colorFill and (x+left, y+bottom) in points):
            notFillTri = True
            fillTri = False
          if (fillTri):
            if (newBuffer[x-1][y] == colorFill and newBuffer[x][y] == colorFill and (x+left, y+bottom) not in points):
              notFillTri = True
              fillTri = False
            if (fillTri):
              newBuffer[x][y] = colorFill
          if (notFillTri):
            if (newBuffer[x-1][y] == False and newBuffer[x][y] == colorInterceptor):
              fillTri = True
              notFillTri = False
            else:
              newBuffer[x][y] = False

      fill = False
      interceptions = 0

    return newBuffer

  # fill a polygon from an array of points
  def glFillPolygon(self, points, colorBorder = None , colorFill = None):
    if colorBorder == None:
      colorBorder = self.curr_color
    if colorFill == None:
      colorFill = self.curr_color
    top = 0
    bottom = self.height
    left = self.width
    right = 0
    for i in range(len(points)):
      if points[i][0] < left:
        left = points[i][0]
      if points[i][0] > right:
        right = points[i][0]
      if points[i][1] > top:
        top = points[i][1]
      if points[i][1] < bottom:
        bottom = points[i][1]

    polygonHeight = top - bottom + 1
    polygonWidth = right - left + 1

    polygonBuffer = [ [False for y in range(polygonHeight)] for x in range(polygonWidth) ]

    for i in range(len(points)):
      if i == len(points) - 1:
        polygonBuffer = self.glLine(V2(points[i][0] - left, points[i][1] - bottom), V2(points[0][0] - left, points[0][1] - bottom), color=colorBorder, buffer=polygonBuffer)
      else:
        polygonBuffer = self.glLine(V2(points[i][0] - left, points[i][1] - bottom), V2(points[i+1][0] - left, points[i+1][1] - bottom), color=colorBorder, buffer=polygonBuffer)
    
    polygonBuffer = self.glLineInterceptor(polygonBuffer, polygonWidth, polygonHeight, left, bottom, points, colorFill=colorFill, colorInterceptor=colorBorder)

    for i in range(len(points)):
      if i == len(points) - 1:
        polygonBuffer = self.glLine(V2(points[i][0] - left, points[i][1] - bottom), V2(points[0][0] - left, points[0][1] - bottom), color=colorBorder, buffer=polygonBuffer)
      else:
        polygonBuffer = self.glLine(V2(points[i][0] - left, points[i][1] - bottom), V2(points[i+1][0] - left, points[i+1][1] - bottom), color=colorBorder, buffer=polygonBuffer)
    
    for x in range(polygonWidth):
      for y in range(polygonHeight):
        if (polygonBuffer[x][y] == colorFill and polygonBuffer[x][y-1] == False):
          polygonBuffer[x][y] = False
    
    for x in range(polygonWidth):
      for y in range(polygonHeight):
        if polygonBuffer[x][y] == colorBorder:
          self.glPoint(x+left, y+bottom, color=colorBorder)
        elif polygonBuffer[x][y] == colorFill:
          self.glPoint(x+left, y+bottom, color=colorFill)

  def glTriangle(self, A, B, C, color = None):
    self.glLine(A, B, color=color)
    self.glLine(B, C, color=color)
    self.glLine(C, A, color=color)

    if A.y < B.y:
      A, B = B, A
    if A.y < C.y:
      A, C = C, A
    if B.y < C.y:
      B, C = C, B

    def flatBottom(v1, v2, v3):
      d_v2_v1 = (v2.x - v1.x) / (v2.y - v1.y)
      d_v3_v1 = (v3.x - v1.x) / (v3.y - v1.y)

      x1 = v2.x
      x2 = v3.x

      for y in range(v2.y, v1.y + 1):
        self.glLine(V2(int(x1), y), V2(int(x2), y), color=color)
        x1 += d_v2_v1
        x2 += d_v3_v1

    def flatTop(v1, v2, v3):
      d_v3_v1 = (v3.x - v1.x) / (v3.y - v1.y)
      d_v3_v2 = (v3.x - v2.x) / (v3.y - v2.y)

      x1 = v3.x
      x2 = v2.x

      for y in range(v3.y, v1.y + 1):
        self.glLine(V2(int(x1), y), V2(int(x2), y), color=color)
        x1 += d_v3_v1
        x2 += d_v3_v2
    
    if B.y == C.y:
      # flat bottom
      flatBottom(A, B, C)
    elif A.y == B.y:
      # flat top
      flatTop(A, B, C)
    else:
      # Divide triangle and draw two triangles
      # teorema de intercepto
      D = V2(A.x + ((B.y - A.y) / (C.y - A.y)) * (C.x - A.x), B.y)
      flatBottom(A, B, D)
      flatTop(B, D, C)

  def glFinish(self, filename):
    # Creates a BMP file and fills it with the data inside self.pixels
    with open(filename, "wb") as file:
      # HEADER
      # Signature
      file.write(bytes('B'.encode('ascii')))
      file.write(bytes('M'.encode('ascii')))
      # FileSize in bytes
      file.write(dword(14 + 40 + (self.width * self.height * 3)))
      # Reserved
      file.write(dword(0)) # 0 = unused
      # DataOffset
      file.write(dword(14 + 40)) # from beginning of file to the beginning of bitmap data

      # INFO HEADER
      # Size
      file.write(dword(40)) # 40 = size of info header
      # Width
      file.write(dword(self.width))
      # Height
      file.write(dword(self.height))
      # Planes
      file.write(word(1)) # number of planes
      # Bits per pixel
      file.write(word(24)) # 24 = 24bit RGB. NumColors = 16M
      # Compression
      file.write(dword(0)) # 0 = BI_RGB no compression
      # ImageSize
      file.write(dword(self.width * self.height * 3))
      # XpixelsPerM
      file.write(dword(0))
      # YpixelsPerM
      file.write(dword(0))
      # Colors Used
      file.write(dword(0))
      # Important Colors
      file.write(dword(0)) # 0 = all

      # COLOR TABLE
      for y in range(self.height):
        for x in range(self.width):
          file.write(self.pixels[x][y])
