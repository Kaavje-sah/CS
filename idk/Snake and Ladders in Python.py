# Snake and Ladders in Python
import random
import time

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player_position = 1
    computer_position = 1

    while player_position < 101 and computer_position < 101:
        # Player's turn
        print(f"\nCurrent player position: {player_position}")
        input("Press Enter to roll the dice...")
        player_roll = roll_dice()
        print(f"You rolled a {player_roll}")
        player_position += player_roll
        if player_position > 100:
            player_position = 100
            print("You reached the final position! Congratulations!")
        elif player_position == 100:
            print("You reached the final position! Congratulations!")
        elif player_position > 50 and player_position < 70:
            player_position = 30
            print("Oh no! You landed on a snake. You've been moved to position 30.")
        elif player_position > 70 and player_position < 90:
            player_position = 50
            print("Oh no! You landed on a snake. You've been moved to position 50.")
        else:
            print(f"Your new position is {player_position}.")

        if computer_position < 101:
            print(f"\nCurrent computer position: {computer_position}")
            print("Computer is rolling the dice...")
            computer_roll = roll_dice()
            print(f"Computer rolled a {computer_roll}")
            computer_position += computer_roll
            if computer_position > 100:
                computer_position = 100
                print("Computer reached the final position! Better luck next time!")
            elif computer_position == 100:
                print("Computer reached the final position! Better luck next time!")
            elif computer_position > 50 and computer_position < 70:
                computer_position = 30
                print("Oh no! Computer landed on a snake. Computer's been moved to position 30.")
            elif computer_position > 70 and computer_position < 90:
                computer_position = 50
                print("Oh no! Computer landed on a snake. Computer's been moved to position 50.")
            else:
                print(f"Computer's new position is {computer_position}.")
            time.sleep(1)

    if player_position == 100 and computer_position == 100:
        print("It's a tie!")
    elif player_position == 100:
        print("You win! Congratulations!")
    else:
        print("Computer wins! Better luck next time!")

    print("\nGame over!")

play_game()

# import tkinter as tk
# import random

# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.position = 1

# class Game:
#     def __init__(self):
#         self.player = Player("Player")
#         self.computer = Player("Computer")
#         self.current_player = self.player
#         self.dice_value = 0
#         self.snakes = {55: 30, 75: 50}
#         self.ladders = {}  # Add ladders as needed

#     def roll_dice(self):
#         self.dice_value = random.randint(1, 6)
#         self.update_game_state()

#     def update_game_state(self):
#         self.current_player.position += self.dice_value
#         if self.current_player.position > 100:
#             self.current_player.position = 100
#         if self.current_player.position in self.snakes:
#             self.current_player.position = self.snakes[self.current_player.position]
#             main_window.dice_label.config(text=f"{self.current_player.name} landed on a snake! New position: {self.current_player.position}")
#         elif self.current_player.position in self.ladders:
#             self.current_player.position = self.ladders[self.current_player.position]
#             main_window.dice_label.config(text=f"{self.current_player.name} landed on a ladder! New position: {self.current_player.position}")
#         else:
#             main_window.dice_label.config(text=f"{self.current_player.name} rolled a {self.dice_value}. New position: {self.current_player.position}")
#         if self.current_player.position == 100:
#             main_window.dice_label.config(text=f"{self.current_player.name} wins! Congratulations!")
#             main_window.roll_button.config(state="disabled")
#         else:
#             if self.current_player == self.player:
#                 self.current_player = self.computer
#                 main_window.dice_label.config(text="Computer's turn...")
#                 self.computer_turn()
#             else:
#                 self.current_player = self.player

#     def computer_turn(self):
#         self.dice_value = random.randint(1, 6)
#         self.update_game_state()

# class Board:
#     def __init__(self, master):
#         self.master = master
#         self.canvas = tk.Canvas(master, width=400, height=400)
#         self.canvas.pack()
#         self.draw_board()
#         self.player_token = None
#         self.computer_token = None

#     def draw_board(self):
#         for i in range(10):
#             for j in range(10):
#                 self.canvas.create_rectangle(i*40, j*40, (i+1)*40, (j+1)*40, fill='white')

#     def update_player_position(self, position):
#         if self.player_token:
#             self.canvas.delete(self.player_token)
#         x = (position - 1) % 10
#         y = 9 - (position - 1) // 10
#         self.player_token = self.canvas.create_text(x*40 + 20, y*40 + 20, text='*', font=('Arial', 24), fill='blue')

#     def update_computer_position(self, position):
#         if self.computer_token:
#             self.canvas.delete(self.computer_token)
#         x = (position - 1) % 10
#         y = 9 - (position - 1) // 10
#         self.computer_token = self.canvas.create_text(x*40 + 20, y*40 + 20, text='*', font=('Arial', 24), fill='red')
# class MainWindow:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(master)
#         self.frame.pack()
#         self.board = Board(self.frame)
#         self.dice_label = tk.Label(self.frame, text='Roll the dice!')
#         self.dice_label.pack()
#         self.roll_button = tk.Button(self.frame, text='Roll', command=game.roll_dice)
#         self.roll_button.pack()

# root = tk.Tk()
# game = Game()
# main_window = MainWindow(root)
# root.mainloop()