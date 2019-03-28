## ANIMASI
##ROKOK BAR CHART


import matplotlib.pyplot as plt
import numpy as np

#==================================================================
##MENGGUNAKAN PACKAGE ANIMASI MATPLOTLIB
#Memanggil package animasi
import matplotlib.animation as anim

fig = plt.figure('Tes Animasi')
i = fig.add_subplot(1,1,1)

def grafik(s):
    x = []
    y = []
    data = open('28f.csv', 'r').read()
    baris = data.split('\n')
    for n in baris:
        a, b = n.split(',')
        x.append(a)
        y.append(b)
    i.clear() #gapake jd warna-warni
    i.plot(x,y)

run = anim.FuncAnimation(fig, grafik, interval = 1000) # interval 1000 = 1 sekon

plt.show()
## Ganti-ganti file csvnya, nanti otomatis ke-update

#==================================================================
## Rokok - bar chart
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

fig=plt.figure('Presentase Perokok Per Provinsi')
i=plt.subplot(111, projection='3d')
prov=[]
r15=[]
r16=[]
with open('rokok.csv','r') as fileku:
    reader=csv.reader(fileku)
    for x in reader:
        prov.append(x[0])
        r15.append(float(x[1]))
        r16.append(float(x[2]))
prov.remove(prov[0])
r15.remove(r15[0])
r16.remove(r16[0])
#==================================================================
## 3D bar graph
# xalas=np.arange(1,35,1)
# yalas=np.ones(34)
# zalas=np.zeros(34)
# xdinding=np.repeat(.5,34)
# ydinding=np.repeat(.5,34)
# xalas16=np.arange(1,35,1)
# yalas16=np.repeat(2,34)
# i.bar3d(xalas,yalas,zalas,xdinding,ydinding,r15)
# i.bar3d(xalas16,yalas16,zalas,xdinding,ydinding,r16)
# plt.xticks(xalas,prov,rotation=90)
# i.annotate('Provinsi', xy=(0, 0), ha='left', va='bottom', xycoords='axes fraction', fontsize=10)
# ##xy float
# ##i.set_xlabel('Provinsi')
# i.set_ylabel('Y')
# i.set_zlabel('Presentase Rokok')
# plt.show()