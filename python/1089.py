#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1089

class oscii:
    def __init__(self,init):
        self.cont = 0
        if init:
            self.subindo = True
            self.descendo = False
        else:
            self.subindo = False
            self.descendo = True
    def mudou(self):
        if self.subindo:
            self.subindo = False
            self.descendo = True
        else:
            self.subindo = True
            self.descendo = False
        self.cont = self.cont + 1

    def atual(self,n1,n2):
        if self.subindo:
            if int(n1) > int(n2):
                self.mudou()
        else:
            if int(n1) < int(n2):
                    self.mudou()

    def getCont(self):
        return self.cont

def setList(lista):
    newlist = []
    for i in lista:
        newlist.append(int(i))
    return newlist

while True:
    n = int(input())
    if n == 0:
        exit(0)
    lista = input().split(" ")
    lista.append(lista[0])
    lista = setList(lista)
    obj = oscii(lista[0] < lista[1])

    for i in range(len(lista)):
        if i < len(lista) - 1:
            obj.atual(lista[i],lista[i + 1])
    i = 0
    if (lista[0] > lista[1]) & (lista[n - 1] > lista[n]):
        i = i - 1
    if (lista[0] < lista[1]) & (lista[n - 1] < lista[n]):
        i = i - 1

    print( obj.getCont() + 1 + i)
