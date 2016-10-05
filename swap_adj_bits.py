#You're given an arbitrary 32-bit integer n. 
#Swap each pair of adjacent bits in its binary representation and return the result as a decimal number.
def swapAdjacentBits(n):
    return int(''.join([(bin(n)[2:].zfill((len(bin(n)[2:])/2)*2 + (len(bin(n)[2:])%2)*2))[i+1]+(bin(n)[2:].zfill((len(bin(n)[2:])/2)*2 + (len(bin(n)[2:])%2)*2))[i] for i in range(0,len((bin(n)[2:].zfill((len(bin(n)[2:])/2)*2 + (len(bin(n)[2:])%2)*2))),2)]),2)
    
#above function is the same as this one below, only difference that variable 'a' has been inserted into the comprehension
#a = (bin(n)[2:].zfill((len(bin(n)[2:])/2)*2 + (len(bin(n)[2:])%2)*2))
#print int(''.join([a[i+1]+a[i] for i in range(0,len(a),2)]),2)
