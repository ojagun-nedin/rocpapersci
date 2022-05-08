import random


while True:
    choice_list = ['r', 's', 'p']

    computer = random.choice(choice_list)

    user = None

    def play(user, computer):
        while user not in choice_list:

            user = input("what is your choice? 'r' for rock, 's' for sciccors, and 'p' for paper:  ").lower()
    
        if user == computer:
            print("computer: ",computer)
            print("user: ",user)
            return "it's a tie"

        if win(user, computer):
            print("computer: ",computer)
            print("user: ",user)
            return "You won!!!"
        else:
            print("computer: ",computer)
            print("user: ",user)
            return "You lost!!!"


    def win(player, opponent):
        # condition: player wins if r > s or s > p or p > r......... return True

        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True

    print(play(user, computer))

    play_again = input("Play again? (y or n): ").lower()

    if play_again != 'y':
        break

print("BYE!!!")