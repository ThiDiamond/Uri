#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1414

while True:
    t, n = input().split()
    t = int(t)
    if t == 0:
        exit(0)
    n = int(n)
    times = []
    pontos = []
    for i in range(t):
        time, ponto = input().split()
        pontos.append(int(ponto))
    print((n * 3) - sum(pontos))
