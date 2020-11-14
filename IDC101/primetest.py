                '''Primarility test'''
import math
import random

def FermatPrimalityTest(number):
    if (number > 1):
        for t in range(100):
            # check for some random integer 100 times.
            randomNumber = random.randint(2, number) - 1
            # pow(x,y,z) returns x*^y(mod z)
            if (pow(randomNumber, number - 1, number) != 1):
                return False

        return True
    else:
        return False


def Isprime(n):
    if FrematPrimarilityTest(n)==True:
        while n <= 1:
            return False
        for i in range(2, int(math.sqrt(n) + 1), 1):
            if n % i == 0:
                return False
        return True
    else:
        return False


