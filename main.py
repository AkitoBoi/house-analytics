import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('kc-house-data.csv')

plt.figure(figsize = (10, 6))
plt.hist(data['price'], bins=30, edgecolor = 'black')
plt.title('Распределение цен на недвижимость')
plt.xlabel('Цена (USD)')
plt.ylabel('Количество домов')
plt.grid(True)
plt.show()

plt.figure(figsize = (10, 6))
plt.hist(data['sqft_living'], bins=30, edgecolor = 'black')
plt.title('Распределение жилой площади')
plt.xlabel('Жилая площадь (sqft)')
plt.ylabel('Количество домов')
plt.grid(True)
plt.show()

plt.figure(figsize = (10, 6))
plt.hist(data['yr_built'], bins=30, edgecolor = 'black')
plt.title('Распределение года постройки')
plt.xlabel('Год постройки')
plt.ylabel('Количество домов')
plt.grid(True)
plt.show()