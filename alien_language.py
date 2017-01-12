#https://code.google.com/codejam/contest/dashboard?c=90101

import re
file = open('C:\Users\Mehmet T Sakallioglu\Desktop\A-large-practice.in','r')
integers=[int(x) for x in file.readline().split()]
L=integers[0]
D=integers[1]
N=integers[2]
words=[]
output=''

for i in range(D):
    words.append(file.readline()[:L])
    
for j in range(N):
    tmp=file.readline()

    tokens=re.findall(r"\(?\w+\)?",tmp)
    result=words
    
    lngth=0
    for i in range(len(tokens)):
        if tokens[i][0]!='(':
            result=[x for x in result if x[lngth:lngth+len(tokens[i])]==tokens[i]]
            lngth += len(tokens[i])
        else:
            result=[x for x in result if x[lngth:lngth+1] in tokens[i][1:len(tokens[i])-1]]
            lngth += 1
    
    output += "Case #%d: %d\n" %(j+1,len(result))

file.close()
f = open('C:\Users\Mehmet T Sakallioglu\Desktop\sdfg.in','w')
f.write(output)
f.close()
