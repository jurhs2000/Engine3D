from math import cos, inf
from random import uniform, random
from src.glTypes import V3, newColor
from src.glMath import angle, cross, divide, dot, negative, norm, substract

def flat(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  tA, tB, tC = kwargs['textureCoords']
  A, B, C = kwargs['vertices']
  b, g, r = kwargs['color']
  triangleNormal = kwargs['triangleNormal']

  b/=255
  g/=255
  r/=255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  intensity = dot(triangleNormal, negative(render.directional_light))

  b *= intensity
  g *= intensity
  r *= intensity

  if intensity > 0: return r, g, b
  else: return 0, 0, 0

def gourad(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  nA, nB, nC = kwargs['normals']

  b /= 255
  g /= 255
  r /= 255

  intensityA = dot(nA, negative(render.directional_light))
  intensityB = dot(nB, negative(render.directional_light))
  intensityC = dot(nC, negative(render.directional_light))

  intensity = intensityA*u + intensityB*v + intensityC*w
  b *= intensity
  g *= intensity
  r *= intensity

  if intensity > 0:
    return r, g, b
  else:
    return 0, 0, 0

def phong(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']

  b /= 255
  g /= 255
  r /= 255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))

  b = b*intensity if b*intensity <=1 else 1
  g = g*intensity if g*intensity <=1 else 1
  r = r*intensity if r*intensity <=1 else 1

  if intensity > 0:
    return r, g, b
  else:
    return 0, 0, 0

def unlit(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']

  b /= 255
  g /= 255
  r /= 255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  return r, g, b

def toon(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']

  b /= 255
  g /= 255
  r /= 255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))

  if intensity > 0.9:
    intensity = 1
  elif intensity > 0.6:
    intensity = 0.6
  elif intensity > 0.2:
    intensity = 0.4
  else:
    intensity = 0.2

  b *= intensity
  g *= intensity
  r *= intensity

  if intensity > 0:
    return r, g, b
  else:
    return 0, 0, 0

def coolShader(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  nA, nB, nC = kwargs['normals']

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))

  r, g, b = (0,0,0)

  if intensity > 0.7:
    r = 1
  elif intensity > 0.3:
    r = 0.5
    b = 0.5
  else:
    b = 1

  return r, g, b

def textureBlend(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']

  b /= 255
  g /= 255
  r /= 255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))

  if intensity < 0:
    intensity = 0

  b *= intensity
  g *= intensity
  r *= intensity

  if render.active_texture2:
    textureColor = render.active_texture2.getColor(tx, ty)
    b += (textureColor[0] / 255) * (1 - intensity)
    g += (textureColor[1] / 255) * (1 - intensity)
    r += (textureColor[2] / 255) * (1 - intensity)

  return r, g, b

def gradient(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  nA, nB, nC = kwargs['normals']
  A, B, C = kwargs['vertices']
  upColor = kwargs['upColor']
  downColor = kwargs['downColor']

  y = A[1] * u + B[1] * v + C[1] * w
  height = render.maxY - render.minY
  b = (((y+abs(render.minY)) / height) * (upColor[0] - downColor[0]) + downColor[0]) / 255
  g = (((y+abs(render.minY)) / height) * (upColor[1] - downColor[1]) + downColor[1]) / 255
  r = (((y+abs(render.minY)) / height) * (upColor[2] - downColor[2]) + downColor[2]) / 255

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))

  b = b*intensity if b*intensity <=1 else 1
  g = g*intensity if g*intensity <=1 else 1
  r = r*intensity if r*intensity <=1 else 1

  if intensity > 0:
    return r, g, b
  else:
    return 0, 0, 0

def highlighter(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']
  color = kwargs['highColor']

  b /= 255
  g /= 255
  r /= 255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))
  b = b*intensity
  g = g*intensity
  r = r*intensity

  forwardVector = V3(render.camMatrix[0][2], render.camMatrix[1][2], render.camMatrix[2][2])
  parallel = dot(normal, forwardVector)
  b = color[0]/255 * (1 - parallel) if color[0]/255 * (1 - parallel)>b else b
  g = color[1]/255 * (1 - parallel) if color[1]/255 * (1 - parallel)>g else g
  r = color[2]/255 * (1 - parallel) if color[2]/255 * (1 - parallel)>r else r
  b = float(abs(b*(1-pow((intensity+1),-10))))
  g = float(abs(g*(1-pow((intensity+1),-10))))
  r = float(abs(r*(1-pow((intensity+1),-10))))

  b = b if b <=1 else 1
  g = g if g <=1 else 1
  r = r if r <=1 else 1

  if intensity > 0:
    return r, g, b
  else:
    return 0, 0, 0

