##pip install matplotlib

## plot dari list
## bar
## fill_between
## yticks/xticks
## legend
## title
## ylim
## legend
'''
plt.plot
'''
import matplotlib.pyplot as plt
import numpy as np
a=np.array([1,2,3,4])
# #b=np.array([2,5,7,4])
# # a=[1,2,3,4]
# # b=[2,5,7,4]
# #plt.plot(a,b,'ro') #red circle
# # plt.plot(a,b,b,a) # x=a,y=b;x=b,y=a
# # plt.plot(a,a,a,a**2,a,a**3)
# # plt.plot(a,a,'g--',a,a,'g*',a,a**2,'r--',a,a**3,'g^',a,a**3,'y--')
# ###
# plt.plot(a,a**3) 
# plt.fill_between(a,a**3,facecolor='r',alpha=0.3) #diisi bagian bawah
# plt.fill_between(a,a**3,205,facecolor='r',alpha=0.3) #batas atas 205 jadi diisi ke atas a, agak merah transparan
# plt.show()
#==================================================================
# plt.figure()
# plt.plot(a,a)
# plt.fill_between(a,a[1],facecolor='r',alpha=0.3) #a[1]=2 batas atas, bentuk persegi, di bawah 2
# plt.fill_between(a,a,a[3],facecolor='r',alpha=0.3) #a[3]=4, batas atas, diisi yang atas a
# plt.fill_between(a,0,a,facecolor='r',alpha=0.3) #0=batas bawah, yang diisi yang bawah a
# plt.fill_between(a,a[2],a,facecolor='r',alpha=0.3) #a[3]=3, batasnya 3 isi diatas dan dibawah
# plt.title('Tes doang')
# # plt.xlabel('Nilai x')
# # plt.ylabel('Nilai y',fontsize=8)
# # plt.grid(True,color='red',linestyle='--')
# # #plt.legend(['axa','axaa','axaaa'])
#plt.subplots_adjust(left=0.35,bottom=0.2,right=0.95,top=0.9,wspace=0.2,hspace=0.2) #hspace jeda tinggi sama subplot lain, wspace jeda lebar
# plt.show()

'''
soal 3x+2y=12, dimana titik potong pada sumbu x dan sumbu y
'''
#==================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# a=np.array([[3]]) #harus dua dimensi variablenya
# b=np.array([[2]]) #harus dua dimensi variablenya
# c=np.array([12])
# x=np.linalg.solve(a,c) #y=0 
# y=np.linalg.solve(b,c) #x=0
# print(x)
# print(y)
# titika=np.array([x[0],0])
# titikb=np.array([0,y[0]])
# titikx=np.array([0,1])
# titiky=np.array([-1,8])
# print(titika)
# print(titikb)
# plt.plot(titika,titikb,'r-',titikx,titiky,'b--')
# plt.grid(True)
# plt.show()

'''
sinus
'''
#==================================================================
'''
degree
cos(degree*np.pi/180)
cos(radian)
'''
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.arange(0,3*np.pi,0.1) #start,stop
# y=np.sin(x) #radian
# z=np.cos(x) #radian
# w=np.tan(x) #radian
# plt.plot(x,y,'r--',x,z,'g--',x,w,'b--')
# plt.grid(True)
# plt.title('Grafik Trigonometri')
# plt.legend(['sinus','cos','tan'])
# plt.show()

