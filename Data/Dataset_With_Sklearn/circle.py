# importing libraries
from sklearn.datasets import make_circles
from matplotlib import pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')

X, y = make_circles(n_samples = 100 , noise = 0.02)
plt.scatter(X[:,0], X[:,1], s = 40 , color = 'g')
plt.ylabel('Y')
plt.xlabel('X')

plt.show()
plt.clf()
