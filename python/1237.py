#Link to problem:
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1237

from difflib import SequenceMatcher 
  
def longestSubstring(str1,str2): 
  
     # initialize SequenceMatcher object with  
     # input string 
     seqMatch = SequenceMatcher(None,str1,str2) 
  
     # find match of longest sub-string 
     # output will be like Match(a=0, b=0, size=5) 
     match = seqMatch.find_longest_match(0, len(str1), 0, len(str2)) 
  
     # print longest substring 
     if (match.size!=0): 
          print (len(str1[match.a: match.a + match.size]))  
     else: 
          print (0) 
  
while True:
    try:
        a = input()
        b = input()

        longestSubstring(a,b)     

    except EOFError:
        exit(0)
