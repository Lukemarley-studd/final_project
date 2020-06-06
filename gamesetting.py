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
        playerlist1 = [' ★ ', ' ❤ ', ' ✿ ', ' 😀 ']
        playerlist2 = [' ★ ', ' ❤ ', ' ✿ ', ' 😀 ']
        playerlist3 = [' ★ ', ' ❤ ', ' ✿ ', ' 😀 ']
        playerlist4 = [' ★ ', ' ❤ ', ' ✿ ', ' 😀 ']
        self.chooseplayer1 = ttk.Combobox(self, values = playerlist1, state = 'readonly')
        self.chooseplayer2 = ttk.Combobox(self, values = playerlist2, state = 'readonly')
        self.chooseplayer3 = ttk.Combobox(self, values = playerlist3, state = 'readonly')
        self.chooseplayer4 = ttk.Combobox(self, values = playerlist4, state = 'readonly')
        self.startbtn = tk.Button(self, text = '開始！', bg = 'black', font = font1, fg = 'white', command = self.start)  # 開始的按鈕

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
        self.chooseplayer1.grid(row = 83, column = 1)
        self.player2.grid(row = 82, column = 2)
        self.chooseplayer2.grid(row = 83, column = 2)
        self.player3.grid_forget()
        self.chooseplayer3.grid_forget()
        self.player4.grid_forget()
        self.choosecolor4.grid_forget()
    def click3users(self):
        self.player1.grid(row = 82, column = 1)
        self.chooseplayer1.grid(row = 83, column = 1)
        self.player2.grid(row = 82, column = 2)
        self.chooseplayer2.grid(row = 83, column = 2)
        self.player3.grid(row = 82, column = 3)
        self.chooseplayer3.grid(row = 83, column = 3)
        self.player4.grid_forget()
        self.chooseplayer4.grid_forget()
    def click4users(self):
        self.player1.grid(row = 82, column = 1)
        self.chooseplayer1.grid(row = 83, column = 1)
        self.player2.grid(row = 82, column = 2)
        self.chooseplayer2.grid(row = 83, column = 2)
        self.player3.grid(row = 82, column = 3)
        self.chooseplayer3.grid(row = 83, column = 3)
        self.player4.grid(row = 82, column = 4)
        self.chooseplayer4.grid(row = 83, column = 4)
        
    def start(self):  # 開始遊戲的指令
        global newframe
        mywindow.destroy()  # 刪掉起始畫面
        newframe = NewFrame()  # 創立（接）遊戲開始的畫面
        newframe.configure(bg='black')
        newframe.mainloop()



