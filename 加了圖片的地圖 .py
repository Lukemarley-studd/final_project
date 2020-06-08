import tkinter as tk

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create()

    def create(self):  # 外圈圖片及內圈格子
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
        self.picture08= tk.Label(self, height=6, width=20)
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
        self.picture18= tk.Label(self, height=6, width=20)
        self.picture18.grid(row=0, column=1)
        self.picture19= tk.Label(self, height=6, width=20)
        self.picture19.grid(row=0, column=6)
        self.picture20= tk.Label(self, height=6, width=20)
        self.picture20.grid(row=1, column=0)
        self.picture21= tk.Label(self, height=6, width=20)
        self.picture21.grid(row=1, column=7)
        self.picture22= tk.Label(self, height=6, width=20)
        self.picture22.grid(row=5, column=0)
        self.picture23= tk.Label(self, height=6, width=20)
        self.picture23.grid(row=5, column=7)
        self.picture24= tk.Label(self, height=6, width=20)
        self.picture24.grid(row=6, column=1)
        self.picture25= tk.Label(self, height=6, width=20)
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
        
        score_1 = 0
        """
        改變玩家1的學分數
        """
        
        self.score_variable_1 = tk.StringVar(self, f'★ credits: {score_1}')
        self.score_lbl = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_1, font=('Arial', 12))
        self.score_lbl.place(x = 320, y = 230)
        
        score_2 = 0
        """
        #改變玩家2的學分數
        """
        self.score_variable_2 = tk.StringVar(self, f'❤ credits: {score_2}')
        self.score_lb2 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_2, font=('Arial', 12))
        self.score_lb2.place(x = 320, y = 280)

        #如果有玩家三
        score_3 = 0
        
        #改變玩家3的學分數
          
        self.score_variable_3 = tk.StringVar(self, f'✿ credits: {score_3}')
        self.score_lb3 = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_3, font=('Arial', 12))
        self.score_lb3.place(x = 320, y = 330)
        
        """
        如果有玩家四
        """
        
        score_4 = 0
        """
        改變玩家4的學分數
        """
        self.score_variable_4 = tk.StringVar(self, f'😀 credits: {score_4}')
        self.score_lb4 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_4, font=('Arial', 12))
        self.score_lb4.place(x = 320, y = 380)
        

game = Game()
game.mainloop()