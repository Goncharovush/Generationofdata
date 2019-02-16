import matplotlib.pyplot as plt
import numpy as np

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
coord=[]
for i in range(len(bord1)):
    for j in range(len(bord1[i])):
        bord[i][j]=max(bord1[i][j],bord2[i][j])
        if (bord[i][j]>0):
            coord.append([i,j])
def dist(a,b):
    return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])

groops=[]
"""while (len(coord)!=0):
    step = 0
    used = []
    first = coord[0]
    used.append(first)
    round = used[0]
    del coord[0]
    while True:
        if (step>1):
            coord.append(used[0])
            del used[0]
        def comparator(a):
            return dist(a, first)
        coord.sort(key=comparator)
        used.append(coord[0])
        first=coord[0]
        if (first==round):
            groops.append(used)
            break
        step=step+1
        del coord[0]
    if len(coord)==0:
        break"""
plt.imshow(bord)
plt.show()