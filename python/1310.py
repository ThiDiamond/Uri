#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1310

def maxSubArraySum(a,size): 
      
    max_so_far = a[0] 
    curr_max = a[0] 
      
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max) 

    if max_so_far <= 0:
        max_so_far = 0      
    return max_so_far 
  


while True:
    try:
        receita = []
        n = int(input())
        cpd = int(input())
        for i in range(n):
            receita.append(int(input()) - cpd)
        
        print(maxSubArraySum(receita, len(receita)))

    except EOFError:
        exit(0)
