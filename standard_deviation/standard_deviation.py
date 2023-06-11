import numpy

speed = [86,87,88,86,87,85,86]

x_std = numpy.std(speed)
x_var = numpy.var(speed)

print("std: ", x_std)
print("var: ", x_var)