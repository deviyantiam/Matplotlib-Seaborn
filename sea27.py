## replot
## barplot
## heatmap

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x=np.arange(10)
y=np.random.randint(10,size=10)
dataku =pd.DataFrame({
    'x':x,
    'y':y,
    'z':['Ya','Tidak','Boleh Juga','Tidak','Ya','Tidak','Ya','Ya','Boleh Juga','Tidak']
})
# sns.set(style='darkgrid')
print(dataku)
sns.relplot(data=dataku,x='x',y='y',kind='line')
# sns.relplot(data=dataku,x='x',y='y',hue='z',kind='scatter')
# sns.relplot(data=dataku,x='x',y='y',hue='z',size='z',style='z',kind='scatter') #size besar, style lingkaran beda
# sns.barplot(data=dataku,x='x',y='y',hue='z')
plt.show()

# mydata=sns.load_dataset('flights')
# print(mydata)
# mydata=mydata.pivot('month','year','passengers')
# print(mydata)
# sns.heatmap(mydata)
# sns.heatmap(mydata,cmap='rocket')
# sns.heatmap(mydata,cmap='rocket_r',annot=True,fmt='d') #_r dibalik, anot angka muncul, fmt=digit biar tulisannya pendek
# sns.heatmap(mydata,cmap='BuPu',annot=True,fmt='d')
# sns.swarmplot(data=mydata,x='month',y='passengers',hue='year') #ga usah pivot
##lmplot tarik garis lurus/best fit line, prediksi data yang ga ada, tidak bisa analisa karena cuma tampilan doang
# sns.lmplot(data=mydata,x='year',y='passengers')
# plt.xticks(rotation=90)
# plt.legend(loc=2, fontsize=5.4)
# plt.show()



