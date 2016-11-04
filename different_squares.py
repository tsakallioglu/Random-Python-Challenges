#Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

def differentSquares(matrix):
    a=[]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            try:
                if a.index([matrix[i][j:j+2],matrix[i+1][j:j+2]])>=0:
                    continue
            except:
                a.append([matrix[i][j:j+2],matrix[i+1][j:j+2]])
    return len(a)
