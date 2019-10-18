import matplotlib.pyplot as plt

labels = 'frogs', 'Hogs', 'Dogs', 'Logs'

data = [15, 30, 45, 10] # 100%

figl, axl = plt.subplots() # grafik
axl.pie(data, labels=labels, shadow=True)
plt.show()