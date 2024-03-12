import csv
import matplotlib.pyplot as plt
import numpy as np


with open('data1.csv', newline='', encoding='windows-1251') as csvfile:
    data = []
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        data.append(row)
x1 = [data[i][0] for i in range(1, len(data))] #1 столбец
y1 = [float(data[i][3]) for i in range(1, len(data))] #4 столбец
y2 = [float(data[i][9]) for i in range(1, len(data))] #10 столбец

figs, ax = plt.subplots(figsize=(8, 4))
plt.plot(x1, y1, label='4-column plot')
plt.plot(x1, y2, label='10-column plot')
plt.axis([0, len(x1), 0, 120])
ax.set_xticks(np.arange(0, len(x1), 300))
plt.xlabel('1 column')
plt.ylabel('4 and 10 column')

plt.legend()
plt.show()