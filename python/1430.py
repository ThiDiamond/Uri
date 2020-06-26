#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1430

notas = {'W': 1, 'H': 0.5, 'Q': 0.25, 'E': 0.125, 'S': 0.0625, 'T': 0.03125, 'X': 0.015625}
while True:
    string = input()
    if string == '*':
        exit(0)
    compassos = string.split('/')
    compassos.remove('')
    i = 0
    for compasso in compassos:
        count = 0
        for nota in compasso:
            count = count + notas[nota]
        if count == 1:
            i = i + 1
    print(i)
