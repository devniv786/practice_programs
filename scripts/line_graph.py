import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame({'Count':[100, 200, 500],'HTTP Response Time':[3500, 3600, 3900],'Processed Time':[3100, 3300, 3500],'Published Time':[4500, 4700, 5100],'Confirmed Time':[5600, 5900, 6500]})
df = pd.read_excel('Data.xlsx')
x = list(df['Count'].values)
y1 = list(df['HTTP Response Time'].values)
y2 = list(df['Processed Time'].values)
y3 = list(df['Published Time'].values)
y4 = list(df['Confirmed Time'].values)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

plt.legend(['HTTP Response Time', 'Processed Time', 'Published Time',
       'Confirmed Time'], loc='upper right')

plt.show()