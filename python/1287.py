#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1287

while True:
  try:
      string = input()
      string = string.replace('O', '0')
      string = string.replace('o', '0')

      string = string.replace('l', '1')
      
      string = string.replace(',', '')
      string = string.replace(' ', '')

      try:
          number = int(string)
          if ((number > 2147483647) or (number < 0)):
            print('error')
          else:
            print(number)
      except:
          print('error')


  except EOFError:
    exit(0) 
