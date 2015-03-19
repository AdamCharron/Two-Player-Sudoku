def table(N, grid):
    game_grid = ' '

    for rows in range(N):
        for columns in range(N):

            game_grid += str(grid[rows][columns]) + ' '
            if ((columns + 1)%N**0.5 == 0) and ((columns + 1) != N):
                game_grid += '| '
            if (columns + 1) == N:
                game_grid += '\n' + ' '
        if ((rows + 1)%N**0.5 == 0) and ((rows + 1) != N):
            game_grid += '-'*len(game_grid[:game_grid.find('\n') - 2])\
                         + '\n' + ' '
    print(game_grid)    
    return game_grid            


    
def move(N, grid, row, col, val):

    '''print("move is: ", check_move(N, grid, row, col, val))'''

    if (check_move(N, grid, row, col, val) != 1):
        print("I'm sorry, but I can't do that")
        return 0
    
    grid[row - 1][col - 1] = val
    return grid


def validate(num, N):

    if (num < 0):
        return -99
    
    if ((type(num) != int) or (num > N)):
        return 0

    return 1
    

def check_move(N, grid, row, col, val):

    if (grid[row - 1][col - 1] != 0):
        return 0

    for i in range(N):
        if (val == grid[row-1][i]):
            return 0

    for j in range(N):
        if (val == grid[j][col-1]):
            return 0

    row_low = int(((row-1)//(N**0.5)) * (N**0.5))
    row_high = int(row_low + (N**0.5 - 1))
    col_low = int(((col-1)//(N**0.5)) * (N**0.5))
    col_high = int(col_low + (N**0.5 - 1))

    '''print("RL, RH, CL, CH, N: ", row_low, row_high, col_low, col_high, N)'''

    for k in range(row_low, row_high + 1):
        for l in range(col_low, col_high + 1):
            if (grid[k][l] == val):
                return 0

    return 1


def check_win(grid, N):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (grid[i-1][j-1] == 0):
                for k in range(1, N + 1):
                    '''print("i: ", i, "j: ", j, "K: ", k)'''
                    if (check_move(N, grid, i, j, k) == 1):
                        return 1

    return 0
        

def main():

    N = int(input("Grid size:"))
    if ((N!=2) and (N != 4) and (N != 9)):
        return

    grid = []
    for element in [0]*N:
        grid += [[0]*N]
    player = 0

    table(N, grid)

    while 1:

        if (check_win(grid, N) == 0):
            player += 1
            print("Player", player%2 + 1, " has won the game")
            return
        
        try:
            print("Player", player%2 + 1, "'s move:")
            row = int(input("Row:"))
            col = int(input("Col:"))
            val = int(input("Val:"))
        except:
            print("Invalid entry")
            continue

        if ((validate(row, N) + validate(col, N) + validate(val, N)) < 0):
            print("Terminating game")
            return
            
        if ((validate(row, N) + validate(col, N) + validate(val, N)) != 3):
            print("What are you doing?")
            continue

        temp = move(N, grid, row, col, val)
        if (temp != 0):
            grid = temp
            player += 1

        print('\n\n', grid, '\n\n')
        
        game_grid = table(N, grid)

main()
