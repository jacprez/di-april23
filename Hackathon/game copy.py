# Part 1
# import random
# options = ('rock', 'paper', 'scissors')
# class Game :
#     options = ('rock', 'paper', 'scissors')
#     def __init__(self):
#         pass
    
#     def get_user_item(self):
#         pass
    
#     def get_computer_item(self):
#         pass
#     def get_game_result(self, user_item, computer_item):
#         self.get_user_items


import random

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Enter your choice (rock/paper/scissors): ")
            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid choice. Please try again.")

    def get_computer_item(self):
        computer_item = random.choice(["rock", "paper", "scissors"])
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors")
            or (user_item == "paper" and computer_item == "rock")
            or (user_item == "scissors" and computer_item == "paper")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        
        print(f"You selected {user_item}. The computer selected {computer_item}.")

        if result == "win":
            print("You win!")
        elif result == "draw":
            print("It's a draw!")
        else:
            print("You lose!")

        return result