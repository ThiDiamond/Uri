#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/2633
while True:
    try:
        carnes = {}
        n = int(input())
        for i in range(n):
            carne, dias = input().split(' ')
            dias = int(dias)
            carnes[dias] = carne
         
        saida = ''
        for i in sorted(carnes.keys()):
            saida = saida + carnes[i] + ' '
        
        print(saida[:len(saida) - 1])

    except EOFError:
        exit(0)
