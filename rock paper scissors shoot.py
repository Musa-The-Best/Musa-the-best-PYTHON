import tkinter as tk
import random
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""
    if choice == computer_choice:
        result = f"Draw! Both chose {choice}"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! Computer chose {computer_choice}"
    else:
        result = f"You Lose! Computer chose {computer_choice}"
    
    result_label.config(text=result)
root = tk.Tk()
root.title("Rock Paper Scissors")
tk.Label(root, text="Rock, Paper, Scissors Game", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)
root.mainloop()