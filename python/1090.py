numeros = {'um': 1, 'dois': 2, 'tres': 3}

def num(n):
    return numeros[n]

def simb(s):
    if s[-1] != 's':
        return s + 's'
    return s  

while True:
    n = int(input())
    if n == 0:
        exit(0)
    
    ns = []
    sb = []
    for i in range(n):
        numero, simbolo = input().split(' ')
        numero = num(numero)
        simbolo = simb(simbolo)
        ns.append(numero)
        sb.append(simbolo)
    
    print('***********************************')
    print('count', 1)
    print(ns.count(1))
    print('***********************************')
    print('count', 2)
    print(ns.count(2))
    print('***********************************')
    print('count', 3)
    print(ns.count(3))
    print('***********************************')
