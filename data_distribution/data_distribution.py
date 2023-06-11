import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 250)

print("Create an array containing 250 random floats between 0 and 5:", x)

x = np.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()

#Normal Data Distribution
x = np.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()