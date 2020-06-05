import tkinter as tk

Root = tk.Tk()

Root.title("學分榜")
Root.geometry("300x300")

score_1 = 0
"""
改變玩家1的學分數
"""
score_variable_1 = tk.StringVar(Root, f'Player 1 credits: {score_1}')
score_lbl = tk.Label(Root, textvariable = score_variable_1)
score_lbl.config(font = (50))
score_lbl.pack()

score_2 = 0
"""
改變玩家2的學分數
"""
score_variable_2 = tk.StringVar(Root, f'Player 2 credits: {score_2}')
score_lb2 = tk.Label(Root, textvariable = score_variable_2)
score_lb2.config(font = (50))
score_lb2.pack()

score_3 = 0
"""
改變玩家3的學分數
"""
score_variable_3 = tk.StringVar(Root, f'Player 3 credits: {score_3}')
score_lb3 = tk.Label(Root, textvariable = score_variable_3)
score_lb3.config(font = (50))
score_lb3.pack()

score_4 = 0
"""
改變玩家4的學分數
"""
score_variable_4 = tk.StringVar(Root, f'Player 4 credits: {score_4}')
score_lb4 = tk.Label(Root, textvariable = score_variable_4)
score_lb4.config(font = (50))
score_lb4.pack()

Root.mainloop()
