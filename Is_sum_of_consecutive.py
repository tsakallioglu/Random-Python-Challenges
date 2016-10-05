#Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

def isSumOfConsecutive2(n):
    count=0

    for m in range(2,n):
        if ((m%2==1 and n%m==0) or (m%2==0 and (2*n+m)%(2*m)==0)) and (2*n-m**2)/(2*m)>=0:
            count += 1
    
    return count
