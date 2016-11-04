#Given a string consisting of lowercase English letters, find the largest square which can be obtained by reordering 
#its characters and replacing them with digits (leading zeros are not allowed) where same characters always map to the same 
#digits and different characters always map to different digits.
#If there is no solution, return -1.

def constructSquare(s):
    length=len(s)

    combinations=[]
    i=4
    while length<11:
        if len(str(i**2))==length:
            combinations.append(str(i**2))        
        elif len(str(i**2))>length:
            break
        i += 1

    combinations.sort(reverse=True)

    for i in combinations:
        cnt1=[i.count(x) for x in set(i)]
        cnt2=[s.count(x) for x in set(s)]

        if sorted(cnt1)==sorted(cnt2):
            return int(i)
    return -1
