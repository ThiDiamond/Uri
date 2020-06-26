#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1259

n = int(input())
pair = []
odd = []
for i in range(n):
    number = int(input())
    
    if number % 2 == 0:
        pair.append(number)
    else:
        odd.append(number)

pair.sort()
odd.sort(reverse=True)

for i in pair:
    print(i)
for i in odd:
    print(i)
