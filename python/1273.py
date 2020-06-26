#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1273
loop = 0
while True:
    try:
        loop = loop + 1
        inputs = int(input())
        if (loop > 1) and (inputs != 0):
            print()
        
        words = []
        lengths = []

        for i in range(inputs):
            word = input()
            length = len(word)
            words.append(word)
            lengths.append(length)

        maxLength = max(lengths)

        for word in words:
            length = len(word)
            spaces = " " * (maxLength - length)
            print(spaces + word)
    
    except:
        exit(0)
   
