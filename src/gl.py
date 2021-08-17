# Graphics Library

from src.glTypes import V2, V3, V4, dword, newColor, word
from src.glMath import barycentricCoords, camTransform, createObjectMatrix, createRotationMatrix, dirTransform, divide, cross, dot, inv, negative, norm, substract, top, transformV3
from src.objLoader import Obj

BLACK = newColor(0, 0, 0)
WHITE = newColor(1, 1, 1)

class Renderer(object):
  # Constructor
  def __init__(self, width, height):
    self.curr_color = WHITE
    self.clear_color = BLACK
    self.glLookAt(V3(0,0,0), V3(0,0,-10))
    self.glCreateWindow(width, height)

    self.active_texture = None
    self.active_shader = None
    self.directional_light = V3(0,0,-1)

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

    self.viewportMatrix = [[width/2, 0, 0, x + width/2],
                          [0, height/2, 0, y + height/2],
                          [0, 0, 0.5, 0.5],
                          [0, 0, 0, 1]]

    self.glProjectionMatrix()

  def glViewPortClear(self, color = None):
    for x in range(self.vpX, self.vpX + self.vpWidth):
      for y in range(self.vpY, self.vpY + self.vpHeight):
        self.glPoint(x, y, color)

  def glClearColor(self, r, g, b):
    self.clear_color = newColor(r, g, b)

  def glClear(self):
    # Creates a 2D pixels list and assigns a 3 bytes color for each value
    self.pixels = [ [self.clear_color for y in range(self.height)] for x in range(self.width) ]
    
    self.zBuffer = [ [ float('inf') for y in range(self.height) ] for x in range(self.width) ]

  def glColor(self, r, g, b):
    self.curr_color = newColor(r, g, b)

  def glLookAt(self, eye, camPosition = V3(0,0,0), worldUp=V3(0,1,0)):
    forward = substract(camPosition, eye)
    forward = divide(forward, norm(forward))

    right = cross(worldUp, forward)
    right = divide(right, norm(right))

    up = cross(forward, right)
    up = divide(up, norm(up))

    camMatrix = [[right[0],up[0],forward[0],camPosition.x],
                [right[1],up[1],forward[1],camPosition.y],
                [right[2],up[2],forward[2],camPosition.z],
                [0,0,0,1]]

    self.viewMatrix = inv(camMatrix)

  def glProjectionMatrix(self, n = 0.1, f = 1000, fov = 60 ):
    t = top(fov, n)
    r = t * self.vpWidth / self.vpHeight

    self.projectionMatrix = [[n/r, 0, 0, 0],
                            [0, n/t, 0, 0],
                            [0, 0, -(f+n)/(f-n), -(2*f*n)/(f-n)],
                            [0, 0, -1, 0]]

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

  def glLoadModel(self, filename,
  translate = V3(0,0,0), scale = V3(1,1,1), light = V3(0,0,-1), rotate = V3(0,0,0)):
    model = Obj(filename)
    modelMatrix = createObjectMatrix(translate, scale, rotate)
    rotationMatrix = createRotationMatrix(rotate)

    light = divide(light, norm(light))

    total = len(model.faces)
    count = 0
    for face in model.faces:
      print(f'face {count}/{total}')
      vertCount = len(face)
      vertices = [None] * vertCount
      textureV = [None] * vertCount
      triangleV = [None] * vertCount
      normals = [None] * vertCount

      for i in range(vertCount):
        vertices[i] = model.vertices[face[i][0]-1]
        textureV[i] = model.textcoords[face[i][1]-1] if self.active_texture else 0
        triangleV[i] = transformV3(vertices[i], modelMatrix)
        normals[i] = dirTransform(model.normals[face[i][2]-1], rotationMatrix)

      # normal = cross(substract(triangleV[1], triangleV[0]), substract(triangleV[2], triangleV[0]))
      # if norm(normal) != 0:
      #   normal = divide(normal, norm(normal))
      # else:
      #   normal = V3(0.5, 0.5, 0.5)
      # intensity = dot(normal, negative(light))
      
      # if intensity > 1: intensity = 1
      # elif intensity < 0: intensity = 0

      for i in range(vertCount):
        triangleV[i] = camTransform(triangleV[i], self.viewportMatrix, self.projectionMatrix, self.viewMatrix)

      self.glTriangleBarycentric(triangleV[0],triangleV[1],triangleV[2],(textureV[0], textureV[1], textureV[2]),verts=(triangleV[0],triangleV[1],triangleV[2]), normals=(normals[0],normals[1],normals[2]))
      if vertCount == 4:
        self.glTriangleBarycentric(triangleV[0],triangleV[2],triangleV[3],(textureV[0], textureV[2], textureV[3]),verts=(triangleV[0],triangleV[2],triangleV[3]), normals=(normals[0],normals[2],normals[3]))
      count += 1

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

  def glTriangleStandard(self, A, B, C, color = None):
    if A.y < B.y:
      A, B = B, A
    if A.y < C.y:
      A, C = C, A
    if B.y < C.y:
      B, C = C, B

    def flatBottom(v1, v2, v3):
      try:
        d_v2_v1 = (v2.x - v1.x) / (v2.y - v1.y)
        d_v3_v1 = (v3.x - v1.x) / (v3.y - v1.y)
      except:
        pass
      else:
        x1 = v2.x
        x2 = v3.x
        for y in range(v2.y, v1.y + 1):
          self.glLine(V2(int(x1), y), V2(int(x2), y), color=color)
          x1 += d_v2_v1
          x2 += d_v3_v1

    def flatTop(v1, v2, v3):
      try:
        d_v3_v1 = (v3.x - v1.x) / (v3.y - v1.y)
        d_v3_v2 = (v3.x - v2.x) / (v3.y - v2.y)
      except:
        pass
      else:
        x1 = v3.x
        x2 = v3.x
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
    elif C.y == A.y:
      return # avoid division by zero
    else:
      # Divide triangle and draw two triangles
      # teorema de intercepto
      D = V2(A.x + ((B.y - A.y) / (C.y - A.y)) * (C.x - A.x), B.y)
      flatBottom(A, B, D)
      flatTop(B, D, C)

  def glTriangleBarycentric(self, A, B, C, textCoords = (), verts = (), normals = (), color = None):
    # Bounding box
    minX = round(min(A.x, B.x, C.x))
    minY = round(min(A.y, B.y, C.y))
    maxX = round(max(A.x, B.x, C.x))
    maxY = round(max(A.y, B.y, C.y))

    for x in range(minX, maxX + 1):
      for y in range(minY, maxY + 1):
        u, v, w = barycentricCoords(A, B, C, V2(x, y))
        if u >= 0 and v >= 0 and w >= 0:
          z = A.z * u + B.z * v + C.z * w
          # if self.active_texture:
          #   tA, tB, tC = textCoords
          #   tx = tA[0] * u + tB[0] * v + tC[0] * w
          #   ty = tA[1] * u + tB[1] * v + tC[1] * w
          #   color = self.active_texture.getColor(tx, ty)
          if 0 <= x < self.width and 0 <= y < self.height:
            if z < self.zBuffer[x][y] and z <= 1 and z >= -1:
              if self.active_shader:
                r, g, b = self.active_shader(self,
                                            verts=verts,
                                            baryCoords=(u,v,w),
                                            textCoords=textCoords,
                                            normals=normals,
                                            color = color or self.curr_color)
              else:
                b, g, r = color = self.curr_color
                b = b/255
                g = g/255
                r = r/255

              # self.glPoint(x, y, newColor(color[2] * intensity / 255,
              #                             color[1] * intensity / 255,
              #                             color[0] * intensity / 255))
              self.glPoint(x, y, newColor(r, g, b))
              self.zBuffer[x][y] = z
          # else:
          #   if 0 <= x < self.width and 0 <= y < self.height:
          #     if z < self.zBuffer[x][y] and z <= 1 and z >= -1:
          #       self.glPoint(x, y, newColor(intensity, intensity, intensity))
          #       self.zBuffer[x][y] = z

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
