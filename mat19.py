## BUAT BAR&PLOT
## subplot2grid
## spines
## tick_params
## axhline
## axvline

import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(1,10,1)
# y = np.array([1, 4, 9, 3, 5, 8, 4, 10, 9])

# # i = plt.subplot2grid(shape, lokasi), eg:
# #i = plt.subplot2grid((2,2), (1,0)) #(2,2) artinya shape figure dibagi 2 baris dan 2 kolom | (1,0) lokasinya di kotak baris kesatu (bawah) kolom ke 0 (kiri) | lokasi tidak bisa lebih dari sama dengan shape nya.
# i=plt.subplot2grid((1,1),(0,0))
# i.plot(x,y, 'r--', linewidth = 2)
# i.bar(x,y, color = 'yellow')

# i.spines['left'].set_color('r')
# i.spines['left'].set_linewidth(5)
# i.spines['bottom'].set_visible(False) #tanpa garis sumbu

# i.tick_params(axis = 'x', color = 'black', colors = 'red', labelsize = 'small') #color = warna tick marker pada axis, colors = warna font axis 
# i.tick_params(axis = 'y', color = 'black', colors = 'red')
# # i.tick_params(axis = 'both', colors = 'red') #pakai both untuk sekaligus mengganti warna font x dan y axis

# #membuat garis horizontal menggunakan .axhline => bisa digunakan untuk membuat garis rata2
# i.axhline(5, color = 'g', linewidth = 3)
# #atau
# plt.axhline(3)

# #membuat garis vertikal menggunakan .axvline
# i.axvline(5)
# #atau
# plt.axvline(3, color = 'g', linewidth = 3)

# #mengisi area antara rata2
# i.fill_between(x, 5, 3, facecolor = 'g', alpha = 0.2) #alpha untuk mengatur transparansi warna

# plt.xlabel('Nilai X')
# plt.show()

#==================================================================
####artist layer
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
fig=Figure()
canvas=FigureCanvas(fig)
import numpy as np
x=np.random.randn(10000)
ax=fig.add_subplot(111)
ax.hist(x,100) #generate a histogram of the 10000 numbers
ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
# fig.savefig('matplotlib_hist.png') #langsung save ga pake plt.show()


#==================================================================
###scripting layer
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.random.randn(10000)
# plt.hist(x,100)
# ## plt.savefig('matplotlib_his1.png')
# plt.show()

#==================================================================
##check the version of matplotlib
# import matplotlib as mpl
# print('version',mpl._version)
