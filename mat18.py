## scatter
## pie
## 2 bars, 2 lines
## style.use
## annotate
## axes3d
## image
## bar3d
## hist

## 2 bars, 2 lines
#==================================================================
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(10)
y=np.arange(0,20,2)
z=np.arange(21,1,-2)
# plt.figure(1)
# plt.plot(x,y,'r-')
plt.bar(x,y,color='yellow',yerr=0.5, bottom=z)
# #bottom = to create a stacked bar chart=to break down or compare parts of a whole,bandingin dgn chart lain,kebalik diatas plot barnya
# #yerr=error bar, y axis
# plt.plot(x,z,'b-')
# plt.bar(x,z)
# #plt.xticks(x)
# plt.grid(True)
# # plt.figure(2)
# # plt.plot(x,y,'r-')
# # plt.bar(x,y,color='yellow',bottom=z)
# # #bottom = to create a stacked bar chart=to break down or compare parts of a whole
# # plt.plot(x,z,'b-')
# # plt.bar(x,z)
# # #plt.xticks(x)
# # plt.grid(True)
plt.show()

## Scatter plot
#==================================================================
# plt.scatter(x,y,marker='*',s=300) #s=size scatter, by default bulat
# plt.xticks(x)
# plt.grid(True)
# plt.show()

## Pie chart
#==================================================================
# slice= [8,4,8,4] #menunjukkan proporsi data, contoh makan 4 jam
# aktivitas=['Tidur','Makan','Bekerja','Olahraga']
# x=np.array([0,1,2,3])
# plt.pie(slice,labels=aktivitas,explode=(0,0.2,0,0.4),startangle=90,shadow=True,colors=['r','g','y','k'])
# #shadow=bayangan
# #startangle=dirotate
# #explode=dipotong/cabut slicenya, 0=tidak kecabut
# plt.plot(x,x**2)
# plt.show()

## STYLE
#==================================================================
# from matplotlib import style
# #bisa dicari melalui syntax
# print(plt.style.available)
# #cara gunain style menggunakan syntax style.use('nama style')
# style.use('dark_background')
# plt.bar(x,y,color='yellow')
# plt.plot(x,y,'b-')
# plt.grid(True)

# #Menambahkan data labels: plt.text(x?, y?, teks apa?)
# for i in x:
#     plt.text(i-.1 , y[i] + .5, y[i]) #letak label bisa diatur dengan menambahkan atau mengurangi posisi x dan y teksnya.

# #Memberikan anotasi/catatan pada salah satu data
# plt.annotate(
# 'Ini tertinggi',
# xy = (x[len(x)-1],18), target ditunjuk
# xytext = (5,21), #teks di sesuai sumbu
# arrowprops = dict(facecolor = 'red', shrink = .2) #semakin kecil bagus bentuk arrownya
# #arrowprops = dict(arrowstyle = 'wedge') #segi3,syntax arrowstyle tidak bisa dibarengi dengan shrink
# )
# plt.show()

## Window figure
#==================================================================
# plt.figure('Hello',figsize=(8,8)) #figsize lebar window
# ## Split window figure menjadi beberapa bagian
# plt.subplot(2,2,1)
# plt.bar(x,x,color='green')
# plt.subplot(2,2,2)
# plt.plot(x,x**2,'r--')
# plt.subplot(2,2,3)
# plt.scatter(x,x**3,s=150)
# plt.subplot(2,2,4)
# plt.pie([4,4,4,4],labels=['A','B','C','D'])
# plt.suptitle('Bikin 4 grafik dalam 1 figure')
# plt.show()

## MATPLOTLIB IMAGE
#==================================================================
# import matplotlib.image as mpimg
# # file yg direkomendasikan png
# gambar=mpimg.imread('sun.png',0) #run the 0 image/1st image
# #xgbr=gambar[:,:,1] #R, 2G 3B
# c=np.arange(250)
# plt.imshow(gambar)
# #plt.imshow(xgbr,cmap='jet') #'hot'
# plt.plot(c,c,'r-')
# #plt.colorbar()
# plt.show()

## 3D plotting
#==================================================================
# from mpl_toolkits.mplot3d import axes3d
# plt.figure('3D Plotting')
# #i=plt.subplot(221, projection='3d')
# #i=plt.subplot2grid(221)
# i=plt.subplot2grid((2,2),(1,0),projection='3d')
# x=np.arange(10)
# y=np.arange(10)
# z=np.array([x])
# xn=np.arange(10,0,-1)
# yn=np.arange(10,0,-1)
# zn=np.array([xn])
# i.plot_wireframe(x,y,z)
# i.plot_wireframe(xn,yn,zn)
# i.scatter(x,y,z,color='red',marker='*',s=200)
# plt.show()

## 3D bar
#==================================================================
# xalas=np.arange(10)
# #yalas=np.arange(10)
# #zalas=np.arange(10,0,-1)
# yalas=np.ones(10)
# zalas=np.zeros(10)
# xdinding=np.ones(10) #ones selebar x, zeros cuma garis aja, selebar y.
# ydinding=np.ones(10)
# zdinding=np.arange(10)
# i.bar3d(xalas,yalas,zalas,xdinding,ydinding,zdinding)
# i.set_xlabel('ini x')
# i.set_ylabel('ini y')
# i.set_zlabel('ini z')
# plt.show()

## Histogram
#==================================================================
# m=[1,1,2,2,2,3,3,3,3,4,4,4,4,5,1,0]
# plt.hist(m,bins=5)
# plt.show()