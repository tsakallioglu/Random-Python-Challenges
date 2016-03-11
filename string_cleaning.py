def answer(chunk,word):  
    comb=[]
    i=0
    while True:
        i=chunk.find(word,i)
        if i == -1:
            break
        comb.append(chunk[:i]+chunk[(i+len(word)):]) 
        i=i+1
            
    for a in comb:
        j=0
        while True:
            j=a.find(word,j)
            
            if j == -1:
                break
            
            if a[:j]+a[(j+len(word)):] not in comb:
                comb.append(a[:j]+a[(j+len(word)):])
            
            if '' in comb:
                return ''
            j=j+1
    
    comb.sort()
    comb.sort(key=len)
    return comb[0]