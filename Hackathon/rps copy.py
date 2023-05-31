# Rock Paper Scissors

# import random

# options = ('rock', 'paper', 'scissors')
# # player = None
# # computer = random.choice(options)
# playing = True

# while playing:
#     player = None
#     computer = random.choice(options)
#     while player not in options:
#         player = input("Enter a choice (rock, paper, or scissors):")
        
#     print(f'Player: {player}')
#     print(f'Computer: {computer}')

#     if player == computer:
#         print("It's a tie!")
#     elif player == 'rock' and computer == 'scissors':
#         print('You win!')
#     elif player == 'scissors' and computer == 'paper':
#         print('You win!')
#     elif player == 'paper' and computer == 'rock':
#         print('You win!')
#     else:
#         print('You lose :(')
        
#     play_again = input('Play again? (y/n): ').lower()
#     if not play_again == 'y':
#         playing = False

# print('Thanks for playing!')


from game import Game

def get_user_menu_choice():
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")

    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def print_results(results):
    print("Game Results:")
    print(f"Win: {results['win']}")
    print(f"Loss: {results['loss']}")
    print(f"Draw: {results['draw']}")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "2":
            print_results(results)
        else:
            print_results(results)
            break

if __name__ == "__main__":
    main()