def cut(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']
  v1, v2, v3 = kwargs['originalVertices']
  axis = kwargs['axis']
  interval = kwargs['interval']

  if axis == 'x':
    direction = v1[0] * u + v2[0] * v + v3[0] * w
  elif axis == 'y':
    direction = v1[1] * u + v2[1] * v + v3[1] * w
  elif axis == 'z':
    direction = v1[2] * u + v2[2] * v + v3[2] * w
  else:
    direction = v1[1] * u + v2[1] * v + v3[1] * w

  if cos(direction*interval) >=0: 

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
      tx = tA[0] * u + tB[0] * v + tC[0] * w
      ty = tA[1] * u + tB[1] * v + tC[1] * w
      textureColor = render.active_texture.getColor(tx, ty)
      b *= textureColor[0] / 255
      g *= textureColor[1] / 255
      r *= textureColor[2] / 255

    nX = nA[0] * u + nB[0] * v + nC[0] * w
    nY = nA[1] * u + nB[1] * v + nC[1] * w
    nZ = nA[2] * u + nB[2] * v + nC[2] * w

    normal = V3(nX, nY, nZ)
    intensity = dot(normal, negative(render.directional_light))

    b = b*intensity if b*intensity <=1 else 1
    g = g*intensity if g*intensity <=1 else 1
    r = r*intensity if r*intensity <=1 else 1
  else :
    b = 0
    g = 0
    r = 0
  b = b if b <=1 else 1
  g = g if g <=1 else 1
  r = r if r <=1 else 1
  b = b if b >=0 else 0
  g = g if g >=0 else 0
  r = r if r >=0 else 0
  return r, g, b

def noise(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']

  b /= 255
  g /= 255
  r /= 255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))

  b = random() * b
  g = random() * g
  r = random() * r
  b = b*intensity if b*intensity <=1 else 1
  g = g*intensity if g*intensity <=1 else 1
  r = r*intensity if r*intensity <=1 else 1

  if intensity > 0:
    return r, g, b
  else:
    return 0, 0, 0

def outline(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']
  color = kwargs['highColor']

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)

  forwardVector = V3(render.camMatrix[0][2], render.camMatrix[1][2], render.camMatrix[2][2])
  parallel = dot(normal, forwardVector)
  if parallel < 0.3:
    b = color[0]/255 * (1 - parallel)
    g = color[1]/255 * (1 - parallel)
    r = color[2]/255 * (1 - parallel)
  else:
    b = 0
    g = 0
    r = 0

  b = b if b <=1 else 1
  g = g if g <=1 else 1
  r = r if r <=1 else 1

  return r, g, b

def snow(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']
  A, B, C = kwargs['vertices']
  color = newColor(1,1,1)

  b /= 255
  g /= 255
  r /= 255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))
  b = b*intensity
  g = g*intensity
  r = r*intensity

  forwardVector = V3(0,-1,1)
  parallel = dot(normal, forwardVector)
  b = color[0]/255 * (1 - parallel) if color[0]/255 * (1 - parallel)>b else b
  g = color[1]/255 * (1 - parallel) if color[1]/255 * (1 - parallel)>g else g
  r = color[2]/255 * (1 - parallel) if color[2]/255 * (1 - parallel)>r else r
  b = float(abs(b*(1-pow((intensity+1),-10))))
  g = float(abs(g*(1-pow((intensity+1),-10))))
  r = float(abs(r*(1-pow((intensity+1),-10))))

  b = b if b <=1 else 1
  g = g if g <=1 else 1
  r = r if r <=1 else 1

  if intensity > 0:
    return r, g, b
  else:
    return 0, 0, 0

def accentuate(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  b, g, r = kwargs['color']
  tA, tB, tC = kwargs['textureCoords']
  nA, nB, nC = kwargs['normals']
  color = kwargs['highColor']

  b /= 255
  g /= 255
  r /= 255

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.getColor(tx, ty)
    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  nX = nA[0] * u + nB[0] * v + nC[0] * w
  nY = nA[1] * u + nB[1] * v + nC[1] * w
  nZ = nA[2] * u + nB[2] * v + nC[2] * w

  normal = V3(nX, nY, nZ)
  intensity = dot(normal, negative(render.directional_light))

  b = color[0]/255 if color[0]/255 > b else b
  g = color[1]/255 if color[1]/255 > g else g
  r = color[2]/255 if color[2]/255 > r else r

  b = b*intensity if b*intensity <=1 else 1
  g = g*intensity if g*intensity <=1 else 1
  r = r*intensity if r*intensity <=1 else 1

  if intensity > 0:
    return r, g, b
  else:
    return 0, 0, 0
