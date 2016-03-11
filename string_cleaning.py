def answer(chunk,word):
    chunk2=list(chunk)
    i=50
    result=[]
    
    while i != 0:
            a = (''.join(chunk2)).find(word)
            if a != -1:
                for _ in xrange(len(word)):
                    chunk2.pop(a)
                
            i = i-1
            
    result.append(''.join(chunk2))
    
    chunk2=list(chunk)
    i=50
    
    while i != 0:
            a = (''.join(chunk2)).rfind(word)
            if a != -1:
                for _ in xrange(len(word)):
                    chunk2.pop(a)
                
            i = i-1
            
    result.append(''.join(chunk2))
    result.sort()
    
    return result[0]
    
chunk="hohololholoholoo"
word="holo"
print answer(chunk,word)