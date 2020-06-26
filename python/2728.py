#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/2728

cobol = list('cobol')
while True:
    try:
        bug = ''
        words = input().split('-')
        for i in range(len(cobol)):
            if (words[i][0].casefold() != cobol[i].casefold()) and (words[i][-1].casefold() != cobol[i].casefold()):
                bug = 'BUG'
        
        if bug == 'BUG':
            print(bug)
        else:
            print('GRACE HOPPER')
            
    except EOFError:
        exit(0)
