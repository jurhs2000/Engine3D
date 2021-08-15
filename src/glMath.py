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
    transVertex = viewMatrix @ augVertex
  else:
    transVertex = viewportMatrix @ projectionMatrix @ viewMatrix @ augVertex
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

def createObjectMatrix(translate, scale, rotate):
  translateMatrix = np.matrix([[1,0,0,translate.x],
                                [0,1,0,translate.y],
                                [0,0,1,translate.z],
                                [0,0,0,1]])

  scaleMatrix = np.matrix([[scale.x,0,0,0],
                            [0,scale.y,0,0],
                            [0,0,scale.z,0],
                            [0,0,0,1]])

  rotationMatrix = createRotationMatrix(rotate)

  return translateMatrix * rotationMatrix * scaleMatrix

def createRotationMatrix(rotate):
  pitch = np.deg2rad(rotate.x)
  yaw = np.deg2rad(rotate.y)
  roll = np.deg2rad(rotate.z)

  rotationX = np.matrix([[1,0,0,0],
                          [0,np.cos(pitch),-np.sin(pitch),0],
                          [0,np.sin(pitch),np.cos(pitch),0],
                          [0,0,0,1]])

  rotationY = np.matrix([[np.cos(yaw),0,np.sin(yaw),0],
                          [0,1,0,0],
                          [-np.sin(yaw),0,np.cos(yaw),0],
                          [0,0,0,1]])

  rotationZ = np.matrix([[np.cos(roll),-np.sin(roll),0,0],
                          [np.sin(roll),np.cos(roll),0,0],
                          [0,0,1,0],
                          [0,0,0,1]])

  return rotationX * rotationY * rotationZ
