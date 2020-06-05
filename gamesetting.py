import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkfont
from tkinter import ttk

class Window(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.create_widgets()


	def create_widgets(self):
		
		#建立物件
		font1 = tkfont.Font(size = 32, family = "Hei")
		self.space = tk.Label(self, height = 1, width = 1, text = ' ', bg = 'black')
		self.png1 = ImageTk.PhotoImage(file='1.png')
		self.lb1 = tk.Label(self, height = 200, width = 450, image = self.png1, bg = 'black')#台大大富翁
		self.png2 = ImageTk.PhotoImage(file='2.png')
		self.lb2 = tk.Label(self, height = 80, width = 700, image = self.png2, bg = 'black')#welcome to ntu
		self.numofuser = tk.Label(self, height = 1, width = 15, font = font1, text = "請選擇玩家人數：", bg = 'black', fg = 'white')
		radiovalue = tk.IntVar()
		self._2p = tk.Radiobutton(self, height = 1, width = 5, font = font1, text = "2人", variable = radiovalue, value = 2, command = self.click2users, bg = 'black', fg = 'white')
		self._3p = tk.Radiobutton(self, height = 1, width = 5, font = font1, text = "3人", variable = radiovalue, value = 3, command = self.click3users, bg = 'black', fg = 'white')
		self._4p = tk.Radiobutton(self, height = 1, width = 5, font = font1, text = "4人", variable = radiovalue, value = 4, command = self.click4users, bg = 'black', fg = 'white')
		self.player1 = tk.Label(self, height = 1, width = 10, font = font1, text = "玩家 1", bg = 'black', fg = 'white')
		self.player2 = tk.Label(self, height = 1, width = 10, font = font1, text = "玩家 2", bg = 'black', fg = 'white')
		self.player3 = tk.Label(self, height = 1, width = 10, font = font1, text = "玩家 3", bg = 'black', fg = 'white')
		self.player4 = tk.Label(self, height = 1, width = 10, font = font1, text = "玩家 4", bg = 'black', fg = 'white')
		colorlist1 = ['紅色', '橘色', '黃色', '綠色', '藍色', '紫色']
		colorlist2 = ['紅色', '橘色', '黃色', '綠色', '藍色', '紫色']
		colorlist3 = ['紅色', '橘色', '黃色', '綠色', '藍色', '紫色']
		colorlist4 = ['紅色', '橘色', '黃色', '綠色', '藍色', '紫色']
		self.choosecolor1 = ttk.Combobox(self, values = colorlist1, state = 'readonly')
		self.choosecolor2 = ttk.Combobox(self, values = colorlist2, state = 'readonly')
		self.choosecolor3 = ttk.Combobox(self, values = colorlist3, state = 'readonly')
		self.choosecolor4 = ttk.Combobox(self, values = colorlist4, state = 'readonly')
		self.startbtn = tk.Button(self, text = '開始！', bg = 'black', font = font1, command = self.start)  # 開始的按鈕
		
		#指定位置
		full = tk.NE + tk.SW
		up = tk.NE + tk.NW
		self.lb1.grid(row = 40, column = 0, columnspan = 5)
		self.lb2.grid(row = 41, column = 0, columnspan = 5, rowspan = 10)
		self.numofuser.grid(row = 80, column = 0, sticky = full)
		self._2p.grid(row = 80, column = 2, sticky = full)
		self._3p.grid(row = 80, column = 3, sticky = full)
		self._4p.grid(row = 80, column = 4, sticky = full)
		self.startbtn.grid(row = 90, column = 2, columnspan = 1)
		self.space.grid(row = 88, column = 0, rowspan = 1)


		#定義command
	def click2users(self):
		self.player1.grid(row = 82, column = 1)
		self.choosecolor1.grid(row = 83, column = 1)
		self.player2.grid(row = 82, column = 2)
		self.choosecolor2.grid(row = 83, column = 2)
		self.player3.grid_forget()
		self.choosecolor3.grid_forget()
		self.player4.grid_forget()
		self.choosecolor4.grid_forget()
	def click3users(self):
		self.player1.grid(row = 82, column = 1)
		self.choosecolor1.grid(row = 83, column = 1)
		self.player2.grid(row = 82, column = 2)
		self.choosecolor2.grid(row = 83, column = 2)
		self.player3.grid(row = 82, column = 3)
		self.choosecolor3.grid(row = 83, column = 3)
		self.player4.grid_forget()
		self.choosecolor4.grid_forget()
	def click4users(self):
		self.player1.grid(row = 82, column = 1)
		self.choosecolor1.grid(row = 83, column = 1)
		self.player2.grid(row = 82, column = 2)
		self.choosecolor2.grid(row = 83, column = 2)
		self.player3.grid(row = 82, column = 3)
		self.choosecolor3.grid(row = 83, column = 3)
		self.player4.grid(row = 82, column = 4)
		self.choosecolor4.grid(row = 83, column = 4)
	def start(self):  # 開始遊戲的指令
		global newframe
		mywindow.destroy()  # 刪掉起始畫面
		newframe = NewFrame()  # 創立（接）遊戲開始的畫面
		newframe.mainloop()




class NewFrame(tk.Frame):  # 遊戲開始的畫面
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.create_widgets()
	def create_widgets(self):#接遊戲開始後的畫面
		pass
		#以下測試用
		#self.png1 = ImageTk.PhotoImage(file='1.png')
		#self.lb1 = tk.Label(self, height = 200, width = 450, image = self.png1, bg = 'black')#台大大富翁
		#self.lb1.grid(row = 40, column = 0, columnspan = 5)

mywindow = Window()
mywindow.master.title("台大大富翁")
mywindow.configure(bg = 'black')

mywindow.mainloop()


'''
遊戲結束的畫面
'''
class GameOver(tk.Frame):
	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		#建立物件
		font1 = tkfont.Font(size = 32, family = "Hei")
		self.space = tk.Label(self, height = 1, width = 1, text = ' ', bg = 'black')
		self.gameoverpng = ImageTk.PhotoImage(file='gameover.png')
		self.gameover = tk.Label(self, height = 80, width = 700, image = self.gameoverpng, bg = 'black')#GameOver的圖片
		self.restartbtn = tk.Button(self, text = '重新開始！', bg = 'black', font = font1, command = self.restart_new_game)

		#指定位置
		self.gameover.grid(row = 41, column = 0, columnspan = 5, rowspan = 10)
		self.restartbtn.grid(row = 90, column = 2, columnspan = 1)
		self.space.grid(row = 88, column = 0, rowspan = 1)

		#定義command
	def restart_new_game(self):
		w.destroy()  # w為gameover畫面的代號，這裡是把gameover畫面去除的意思
		newgame = Window()  # 開始新的遊戲
		newgame.configure(bg = 'black')
		newgame.mainloop()

