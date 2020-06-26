#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1728

while True:
    a, b, c = input().replace('+', ' ').replace('=', ' ').split(' ')
    if [a, b, c] == ['0','0','0']:
        print(True)
        exit(0)
    
    a = int(a[::-1])
    b = int(b[::-1])
    c = int(c[::-1])
    print(a + b == c)
