# Check if a number belongs to fibonacci series
import math


def perfect_sq_rt(f):
    s = int(math.sqrt(f))
    return s*s == f


def formula_check(n):
    if perfect_sq_rt(5*n*n+4) or perfect_sq_rt(5*n*n-4):
        print("Number belongs to Fibonacci Series")
    else:
        print("Number doesn't belong to Fibonacci Series")


n = int(input("Enter integer:"))
if n > 0:
    formula_check(n)



