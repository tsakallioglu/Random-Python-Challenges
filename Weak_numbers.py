#We define the weakness of number x as the number of positive integers smaller than x that have more divisors than x.
#It follows that the weaker the number, the greater overall weakness it has. For the given integer n, you need to answer two questions:
#what is the weakness of the weakest numbers in the range [1, n]?
#how many numbers in the range [1, n] have this weakness?
#Return the answer as an array of two elements, where the first element is the answer to the first question, 
#and the second element is the answer to the second question.

#Function that calculates the number of divisors for a given number
def num_of_div(n): 
    div=[]
    result=1
    if n!=1:
        while (n!=1):
            for i in range(2,n+1):
                if n%i==0:
                    div.append(i)
                    n /= i
                    break
        
        for x in set(div):
            result *= div.count(x)+1
    
    return result

#Main Function
def weakNumbers(n):
    divisors=[]
    weaknesses=[]

    for i in range(1,n+1):
        curr_div=num_of_div(i)
        divisors.append(curr_div)

        weakness=0
        for j in range (1,i):
            if divisors[j]>curr_div:
                weakness += 1

        weaknesses.append(weakness)

    return [max(weaknesses),weaknesses.count(max(weaknesses))]
