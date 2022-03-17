import random
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        #creates list of ' ' x9 times, 3x3 board
        self.current_winner = None
        #keep track of winner

    def print_board(self):
        #get the rows: 0-1-2, 3-4-5, 6-7-8.  board[0:3], board[3:6], board[6:9]
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')
        #print(self.board)

    
    @staticmethod
    def print_board_nums():
        # 0|1|2 tells us what number corresponds to which box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        #method 1:
        """ 
        moves = []
        for (i, spot) in enumerate(self.board):
            #['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')] 
            # creates (i, spot) in loop
            if spot == ' ':
                moves.append(i)  #get indexes of available spots

        return moves
        """
        #another way:
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board #true if ' ' is in board

    def num_empty_squares(self):
        #method1:
        #return len(self.available_moves())
        #method2:
        return self.board.count(' ')

    def make_move(self, square, letter):
        #print(square)
        if self.board[square] == ' ':
            self.board[square] = letter
            #check winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # check 3 in a row, column, diagonal
        row_index = square // 3
        row = self.board[row_index*3 : (row_index + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        #column
        col_index = square % 3 # leftover from divided by 3
        column = [self.board[col_index + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #diagonal
        size=3
        #check only 0,2,4,6,8 numbers
        if square % 2 == 0:
             # it is even
            #diagonal1: 0 - 4- 8
            #i=0  i+size+1   +size+1
            diagonal1 = [self.board[i] for i in range(0, size**2, (size+1))]
            if all([spot == letter for spot in diagonal1]):
                return True
            #diagonal2: 2-4-6
            #i=size-1, i+size-1, +size-1
            diagonal2 = [self.board[i] for i in range((size-1), (size**2 - (size-1)), (size - 1))] 
            if all([spot == letter for spot in diagonal2]):
                return True
        #here all checks fail
        return False



def play(game, x_player, o_player, print_game=True):
    #returns the winner (letter) or None if a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    #iterate while are available places
    while game.empty_squares():
        #get the move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}.')
                game.print_board()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter    


        #alternate letter (swith players)
        letter = 'O' if letter == 'X' else 'X'
        #make pause
        if print_game:
            time.sleep(0.8)

    #while loop ends
    if print_game:
        print('It\'s a tie')

            


#my method to get diagonal
def my_diagonal():
    my_board = [i for i in range(9)]
    size=3
    print(size**2)
    #just display board
    for i in range(3):
        print(my_board[i*3: (i*3+3)])
    #diagonal1: 0 - 4- 8
    #i=0  i+size+1   +size+1
    my_diagonal1 = [my_board[i] for i in range(0, size**2, (size+1))]
    print(my_diagonal1)
    #diagonal2: 2-4-6
    #i=size-1, i+size-1, +size-1
    my_diagonal2 = [my_board[i] for i in range((size-1), (size**2 - (size-1)), (size - 1))] 
    print(my_diagonal2)



if __name__ == '__main__':
    def automated_run():
    
        x_wins = 0
        o_wins = 0
        ties = 0
     
       
        for _ in range(10):
            o_player = RandomComputerPlayer('O')
            x_player = GeniusComputerPlayer('X')

            t = TicTacToe()
            #t.print_board_nums()
            #play(t, x_player, o_player, print_game=True)
            result = play(t, x_player, o_player, print_game=False)
            if result == 'X':
                x_wins += 1
            elif result == 'O':
                o_wins += 1
            else:
                ties +=1

        print(f'After 1000 plays {x_wins} X wins, {o_wins} O wins, {ties} ties')


    o_player = HumanPlayer('O')
    x_player = GeniusComputerPlayer('X')

    t = TicTacToe()
    t.print_board_nums()
    play(t, x_player, o_player, print_game=True)



