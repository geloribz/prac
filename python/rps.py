import random

def play():
    user = input("What's your choice:\n'r' for rock, 'p' for paper, 's' for scissors?\n")
    computer = random.choice(['r','p','s'])
    print(f'Computer chose {computer}!')

    if user == computer:
        return 'It\'s a tie!'

    # r>s,s>p,p>r
    if is_win(user, computer):
        return 'You win!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r>s,s>p,p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

trial = 'y'
while trial == 'y':
    print(play())
    trial = input('Play again? Y/N:\n').lower()