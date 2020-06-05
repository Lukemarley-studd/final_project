import tkinter as tk
import random

Dice = tk.Tk()  # 主視窗
Dice.geometry("350x350")
Dice.title("骰子")

label = tk.Label(Dice, text = "", font = ("Helvetica", 300))

def roll_dice():
    dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    steps = f"{random.choice(dice)}"
    step_num = int()
    if steps == "\u2680":
        step_num = 1
    elif steps == "\u2681":
        step_num = 2
    elif steps == "\u2682":
        step_num = 3
    elif steps == "\u2683":
        step_num = 4
    elif steps == "\u2684":
        step_num = 5
    elif steps == "\u2685":
        step_num = 6
    print(step_num)               
    label.configure(text = steps)
    label.pack()


button = tk.Button(Dice, text = "擲骰子", height = 5, width = 15, foreground = "red", command = roll_dice)
button.pack()

Dice.mainloop()