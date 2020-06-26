#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1793
while True:
    n = int(input())
    if n == 0:
        exit(0)
    t = input().split(' ')
    result = []
    for i in t:
        i = int(i)
        result = result + list(range(i, i+10))
    print(len(set(result)))
