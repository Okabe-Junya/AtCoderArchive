import numpy as np

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

a = np.array([Ax, Ay])
b = np.array([Bx, By])
c = np.array([Cx, Cy])
d = np.array([Dx, Dy])

vecab = b - a
vecbc = c - b
veccd = d - c
vecda = a - d

sina = np.cross(vecab, vecbc) / (np.linalg.norm(vecab) * np.linalg.norm(vecbc))
sinb = np.cross(vecbc, veccd) / (np.linalg.norm(vecbc) * np.linalg.norm(veccd))
sinc = np.cross(veccd, vecda) / (np.linalg.norm(veccd) * np.linalg.norm(vecda))
sind = np.cross(vecda, vecab) / (np.linalg.norm(vecda) * np.linalg.norm(vecab))
if sina <= 0 or sinb <= 0 or sinc <= 0 or sind <= 0:
    print('No')
else:
    print('Yes')
