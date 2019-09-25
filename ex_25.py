from math import *

num = float(input("Insira um número: "))
base = 2.0

def power(n):
    return n**2.0

def newton_eq(n):
    return (base + (n/base)) / 2.0

def error(k, p_guess):
    return abs(k - (power(p_guess))) < 0.001

p = 0

while(not error(num, p)):
    p = newton_eq(num)
    base = p

print("A raiz é: " + str(p))

# print(p)
# print(k)
