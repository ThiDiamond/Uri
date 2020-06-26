while True:
    (d, n) = input().split()
    if d == '0' and n == '0':
        exit(0)
    n = n.replace(d, '')
    if n == '':
        print(0)
    else:
        print(int(n))
