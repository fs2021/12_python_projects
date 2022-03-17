import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter


    # we want all player to get their next move
    def get_move(self, game):
        pass #it is 'no operation', just placeholder

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid spot for next move
        square = random.choice(game.available_moves())
        return square

        

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            #check if it's integer number and available move
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square")
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #at the beginning choose random
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #cho0se based on minimax algorithm
            square = self.minimax(game, self.letter)['position']
            #print(square)
            


        return square


    def minimax(self, state_of_game, player):
        #yourself
        #score is maximum for best move and minimum for worst move
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        #check if the previous move was a winner
        if state_of_game.current_winner == other_player:
            #we should return position and score
            #for minimax to work
            score = 1*(state_of_game.num_empty_squares() + 1)
            return {
                'position': None,
                'score': score if other_player == max_player else -1*score
            }
        elif not state_of_game.empty_squares():

            return {
                'position': None,
                'score': 0
            }

        if player == max_player:
            #initialize
            best = {
                'position': None,
                'score': -math.inf #each score must be larger, maximize
            }    
        else: best = {
                'position': None,
                'score': math.inf #each score must be smaller, minimize
            }    

        for possible_move in state_of_game.available_moves():
            #step1 - make a move, try that spot
            state_of_game.make_move(possible_move, player)
            
            #step2 - recurse using minimax to simulate game after that move
            #now, we alternate players
            simulated_score = self.minimax(state_of_game, other_player)
            

            #step3 - undo that move
            state_of_game.board[possible_move] = ' '
            state_of_game.current_winner = None
            simulated_score['position'] = possible_move
            #otherwise we will messed up from recursion

            #step4 - update dictionaries if new score is better than current in dictionary
            if player == max_player:
                if simulated_score['score'] > best['score']:
                    best = simulated_score
            else:
                if simulated_score['score'] < best['score']:
                    best = simulated_score
        #print(best)
        return best                            
    