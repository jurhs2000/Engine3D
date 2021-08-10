from src.glTypes import V3
from math import sqrt, pow

def barycentricCoords(A, B, C, P):
  try:
    # u for A = PCB/ABC
    u = (((B.y - C.y) * (P.x - C.x) + (C.x - B.x) * (P.y - C.y)) /
        ((B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)))
    # v for B = PCA/ABC
    v = (((C.y - A.y) * (P.x - C.x) + (A.x - C.x) * (P.y - C.y)) /
        ((B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)))
    # w for C
    w = 1 - u - v
  except:
    return -1, -1, -1
  return u, v, w

def transformV3(vertex, translate=V3(0,0,0), scale=V3(0,0,0)):
  return V3(vertex[0] * scale.x + translate.x,
            vertex[1] * scale.y + translate.y,
            vertex[2] * scale.z + translate.z)

def norm(x):
  xnorm = sqrt(pow(x.x, 2) + pow(x.y, 2) + pow(x.z, 2))
  return xnorm

def divide(v3, d):
  if d != 0:
    divided = V3(v3.x / d, v3.y / d, v3.z / d)
    return divided
  else:
    print('division by zero')
    return V3(0, 0, 0)

def cross(a, b):
  axb = V3(a[1] * b[2] - a[2] * b[1],
         a[2] * b[0] - a[0] * b[2],
         a[0] * b[1] - a[1] * b[0])
  return axb

def substract(x, y):
  return V3(x.x - y.x, x.y - y.y, x.z - y.z)

def negative(x):
  return V3(-x.x, -x.y, -x.z)

def dot(x, y):
  xdy = (x.x * y.x) + (x.y * y.y) + (x.z * y.z)
  return xdy
