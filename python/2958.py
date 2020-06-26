#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/2958

matriz = {'V': [], 'D': []}

n, m = input().split(' ')
n = int(n)

for i in range(n):
    linha = input().split(' ')

    for p in linha:
        matriz[p[1]].append(int(p[0]))


matriz['V'].sort(reverse=True)
matriz['D'].sort(reverse=True)

for i in matriz['V']:
    print(str(i) + 'V')

for i in matriz['D']:
    print(str(i) + 'D')
    

