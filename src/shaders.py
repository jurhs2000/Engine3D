from src.glMath import cross, divide, dot, negative, norm, substract

def flat(render, **kwargs):
  u, v, w = kwargs['baryCoords']
  tA, tB, tC = kwargs['textureCoords']
  A, B, C = kwargs['vertices']
  b, g, r = kwargs['color']

  r = 1
  g = 1
  b = 1

  if render.active_texture:
    tx = tA[0] * u + tB[0] * v + tC[0] * w
    ty = tA[1] * u + tB[1] * v + tC[1] * w
    textureColor = render.active_texture.get_color(tx, ty)

    b *= textureColor[0] / 255
    g *= textureColor[1] / 255
    r *= textureColor[2] / 255

  normal = cross(substract(B,A), substract(C,A))
  normal = divide(normal, norm(normal))
  intensity = dot(normal, negative(render.direcional_light))

  b *= intensity
  g *= intensity
  r *= intensity

  if intensity > 0: return r, g, b
  else: return 0, 0, 0

def gourad(render, **kwargs):
  A, B, C = kwargs['vertices']
  u, v, w = kwargs['baryCoords']
  tA, tB, tC = kwargs['textureCoords']
  b, g, r = kwargs['color']
  nA, nB, nC = kwargs['normals']

  b /= 255
  g /= 255
  r /= 255

  dirLight = [0,0,0]
  dirLight[0] = -render.direcional_light[0]
  dirLight[1] = -render.direcional_light[1]
  dirLight[2] = -render.direcional_light[2]
  intensityA = dot(nA, dirLight)
  intensityB = dot(nB, dirLight)
  intensityC = dot(nC, dirLight)

  intensity = intensityA*u + intensityB*v + intensityC*w

  return r, g, b
