#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1796
n = input()

c = input().split(' ')

if c.count('0') > c.count('1'):
    print('Y')
else:
    print('N')
