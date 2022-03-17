import random
#r>s, s>p, p>r

def play():
    user = input("r, p, s?\n").lower()
    if (user != 'r') and (user != 'p') and (user != 's'):
        return "You typed "+ user
    computer = random.choice(['r', 'p', 's'])
    print(f"My choise was {computer}")
    if user == computer:
        return 'tie'
    elif is_win(user, computer):
        return "You win"    
    return "You lost"

def is_win(player, opponent):
    #true if player wins
    #r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
