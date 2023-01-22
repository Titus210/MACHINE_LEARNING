# import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import math

# define columns using normal distributions
# Column 1
col1 = abs(np.random.normal(1, 12, 100))
# Column 2
col2 = abs(np.random.normal(2, 8, 100))
# Column 3
col3 = abs(np.random.normal(3, 2, 100))
# Column 4
col4 = abs(np.random.normal(10, 15, 100))

# contain features of dataset
x = np.c_[col1, col2, col3, col4]

# output labels from 0 - 3
y = [int(np.random.randint(0, 4)) for i in range(100)]

# panda datafreame to save data
data = pd.DataFrame()

# defining colums of datasets
data['point1'] = col1
data['point2'] = col2
data['point3'] = col3
data['point4'] = col4

# plotting various features x against y
plt.subplot(2, 2, 1)
plt.title('point1')
plt.scatter(y, col1, color="r", label='Point1')

plt.subplot(2, 2, 2)
plt.title('point2')
plt.scatter(y, col1, color="g", label='Point2')

plt.subplot(2, 2, 3)
plt.title('point3')
plt.scatter(y, col1, color="b", label='Point3')

plt.subplot(2, 2, 4)
plt.title('point4')
plt.scatter(y, col1, color="y", label='Point4')

# saving the graph
plt.savefig("Data_visualization.jpg")

plt.show()