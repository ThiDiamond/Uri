#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1393

from math import sqrt, pow

def f(n):
    raiz5 = sqrt(5)
    return int((1/raiz5)  *  ( pow((1+raiz5)/2,n) - pow((1-raiz5)/2,n)    ))

while True:
    n = int(input())
    if n == 0:
        exit(0)
    print(f(n + 1))
