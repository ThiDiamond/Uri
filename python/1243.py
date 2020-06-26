#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1243

while True:
    try:
        string = input()
        symbols = string.split()
        lengths = []
        for symbol in symbols:
            if symbol[:len(symbol) - 1].isalpha():
                if symbol[-1] == '.':
                    lengths.append(len(symbol) - 1)
                elif symbol[-1].isalpha():
                    lengths.append(len(symbol))

            elif len(symbol) == 1 and symbol.isalpha():
                lengths.append(1)

        try:        
            median = int(sum(lengths) / len(lengths))
        except ZeroDivisionError:
            median = 0
        if median <= 3:
            result = 250
        elif median < 6:
            result = 500
        else:
            result = 1000

        print(result)
    except EOFError:
        exit(0) 
