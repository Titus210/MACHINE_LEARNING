## Import Libraries
import pandas as dp
import numpy as np
import matplotlib.pyplot as plt

## Initializing of normal distribution parameters mean, standard deviation
mean = 0.5
std = 0.1

# random module to generate seed value if not available uses system time
np.random.seed(0)

## x-coord
X = np.random.normal(mean, std, (395,1))

##  y-coord
Y = np.random.normal(mean *2, std * 3, (395,1))


# plot graph
plt.scatter(X, Y, color = 'g')
plt.show()
