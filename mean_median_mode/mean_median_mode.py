import numpy as np
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x_mean = np.mean(speed)
x_median = np.median(speed)
x_mode = stats.mode(speed)

print("Mean Mode: ", x_mean)
print("Median Mode: ",  x_median)
print(x_mode)
