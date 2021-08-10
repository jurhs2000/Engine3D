from glTypes import V3
import numpy as np

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

# TODO: implement self norm function
def norm(x):
  return np.linalg.norm(x)

# TODO: implement self cross function
def cross(x, y):
  return np.cross(x, y)

# TODO: implement substract function
def substract(x, y):
  return np.subtract(x, y)

# TODO: implement self dot function
def dot(x, y):
  return np.dot(x, y)
