#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1170

n = int(input())
for i in range(n):
    days = 0
    c = float(input())
    while c > 1:
        c = c / 2
        days = days + 1
    
    print(days, 'dias')
