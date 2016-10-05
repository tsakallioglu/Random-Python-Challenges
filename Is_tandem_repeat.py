#Determine whether the given string can be obtained by one concatenation of some string to itself.

def isTandemRepeat(inputString):
    for i in range(1,len(inputString)/2+1):
        if inputString[:i+1]*(len(inputString)/len(inputString[:i+1]))==inputString:
            return True
    return False
