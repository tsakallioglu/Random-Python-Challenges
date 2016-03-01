def answer(heights):
    small = heights[0]
    total = 0
    
    if len(heights) <= 3:
        return 0
        
    for i in range(0,len(heights)-2):
        if heights[i] > small:
            for j in range(max(heights),0,-1):
                if heights[i+1:].count(j):
                    if j > heights[i]:
                        small = heights[i]
                        break
                    else:
                        small = j
                        break
        
        if small - heights[i+1] > 0:
            total += small - heights[i+1]
    
    return total