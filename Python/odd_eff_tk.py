import tkinter as tk
import random

def play_game():
    try:
        n = int(entry_value.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return
    
    decision = entry_choice.get().lower()

    i = n + random.randint(1, 10)

    if (decision == 'even' and i % 2 == 0) or (decision == 'odd' and i % 2 != 0):
        option_label.config(text="Enter 'bat' for batting or 'bowl' for bowling:")
        option_menu.config(state=tk.NORMAL)
    else:
        option_label.config(text="You lost the toss. Computer decides.")
        option_menu.config(state=tk.DISABLED)

def start_game():
    option_label.config(text="Enter 'bat' for batting or 'bowl' for bowling:")
    number_label.config(text="Enter a number (Batting):")
    number_entry.config(state=tk.NORMAL)
    result_label.config(text="")

def play_batting():
    try:
        number = int(number_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return
    
    global sum_bat
    if number == random.randint(1, 10):
        result_label.config(text=f"Batting sum: {sum_bat}")
        number_entry.config(state=tk.DISABLED)
    else:
        sum_bat += number
        result_label.config(text=f"Current batting sum: {sum_bat}")
        number_entry.delete(0, tk.END)

def play_bowling():
    try:
        number = int(number_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return
    
    global sum_bowl
    if number == random.randint(1, 10):
        result_label.config(text=f"Bowling sum: {sum_bowl}")
        number_entry.config(state=tk.DISABLED)
    else:
        sum_bowl += number
        result_label.config(text=f"Current bowling sum: {sum_bowl}")
        number_entry.delete(0, tk.END)

sum_bat = 0
sum_bowl = 0

root = tk.Tk()
root.title("Odd_eff Game")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label_value = tk.Label(frame, text="Enter value from 1 to 10:")
label_value.grid(row=0, column=0, padx=5, pady=5)
entry_value = tk.Entry(frame)
entry_value.grid(row=0, column=1, padx=5, pady=5)

label_choice = tk.Label(frame, text="Odd or even:")
label_choice.grid(row=1, column=0, padx=5, pady=5)
entry_choice = tk.Entry(frame)
entry_choice.grid(row=1, column=1, padx=5, pady=5)

option_label = tk.Label(frame, text="")
option_label.grid(row=2, columnspan=2, padx=5, pady=10)

play_button = tk.Button(frame, text="Start Toss", command=play_game)
play_button.grid(row=3, columnspan=2, padx=5, pady=5)

number_label = tk.Label(frame, text="")
number_label.grid(row=4, columnspan=2, padx=5, pady=10)

number_entry = tk.Entry(frame)
number_entry.grid(row=5, column=1, padx=5, pady=5)

option_var = tk.StringVar(frame, "bat")
option_menu = tk.OptionMenu(frame, option_var, "bat", "bowl")
option_menu.grid(row=5, column=0, padx=5, pady=5)

result_label = tk.Label(frame, text="")
result_label.grid(row=6, columnspan=2, padx=5, pady=10)

def option_changed(*args):
    if option_var.get() == "bat":
        play_batting()
    elif option_var.get() == "bowl":
        play_bowling()

option_var.trace('w', option_changed)

root.mainloop()
