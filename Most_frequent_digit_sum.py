#A step(x) operation works like this: it changes a number x into x - s(x), where s(x) is the sum of x's digits. 
#You like applying functions to numbers, so given the number n, you decide to build a decreasing sequence of numbers: 
#n, step(n), step(step(n)), etc., with 0 as the last element.
#Building a single sequence isn't enough for you, so you replace all elements of the sequence with the sums of their digits (s(x)). 
#Now you're curious as to which number appears in the new sequence most often. If there are several answers, return the maximal one.

def mostFrequentDigitSum(n):
    def step(x):
        return x - sum([int(i) for i in str(x)])

    seq=[]
    seq.append(sum([int(i) for i in str(n)]))
    while seq[-1] != 0:
        n=step(n)
        seq.append(sum([int(i) for i in str(n)]))

    seq_count=[[i,seq.count(i)]for i in set(seq)]

    return sorted(seq_count,key=lambda x: (x[1],x[0]), reverse=True)[0][0]
