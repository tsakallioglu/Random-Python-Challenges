#A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters. 
#For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.
#A substitution cipher is a method of encoding where each letter of the plaintext alphabet is replaced with the 
#corresponding (i.e. having the same index) letter of some ciphertext alphabet.
#Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) substitution ciphers.

def isSubstitutionCipher(string1, string2):
    dic={}

    for i in range(len(string1)):
        if string1[i] in dic:
            if dic[string1[i]]!=string2[i]:
                return False
        else:
            if string2[i] in dic.values():
                return False
            else:
                dic[string1[i]]=string2[i]
    return True
