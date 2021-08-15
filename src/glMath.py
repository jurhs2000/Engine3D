from src.glTypes import V3, V4
from math import sqrt, pow
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

def baseTransform(vertex, viewMatrix, viewportMatrix=None, projectionMatrix=None):
  augVertex = V4(vertex[0], vertex[1], vertex[2], 1)
  if viewportMatrix is None:
    transVertex = np.matrix(viewMatrix) @ augVertex
  else:
    transVertex = np.matrix(viewportMatrix) @ np.matrix(projectionMatrix) @ np.matrix(viewMatrix) @ augVertex
  transVertex = transVertex.tolist()[0]

  transVertex = V3(transVertex[0] / transVertex[3],
                    transVertex[1] / transVertex[3],
                    transVertex[2] / transVertex[3])

  return transVertex

def transformV3(vertex, vMatrix):
  return baseTransform(vertex, vMatrix)

def camTransform(vertex, viewportMatrix, projectionMatrix, viewMatrix):
  return baseTransform(vertex, viewMatrix, viewportMatrix, projectionMatrix)

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

def matrixMult(matrixA, matrixB):
  product = [ [] for x in range(len(matrixA)) ]
  for i in range(len(matrixA)):
    for j in range(len(matrixA)):
      element = 0
      for n in range(len(matrixA)):
        element += matrixA[i][n] * matrixB[n][j]
      product[i].append(element)
  return product

def createObjectMatrix(translate, scale, rotate):
  translateMatrix = [[1,0,0,translate.x],
                    [0,1,0,translate.y],
                    [0,0,1,translate.z],
                    [0,0,0,1]]

  scaleMatrix = [[scale.x,0,0,0],
                [0,scale.y,0,0],
                [0,0,scale.z,0],
                [0,0,0,1]]

  rotationMatrix = createRotationMatrix(rotate)

  return matrixMult(matrixMult(translateMatrix, rotationMatrix), scaleMatrix)

def createRotationMatrix(rotate):
  pitch = np.deg2rad(rotate.x)
  yaw = np.deg2rad(rotate.y)
  roll = np.deg2rad(rotate.z)

  rotationX = [[1,0,0,0],
              [0,np.cos(pitch),-np.sin(pitch),0],
              [0,np.sin(pitch),np.cos(pitch),0],
              [0,0,0,1]]

  rotationY = [[np.cos(yaw),0,np.sin(yaw),0],
              [0,1,0,0],
              [-np.sin(yaw),0,np.cos(yaw),0],
              [0,0,0,1]]

  rotationZ = [[np.cos(roll),-np.sin(roll),0,0],
              [np.sin(roll),np.cos(roll),0,0],
              [0,0,1,0],
              [0,0,0,1]]

  return matrixMult(matrixMult(rotationX, rotationY), rotationZ)

def top(fov, n):
  return np.tan((fov * np.pi / 180) / 2) * n

# determinant of matrix without numpy
# inspired by https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy
def inv(x):
  detX = det(x)
  cofactors = []
  for i in range(len(x)):
    cofactorRow = []
    for j in range(len(x)):
      minor = matrixMinor(x, i, j)
      cofactorRow.append(((-1)**(i + j)) * det(minor))
    cofactors.append(cofactorRow)
  cofactors = transpose(cofactors)
  for i in range(len(cofactors)):
    for j in range(len(cofactors)):
      cofactors[i][j] = cofactors[i][j] / detX
  return cofactors

def det(x):
  if len(x) == 2:
    return x[0][0] * x[1][1] - x[0][1] * x[1][0]
  else:
    determinant = 0
    for i in range(len(x)):
      determinant += ((-1)**i) * det(matrixMinor(x, 0, i)) * x[0][i]
    return determinant

def matrixMinor(matrix, i, j):
  return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def transpose(x):
  xt = [ [None]*len(x) for i in range(len(x[0])) ]
  for i in range(len(x[0])):
    for j in range(len(x)):
      xt[i][j] = x[j][i]
  return xt