class NewFrame(tk.Frame):  # 遊戲開始的畫面
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()
    def create_widgets(self):#接遊戲開始後的畫面
        self.picture00Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\校門-0000.gif")
        self.picture00= tk.Label(self, height=90, width=135, image=self.picture00Image)
        self.picture00.grid(row=0, column=0)
        self.picture01Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\管院-0000.gif")
        self.picture01= tk.Label(self, height=90, width=135, image=self.picture01Image)
        self.picture01.grid(row=0, column=2)
        self.picture02Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\小福-0000.gif")
        self.picture02= tk.Label(self, height=90, width=135, image=self.picture02Image)
        self.picture02.grid(row=0, column=3)
        self.picture03Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\新體-0000.gif")
        self.picture03= tk.Label(self, height=90, width=135, image=self.picture03Image)
        self.picture03.grid(row=0, column=4)
        self.picture04Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\法學院-0000.gif")
        self.picture04= tk.Label(self, height=90, width=135, image=self.picture04Image)
        self.picture04.grid(row=0, column=5)
        self.picture05Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\文學院-0000.gif")
        self.picture05= tk.Label(self, height=90, width=135, image=self.picture05Image)
        self.picture05.grid(row=0, column=7)
        self.picture06Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\電資學院-0000.gif")
        self.picture06= tk.Label(self, height=90, width=135, image=self.picture06Image)
        self.picture06.grid(row=2, column=7)
        self.picture07Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\活大-0000.gif")
        self.picture07= tk.Label(self, height=90, width=135, image=self.picture07Image)
        self.picture07.grid(row=3, column=7)
        self.picture08= tk.Label(self, height=6, width=20, bg='black')
        self.picture08.grid(row=4, column=7)
        self.picture09Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\社科院-0000.gif")
        self.picture09= tk.Label(self, height=90, width=135, image=self.picture09Image)
        self.picture09.grid(row=6, column=7)
        self.picture10Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\理學院-0000.gif")
        self.picture10= tk.Label(self, height=90, width=135, image=self.picture10Image)
        self.picture10.grid(row=6, column=5)
        self.picture11Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\醫學院-0000.gif")
        self.picture11= tk.Label(self, height=90, width=135, image=self.picture11Image)
        self.picture11.grid(row=6, column=4)
        self.picture12Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\宿舍-0000.gif")
        self.picture12= tk.Label(self, height=90, width=135, image=self.picture12Image)
        self.picture12.grid(row=6, column=3)
        self.picture13Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\計中-0000.gif")
        self.picture13= tk.Label(self, height=90, width=135, image=self.picture13Image)
        self.picture13.grid(row=6, column=2)
        self.picture14Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\總圖-0000.gif")
        self.picture14= tk.Label(self, height=90, width=135, image=self.picture14Image)
        self.picture14.grid(row=6, column=0)
        self.picture15Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\醉月湖-0000.gif")
        self.picture15= tk.Label(self, height=90, width=135, image=self.picture15Image)
        self.picture15.grid(row=4, column=0)
        self.picture16Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\傅鐘-0000.gif")
        self.picture16= tk.Label(self, height=90, width=135, image=self.picture16Image)
        self.picture16.grid(row=3, column=0)
        self.picture17Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\水源-0000.gif")
        self.picture17= tk.Label(self, height=90, width=135, image=self.picture17Image)
        self.picture17.grid(row=2, column=0)
        self.picture18= tk.Label(self, height=6, width=20, bg='black')
        self.picture18.grid(row=0, column=1)
        self.picture19= tk.Label(self, height=6, width=20, bg='black')
        self.picture19.grid(row=0, column=6)
        self.picture20= tk.Label(self, height=6, width=20, bg='black')
        self.picture20.grid(row=1, column=0)
        self.picture21= tk.Label(self, height=6, width=20, bg='black')
        self.picture21.grid(row=1, column=7)
        self.picture22= tk.Label(self, height=6, width=20, bg='black')
        self.picture22.grid(row=5, column=0)
        self.picture23= tk.Label(self, height=6, width=20, bg='black')
        self.picture23.grid(row=5, column=7)
        self.picture24= tk.Label(self, height=6, width=20, bg='black')
        self.picture24.grid(row=6, column=1)
        self.picture25= tk.Label(self, height=6, width=20, bg='black')
        self.picture25.grid(row=6, column=6)

        text_list = ['校門\n\n', '管院\n\n', '小福\n\n', '新體\n\n', '法學院\n\n', '文學院\n\n', '電資學院\n\n',
                    '活大\n\n', '機會/命運\n\n', '社科院\n\n', '理學院\n\n', '醫學院\n\n', '宿舍\n\n',
                    '計中\n\n', '總圖\n\n', '醉月湖\n\n', '傅鐘\n\n', '水源校區\n\n']
        self.place00 = tk.Label(self, height=5, width=16, bg='sky blue', text=text_list[0], fg='white', font=('Arial', 12))
        self.place00.grid(row=1, column=1)
        self.place01 = tk.Label(self, height=5, width=15, bg='pink2', text=text_list[1], fg='white', font=('Arial', 12))
        self.place01.grid(row=1, column=2)
        self.place02 = tk.Label(self, height=5, width=15, bg='sky blue', text=text_list[2], fg='white', font=('Arial', 12))
        self.place02.grid(row=1, column=3)
        self.place03 = tk.Label(self, height=5, width=15, bg='pink2', text=text_list[3], fg='white', font=('Arial', 12))
        self.place03.grid(row=1, column=4)
        self.place04 = tk.Label(self, height=5, width=15, bg='sky blue', text=text_list[4], fg='white', font=('Arial', 12))
        self.place04.grid(row=1, column=5)
        self.place05 = tk.Label(self, height=5, width=16, bg='pink2', text=text_list[5], fg='white', font=('Arial', 12))
        self.place05.grid(row=1, column=6)
        self.place06 = tk.Label(self, height=5, width=16, bg='sky blue', text=text_list[6], fg='white', font=('Arial', 12))
        self.place06.grid(row=2, column=6)
        self.place07 = tk.Label(self, height=5, width=16, bg='pink2', text=text_list[7], fg='white', font=('Arial', 12))
        self.place07.grid(row=3, column=6)
        self.place08 = tk.Label(self, height=5, width=16, bg='sky blue', text=text_list[8], fg='white', font=('Arial', 12))
        self.place08.grid(row=4, column=6)
        self.place09 = tk.Label(self, height=5, width=16, bg='pink2', text=text_list[9], fg='white', font=('Arial', 12))
        self.place09.grid(row=5, column=6)
        self.place10 = tk.Label(self, height=5, width=15, bg='sky blue', text=text_list[10], fg='white', font=('Arial', 12))
        self.place10.grid(row=5, column=5)
        self.place11 = tk.Label(self, height=5, width=15, bg='pink2', text=text_list[11], fg='white', font=('Arial', 12))
        self.place11.grid(row=5, column=4)
        self.place12 = tk.Label(self, height=5, width=15, bg='sky blue', text=text_list[12], fg='white', font=('Arial', 12))
        self.place12.grid(row=5, column=3)
        self.place13 = tk.Label(self, height=5, width=15, bg='pink2', text=text_list[13], fg='white', font=('Arial', 12))
        self.place13.grid(row=5, column=2)
        self.place14 = tk.Label(self, height=5, width=16, bg='sky blue', text=text_list[14], fg='white', font=('Arial', 12))
        self.place14.grid(row=5, column=1)
        self.place15 = tk.Label(self, height=5, width=16, bg='pink2', text=text_list[15], fg='white', font=('Arial', 12))
        self.place15.grid(row=4, column=1)
        self.place16 = tk.Label(self, height=5, width=16, bg='sky blue', text=text_list[16], fg='white', font=('Arial', 12))
        self.place16.grid(row=3, column=1)
        self.place17 = tk.Label(self, height=5, width=16, bg='pink2', text=text_list[17], fg='white', font=('Arial', 12))
        self.place17.grid(row=2, column=1)
        # pass
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

