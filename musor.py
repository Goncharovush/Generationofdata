#import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
X = np.arange(0, 100, 0.1)
Y = np.arange(0, 100, 0.1)

XX, YY = np.meshgrid(X, Y)
data = np.zeros(XX.shape)

for i in range(100):
    a, b = np.random.uniform(low=0, high=100, size=2)
    std_1, std_2 = np.random.uniform(low=0, high=50, size=2)

    data = data + np.exp(-(XX - a) ** 2 / std_1 - (YY - b) ** 2 / std_2)
d = data
d[np.where(data > 1e0)] = 1
d[np.where(data < 1e0)] = 0
bord1=np.zeros(d.shape)
bord=np.zeros(d.shape)
bord2=np.zeros(d.shape)
for j in range(len(d)-1):
    bord1[j+1]=d[j+1]-d[j]
d=d.transpose()
for j in range(len(d)-1):
    bord2[j+1]=d[j+1]-d[j]
bord2=bord2.transpose()
bord1[np.where(bord1 != 0.0)] = 1
bord1[np.where(bord1 == 0.0)] = 0
bord2[np.where(bord2 != 0.0)] = 1
bord2[np.where(bord2 == 0.0)] = 0
for i in range(len(bord1)):
    for j in range(len(bord1[i])):
        bord[i][j]=max(bord1[i][j],bord2[i][j],0.5*data[i][j])
array = np.zeros([256, 256, 3], dtype=np.uint8)
for i in range(1000):
    for j in range(1000):
        if (bord[i][j] == 1.0):
            array[i:,j:]=[0., 0., 0.]
        elif (bord[i][j]==0.5):
            array[i:, j:] = [bord[i][j], 255, 0]
        else:
            array[i:, j:] = [121, 0, bord[i][j]]
img = Image.fromarray(array)
img.save('image.png')