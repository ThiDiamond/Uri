#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/2242

vogais = ['a', 'e', 'i', 'o', 'u']
risada = input()
risadaVogal = []

for letra in risada:
    if letra in vogais:
        risadaVogal.append(letra)

risada = ''.join(risadaVogal)

if risada == risada[::-1]:
    print('S')
else:
    print('N')
