#You are given two strings s and t of the same length, consisting of uppercase English letters. 
#Your task is to find the minimum number of "replacement operations" needed to get some anagram of the string t from the string s. 
#A replacement operation is performed by picking exactly one character from the string s and replacing it by some other character.

def createAnagram(s, t):
    s_count={}
    t_count={}

    for i in set(s):
        s_count[i]=s.count(i)

    for i in set(t):
        t_count[i]=t.count(i)

    count=0
    for i in s_count:
        if i in t_count:
            if s_count[i]>=t_count[i]:
                count += s_count[i]-t_count[i]
        else:
            count += s_count[i]
    
    return count
    
