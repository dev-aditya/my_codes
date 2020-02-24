def error(exp):
    ex = sympify(exp)

    var_count = int(input('No. of variables in the eq: '))
    var = []
    m = 0
    while m < var_count:
        m += 1
        a = input("variable in the expression: ")
        var.append(a)
        locals()[a] = symbols(a)  # converts the string into a variable name

    var = np.array(var)
    val = {}
    error_val = {}

    for i in var:
        m, n = float(input('Error in variable {}  '.format(i))), float(input('Mean Value of variable {}  '.format(i)))

        val[i] = n
        error_val[i] = m
    diff_sq = []

    for i in var:
        diff_sq.append((diff(ex, i).evalf(subs=val) * error_val[i]) ** 2)

    return sqrt(sum(diff_sq))