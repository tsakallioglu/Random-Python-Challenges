#You're given two integers, n and m. Find position of the rightmost bit in which they differ in their binary representations 
#(it is guaranteed that such a bit exists), counting from right to left.
#Return the value of 2position_of_the_found_bit (0-based).

def differentRightmostBit(n, m):
    return 2**str(int(bin(m)[2:]) + int(bin(n)[2:]))[::-1].find('1')