'''
bar
'''
#==================================================================
# import matplotlib.pyplot as plt
# w=['A','B','C','D','E']
# x=[2.6,3,8,5]
# y=[2,6,3,8,5]
# z=[1,3,5,7,9]
# plt.bar(w,y, color='g') #nama dan jumlah
# plt.plot(w,y,'r')
# plt.fill_between(w,y,facecolor='b')
# plt.show()
'''
plot bar
'''
#==================================================================
# import csv
# import numpy as np
# import matplotlib.pyplot as plt
# with open('rokok.csv','r') as fileq:
#     reader=csv.reader(fileq)
#     lokasi=[]
#     r15=[]
#     r16=[]
## list dalam list
#     for x in reader:
#         lokasi.append(x[0])
#         r15.append(float(x[1]))
#         r16.append(float(x[2]))
# r15=r15[1:]
# r16=r16[1:]
# lokasi=lokasi[1:]
# plt.bar(lokasi,r15)
# plt.bar(lokasi,r16)
# plt.xticks(rotation=90)
# plt.yticks(np.arange(0,35,5))#or np.arange(0,35,step=5) #arange bikin deret berdasarkan step
# plt.legend(['%perokok 2015','%perokok 2016'])
# plt.show()
'''
plot lebih dari rata2 aja
'''
#==================================================================
# import csv
# import numpy as np
# import matplotlib.pyplot as plt
# with open('rokok.csv','r') as fileq:
#     reader=csv.reader(fileq)
#     lokasi=[]
#     r15=[]
#     r16=[]
# ## list dalam list
#     for x in reader:
#         lokasi.append(x[0])
#         r15.append(float(x[1]))
#         r16.append(float(x[2]))
# r15=r15[1:]
# r16=r16[1:]
# lokasi=lokasi[1:]
# m15=np.mean(r15)
# m16=np.mean(r16)
# print(m15)
# print(m16)
# h15=[]
# h16=[]
# d15=[]
# d16=[]
# for i in range(len(r15)):
#     if r15[i]> m15:
#         d15.append(r15[i])
#         h15.append(i)

# for ci in range (len(r16)):
#     if r16[ci]>m16:
#         d16.append(r16[ci])
#         h16.append(ci)
# l15=[]
# l16=[]
# for ai in range(len(lokasi)):
#     for xa in range(len(h15)):
#         if ai==h15[xa]:
#             l15.append(lokasi[ai])
# for bi in range(len(lokasi)):
#     for xb in range(len(h16)):
#         if bi ==h16[xb]:
#             l16.append(lokasi[bi])
# print(len(l15))
# print(len(l16))
# plt.bar(l15,d15)
# plt.bar(l16,d16)
# plt.xticks(rotation=90)
# plt.yticks(np.arange(0,35,5))#or np.arange(0,35,step=5) #arange bikin deret berdasarkan step
# plt.legend(['%perokok 2015','%perokok 2016'])
# plt.show()


#==================================================================
# import csv
# import numpy as np
# import matplotlib.pyplot as plt
# with open('rokok.csv','r') as fileq:
#     reader=csv.reader(fileq)
#     lokasi=[]
#     r15=[]
#     r16=[]
#     for x in reader:
#         lokasi.append(x[0])
#         r15.append(float(x[1]))
#         r16.append(float(x[2]))
# r15=r15[1:]
# r16=r16[1:]
# lokasi=lokasi[1:]
# m15=np.mean(r15)
# m16=np.mean(r16)
# print(m15)
# print(m16)
# d15=[]
# d16=[]
# l15=[]
# l16=[]
# for i in range(len(r15)):
#     if r15[i]> m15 and r16[i]>m16:
#         d15.append(r15[i])
#         d16.append(r16[i])
#         l15.append(lokasi[i])
#         l16.append(lokasi[i])
# print(len(l15))
# plt.bar(l15,d15,color='b')
# plt.bar(l16,d16,color='orange')
# a15=np.linspace(m15,m15,len(l15))
# a16=np.linspace(m16,m16,len(l16))
# #plt.axhline(y=m15) #sepanjang dari sumbu sampai mentok
# #plt.plot(l15,[m15]*len(l15),'r-')
# plt.plot([0,len(l15)-1],[m15,m15])
# #plt.plot(l15,np.repeat(m15,len(l15)),lw=5)
# #plt.plot(l16,a16,lw=5)
# plt.xticks(rotation=90)
# #plt.yticks(np.arange(0,35,5))#or np.arange(0,35,step=5) #arange bikin deret berdasarkan step
# plt.ylim((25,35))
# plt.legend(['%perokok 2015','%perokok 2016'],loc=3) #([...],loc=3) atau 2
# plt.title('Perbandingan perokok')
# plt.show()

