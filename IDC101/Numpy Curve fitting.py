import matplotlib as plt
import numpy

# demo curve fitting
x = numpy.array([0.0 , 1.0 , 2.0 , 3.0 , 4.0 , 5.0])
y = numpy.array([0.0 , 0.8 , 0.9 , 0.1 , -0.8 , -1.0])
# now do fit for cubic (order = 3) polynomial
z = numpy.polyfit(x, y, 3)
# z is an array of coefficients , highest first , i . e .
# z = array ([ 0.08703704 , -0.81349206 , 1.69312169 , -0.03968254])
p = numpy.poly1d(z) # creates a polynomial function p from coefficients in z

xs = [0.1 * i for i in range (50)]
ys = [p ( x ) for x in xs]


plt.plot(x, y, 'o', label='data')
plt.plot(xs, ys, label='fitted curve')
plt.ylabel('y')
plt.xlabel('x')
plt.show()