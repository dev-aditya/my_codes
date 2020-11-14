import numpy as N
import numpy.linalg as la

var_count = int(input("No. of variables you want to solve for: "))

coef = N.zeros((var_count, var_count))

R_val = N.zeros(var_count)

for row in range(1, var_count + 1):
    for col in range(1, var_count + 1):
        coef[row - 1, col - 1] = float(input("Coefficient ofx{}: ".format(col)))
        print(coef)

    R_val[row - 1] = float(input("Value on the RHS of the equation: "))
    print(R_val)

var_mat = coef.copy()
var_mat = N.transpose(var_mat)

det = []

for row in range(var_count):
    for col in range(var_count):
        var_mat[row, col] = R_val[col]
    det.append(la.det(var_mat))
    var_mat = coef.copy()
    var_mat = N.transpose(var_mat)
det_array = N.array(det)
if la.det(coef) == 0:
    if len(set(det)) == 1 and list(set(det))[0] == 0:
        print("Infinite solutions exist!")
    elif len(set(det)) != 0:
        print("No Solution Exist!")
else:
    for i in range(var_count):
        print("Value of  x{} is {}".format(i + 1, det_array[i] / la.det(coef)))