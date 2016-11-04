#Let's call two integers A and B friends if each integer from the array divisors is a divisor of both A and B or neither A nor B. 
#If two integers are friends, they are said to be in the same clan. How many clans are the integers from 1 to k, inclusive, broken into?

def numberOfClans(divisors, k):
    def div(n): 
        return [i for i in range(1,n+1) if n%i==0]

    divisors.append(1)
    count=0
    a=[]
    for i in range(1,k+1):
        inter=list(set(divisors) & set(div(i)))
        try:
            if a.index(inter)>=0:
                continue
        except:
            a.append(inter)
            count += 1
    return count
