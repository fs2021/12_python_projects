import random

#board object to represent game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #create the board
        #helper function
        self.board = self.make_new_board()  #plant the bombs


        #initialize a set to keep track of uncovered locations
        #we'll save tuplets (row, col)
        self.dug = set() #if we dig (0,0) --- self.dug = {(0,0)}


    def make_new_board(self):
        #construct new board with bombs
        #list of lists(rows) for 2D board

        #generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #this creates an array 10x10 of "None"
        #print(board)

        #plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            #column is a reminder of loc/dim
            col = loc % self.dim_size

            #'*' means the bomb
            bomb = '*'
            if self.bomb_is_here(board, row, col):
                #just skip this location
                continue
            #plant the bomb
            board[row][col] = bomb
            bombs_planted += 1
        return board
 



    def bomb_is_here(self, board, row, col):
        bomb = '*'
        if board[row][col] == bomb:
            return True
        else:
            return False


    #assign number (0-8) of neighboring bombs to all empty spaces
    def assign_values_to_board(self):
        for r in range(0, self.dim_size):
            for c in range(0, self.dim_size):
                if not self.bomb_is_here(r, c):
                    self.board[r][c] = self.get_num_neighboring_b(r, c)
        pass


    def get_num_neighboring_b(self, row, col):
        #iterate for each of neghboring position and calculate bombs
        #top left r-1, c-1
        #top r-1, c
        #top right r-1, c+1 
        #etc but check bounds!
        num_neighboring_bombs = 0

        #iterate for 3x3 grid of neighbors
        #min and max for board bounds (min=0, max=dim-1)
        """ for r in range(max(0,(row-1)), min((row+1)+1, self.dim_size-1)):
            for c in range(max(0,(col-1)), min((col+1)+1, self.dim_size-1)):
                #we don't want to check central location
                if c != col and r != row:
                    if self.bomb_is_here(r,c):
                        num_neighboring_bombs += 1
        return num_neighboring_bombs """

        #my method
        neighbors = self.get_valid_3x3_coords(self, self.dim_size, row, col)
        for coordinates in neighbors:
            if self.bomb_is_here(coordinates[0], coordinates[1]):
                num_neighboring_bombs += 1
        return num_neighboring_bombs



    def dig(self, row, col):
        #True if no bomb
        #Game over if bomb
        #Uncover number of neighboring
        #if no neighboring - recursively dig neighbors
        self.dug.add((row, col))  #keep track of dug locs

        if self.bomb_is_here(row, col):
            return False
        elif self.board[row][col] > 0:
            #there are neighboring bombs
            return True
        #here we are if no neighboring bomb
        neighbors = self.get_valid_3x3_coords(self, self.dim_size, row, col)
        for coordinates in neighbors:
            self.dig(coordinates)



    def get_valid_3x3_coords(self, dim, row, col):
        neighbors = set()
        for r in range(max(0,(row-1)), min((row+1)+1, dim-1)):
            for c in range(max(0,(col-1)), min((col+1)+1, dim-1)):
                #we don't want to add central location
                if c != col or r != row:
                    neighbors.add((r,c))
        return neighbors


def play(dim_size = 10, num_bombs = 10):
    #step1 create board and plant the bombs
    board = Board(dim_size, num_bombs)

    #step2 show the board and ask to dig
    #step3a if location is a bomb - end the game
    #step3b if not a bomb, dig recursively untill  each square is at least 
    #       next to a bomb
    #step4 repeat st2 and 3 untill there are no more places to dig -- Win
    pass

if __name__=='__main__':
    print('st')
    b = Board(10, 10)
    n = b.get_valid_3x3_coords(10, 0, 0)
    for coord in n:

        print(coord[0])
