import random

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def game_table():
    for x in range(0,3):
        print(3*(" ---") + "\n")
        print(3*"| %d " + "|   " + "\n") %(game[x][0],game[x][1],game[x][2])
    
    print(3*(" ---") + "\n")

def who_won(game):
    for x in range(0,3):
        if game[x][0] == game[x][1] and game[x][1] == game[x][2] and game[x][0] != 0:
            return game[x][0]
        elif game[0][x] == game[1][x] and game[1][x] == game[2][x] and game[0][x] != 0:
            return game[0][x]
    if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[1][1] != 0:
        return game[0][0]
    elif game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[1][1] != 0:
        return game [0][2]
    
    return 0


winner = 0
print("You are Player 2")


while True:
    game_table()
    while True:
        row_inp = int(raw_input("Please give the row you wanna play:\n>"))
        col_inp = int(raw_input("Please give the column you wanna play:\n>"))
        
        if game[row_inp][col_inp] == 0:
            game[row_inp][col_inp] = 2
            break
        else:
            print("Please play another row and column that one is not empty!")
    
    
    winner = who_won(game)
    
    if winner != 0:
        game_table()
        print("Player %d has won the game!") %winner
        break
       
    
    while True:
        r = random.randint(0,2)
        c = random.randint(0,2)
        if game[r][c] == 0:
            break
    
    game[r][c] = 1
    
    winner = who_won(game)
    
    if winner != 0:
        game_table()
        print("Player %d has won the game!") %winner
        break