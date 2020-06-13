import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkfont
from tkinter import ttk
import random

chooseplayerdict = dict()
n = 0
result = False  # 紀錄答題的結果
penalty = False # 有沒有被扣分
class Window(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #建立物件
        font1 = tkfont.Font(size = 20, family = "Arial")
        self.space = tk.Label(self, height = 1, width = 1, text = ' ')
        self.space2 = tk.Label(self, height = 1, width = 20, text = '')
        png = Image.open('1.png')
        png = png.resize((499, 169), Image.ANTIALIAS)
        self.png1 = ImageTk.PhotoImage(png)
        self.lb1 = tk.Label(self, height = 200, width = 600, image = self.png1)#台大大富翁
        png = Image.open('2.png')
        png = png.resize((539, 112), Image.ANTIALIAS)
        self.png2 = ImageTk.PhotoImage(png)
        self.lb2 = tk.Label(self, height = 100, width = 600, image = self.png2)#welcome to ntu
        self.numofuser = tk.Label(self, height = 1, width = 15, font = font1, text = "請選擇玩家人數：")
        radiovalue = tk.IntVar()
        self._2p = tk.Radiobutton(self, height = 1, width = 5, font = font1, text = "2人", variable = radiovalue, value = 2, command = self.click2users)
        self._3p = tk.Radiobutton(self, height = 1, width = 5, font = font1, text = "3人", variable = radiovalue, value = 3, command = self.click3users)
        self._4p = tk.Radiobutton(self, height = 1, width = 5, font = font1, text = "4人", variable = radiovalue, value = 4, command = self.click4users)
        self.player1 = tk.Label(self, height = 1, width = 10, font = font1, text = "玩家 1")
        self.player2 = tk.Label(self, height = 1, width = 10, font = font1, text = "玩家 2")
        self.player3 = tk.Label(self, height = 1, width = 10, font = font1, text = "玩家 3")
        self.player4 = tk.Label(self, height = 1, width = 10, font = font1, text = "玩家 4")
        global playerlist
        playerlist = [' ★ ', ' ❤ ', ' ✿ ', ' 😀 ']
        self.chooseplayer1 = ttk.Combobox(self, values = playerlist, state = 'readonly')
        self.chooseplayer1.bind('<<ComboboxSelected>>', self.comboclick1)
        self.chooseplayer2 = ttk.Combobox(self, values = playerlist, state = 'readonly')
        self.chooseplayer2.bind('<<ComboboxSelected>>', self.comboclick2)
        self.chooseplayer3 = ttk.Combobox(self, values = playerlist, state = 'readonly')
        self.chooseplayer3.bind('<<ComboboxSelected>>', self.comboclick3)
        self.chooseplayer4 = ttk.Combobox(self, values = playerlist, state = 'readonly')
        self.chooseplayer4.bind('<<ComboboxSelected>>', self.comboclick4)
        self.startbtn = tk.Button(self, text = '開始！', font = font1, command = self.start)  # 開始的按鈕
        self.gamerulebtn = tk.Button(self, text = '遊戲規則', font = font1, command = self.viewgamerule)  # 遊戲規則的按鈕
        self.warning = tk.Label(self, height = 1, width = 50, font = font1, text = "請重新選擇玩家(因重複選取或未選取)", bg = 'red4', fg = 'white')

        #指定位置
        full = tk.NE + tk.SW
        up = tk.NE + tk.NW
        self.lb1.grid(row = 0, column = 1, columnspan = 4)
        self.lb2.grid(row = 1, column = 1, columnspan = 5, rowspan = 10)
        self.numofuser.grid(row = 13, column = 0, sticky = full)
        self._2p.grid(row = 13, column = 2, sticky = full)
        self._3p.grid(row = 13, column = 3, sticky = full)
        self._4p.grid(row = 13, column = 4, sticky = full)
        self.startbtn.grid(row = 25, column = 2, columnspan = 1)
        self.gamerulebtn.grid(row = 25, column = 3)
        self.space.grid(row = 12, column = 0, rowspan = 1)
        self.space2.grid(row = 30, column = 6, columnspan = 3)

        #定義command
    def click2users(self):
        self.player1.grid(row = 14, column = 1)
        self.chooseplayer1.grid(row = 15, column = 1)
        self.player2.grid(row = 14, column = 2)
        self.chooseplayer2.grid(row = 15, column = 2)
        self.player3.grid_forget()
        self.chooseplayer3.grid_forget()
        self.player4.grid_forget()
        self.chooseplayer4.grid_forget()
        global n
        n = 2
    def click3users(self):
        self.player1.grid(row = 14, column = 1)
        self.chooseplayer1.grid(row = 15, column = 1)
        self.player2.grid(row = 14, column = 2)
        self.chooseplayer2.grid(row = 15, column = 2)
        self.player3.grid(row = 14, column = 3)
        self.chooseplayer3.grid(row = 15, column = 3)
        self.player4.grid_forget()
        self.chooseplayer4.grid_forget()
        global n
        n = 3
    def click4users(self):
        self.player1.grid(row = 14, column = 1)
        self.chooseplayer1.grid(row = 15, column = 1)
        self.player2.grid(row = 14, column = 2)
        self.chooseplayer2.grid(row = 15, column = 2)
        self.player3.grid(row = 14, column = 3)
        self.chooseplayer3.grid(row = 15, column = 3)
        self.player4.grid(row = 14, column = 4)
        self.chooseplayer4.grid(row = 15, column = 4)
        global n
        n = 4


    def comboclick1(self, event):
        p1label = self.chooseplayer1.get()
        self.playerlabel1 = tk.Label(self, text = p1label)
        chooseplayerdict['player1'] = p1label
    def comboclick2(self, event):
        p2label = self.chooseplayer2.get()
        self.playerlabel2 = tk.Label(self, text = p2label)
        chooseplayerdict['player2'] = p2label
    def comboclick3(self, event):
        p3label = self.chooseplayer3.get()
        self.playerlabel3 = tk.Label(self, text = p3label)
        chooseplayerdict['player3'] = p3label
    def comboclick4(self, event):
        p4label = self.chooseplayer4.get()
        self.playerlabel4 = tk.Label(self, text = p4label)
        chooseplayerdict['player4'] = p4label

    def check_repeated_and_empty(self, chooseplayerdict):
        players = list(chooseplayerdict.values())
        for i in players:
            if players.count(i) != 1 or len(players) != n:
                return False
            else:
                return True

    def viewgamerule(self):
        global GAMERULE
        GAMERULE = GameRuleWindow()
        GAMERULE.mainloop()

    def start(self):  # 開始遊戲的指令
        if self.check_repeated_and_empty(chooseplayerdict) == True:
            global newframe
            mywindow.destroy()  # 刪掉起始畫面
            newframe = NewFrame()  # 創立（接）遊戲開始的畫面
            newframe.mainloop()
        else:
            self.warning.grid(row = 27, column = 1, columnspan = 5)


class GameRuleWindow(tk.Toplevel):  # 遊戲規則的視窗
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        font1 = tkfont.Font(size = 18, family = "Arial")
        font2 = tkfont.Font(size = 22, family = "Arial", weight = 'bold')
        png = Image.open('gamerule.png')
        png = png.resize((179, 53), Image.ANTIALIAS)
        self.png1 = ImageTk.PhotoImage(png)
        self.title = tk.Label(self, height = 100, width = 600, image = self.png1)#遊戲規則
        self.intro = tk.Label(self, height = 1, width = 70, font = font2, text = '這是一款大富翁遊戲，玩家們將進入台大並以獲得20學分為目標，開始搶救學分大作戰！')
        self.lb1 = tk.Label(self, height = 1, width = 54, font = font1, text = '1. 遊戲開始前，請各位玩家先選擇人數以及各自代表的符號（不重複）')
        self.lb2 = tk.Label(self, height = 1, width = 45, font = font1, text = '2. 以校門口為起點，玩家們依序擲骰子進行遊戲（ROLL）')
        self.lb3 = tk.Label(self, height = 1, width = 80, font = font1, text = '3. 到達各地點後，必須回答問題才能獲得學分，回答完畢必須更新才能拿到學分並繼續遊戲（UPDATE）')
        self.lb4 = tk.Label(self, height = 1, width = 29, font = font1, text = '4. 先獲得20學分者獲勝，並結束遊戲')

        self.title.grid(row = 0, column = 20)
        self.intro.grid(row = 2, column = 0, columnspan = 70)
        self.lb1.grid(row = 3, column = 0, columnspan = 54, sticky = tk.W)
        self.lb2.grid(row = 4, column = 0, columnspan = 45, sticky = tk.W)
        self.lb3.grid(row = 5, column = 0, columnspan = 80, sticky = tk.W)
        self.lb4.grid(row = 6, column = 0, columnspan = 29, sticky = tk.W)

'''
遊戲結束的畫面
'''
class GameOverWindow(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # 建立物件
        font1 = tkfont.Font(size = 28, family = "Arial")
        self.space = tk.Label(self, height = 1, width = 1, text = ' ')
        self.gameoverpng = ImageTk.PhotoImage(file='gameover.png')
        self.gameover = tk.Label(self, height = 130, width = 700, image = self.gameoverpng)#GameOver的圖片
        if score_1 >= 20:
            winner = 'The winner is PLAYER 1 !'
        elif score_2 >= 20:
            winner = 'The winner is PLAYER 2 !'
        elif score_3 >= 20:
            winner = 'The winner is PLAYER 3 !'
        else:
            winner = 'The winner is PLAYER 4 !'
        self.winner = tk.Label(self, height = 1, width = 40, font = font1, text = winner)
        self.restartbtn = tk.Button(self, text = '重新開始！', font = font1, command = self.restart_new_game)

        # 指定位置
        self.gameover.grid(row = 0, column = 0, columnspan = 40, rowspan = 5)
        self.winner.grid(row = 6, column = 10, columnspan = 10)
        self.restartbtn.grid(row = 9, column = 15, columnspan = 1)
        self.space.grid(row = 8, column = 0, rowspan = 1)

        # 定義command
    def restart_new_game(self):
        global GAMEOVER
        GAMEOVER.destroy()
        newgame = Window()  # 開始新的遊戲
        newgame.mainloop()


class Problems:
    def __init__(self):  # 題庫
        p0 = [["台大校門屬於哪個等級的古蹟？\n\nA.國定古蹟  B.直轄市定古蹟  C.縣（市）定古蹟  D.不是古蹟", "B"],
              ["校門中間的「國立臺灣大學」字樣是由誰題字的？\n\nA.朱家驊  B.梅貽琦  C.曾志朗  D.杜正勝", "A"],
              ["椰林大道有幾棵椰子樹？\n\nA.200  B.201  C.202  D.203", "B"],
              ["傅園內的斯年堂為何種建築風格？\n\nA.巴洛克  B.哥德式  C.日式  D.古希臘", "D"],
              ["台大校門於下列哪個時間建造？\n\nA.1911~1920  B.1921~1930  C.1931~1940  D.1941~1950", "C"],
              ["\"靠近傅園一側的XX樹也是臺大學生相約等人的目標，常常以「大門口第幾棵XX樹下集合」相互約定\"，\n\n請問引文所說的XX樹指的是下列何者？\n\nA.蒲葵樹  B.椰子樹  C.櫻花樹  D.朱槿樹", "A"]]
        p1 = [["管理學院的院長是？\n\nA.管中閔  B.胡星陽  C.陳家麟  D.劉順仁", "B"],
              ["管院的系辦都在？\n\nA.管一  B.管二  C.管圖  D.教研館", "A"],
              ["哪個不是台大管院的系？\n\nA.工管  B.經濟  C.國企  D.資管", "B"],
              ["以下哪個球隊是隸屬於管院而非單獨系所？\n\nA.桌球  B.羽球  C.壘球  D.網球", "D"],
              ["下列何者不是台大管院的前身？\n\nA.臺灣總督府高等商業學校  B.臺灣省立臺北商業專科學校\n\nC.臺灣省立商學院  D.臺北經濟專門學校", "C"],
              ["請問臺大EMBA的EMBA是指什麼？\n\nA.管理學院職涯規劃學程  B.管理學院碩士在職專班\n\nC.管理學院在職訓練專班  D.管理學院商業在職專班", "B"]]
        p2 = [["下列地點何者沒有出現在Coco臺大店的菜單中？\n\nA.椰林大道  B.總圖  C.醉月湖  D.陳三鼎", "B"],
              ["小福沒有下列哪個店家? \n\nA.摩斯  B.金興發  C.文湯武醬  D.八方雲集", "D"],
              ["下列哪一種食物包含在小福最受歡迎的餐點「摩斯特餐」裡？\n\nA.薯條  B.雞塊  C.蘑菇湯  D.薯餅", "D"],
              ["請問小福郵局有幾台ATM？\n\nA.1  B.2  C.3  D.4", "D"],
              ["小福摩斯星期六的營業時間到幾點？\n\nA.14:30  B.15:30  C.19:30  D 20:30", "B"],
              ["小福沒有下列哪個店家？\n\nA.比斯多  B. All pass 食堂  C.電腦先生  D.金閣屋", "D"]]
        p3 = [["新體裡面沒有哪項設備？\n\nA.游泳池  B.健身房  C.壁球室  D.攀岩場", "D"],
              ["學生使用健身房的年費為多少錢？\n\nA.$1100  B.$1200  C.$1350  D.$1500", "C"],
              ["新體的健身房在哪一層樓？\n\nA.B1  B.1F  C.2F  D.3F", "A"],
              ["新體室內游泳池最適人數為幾人？\n\nA.28  B.32  C.36  D.42", "D"],
              ["請問新體的電話號碼是幾號？\n\nA.(02)3366-5959  B.(02)3636-5959  C.(02)3666-5999  D.(02)3399-5566", "A"],
              ["請問新體哪一天晚上最早閉館？\n\nA.星期一  B.星期二  C.星期六  D.星期天", "D"]]
        p4 = [["法圖位在哪一個館？\n\nA.霖澤館  B.辛亥館  C.裏新館  D.萬才館", "D"],
              ["何者為法律系雙轉輔考試的考試科目？\n\nA.刑總  B.民總  C.著作權法  D.行政法", "B"],
              ["法學院設有幾個研究中心?\n\nA.9  B.11  C.14  D.17", "C"],
              ["下列何者並非台大法律系畢業？\n\nA.吳淡如  B.吳敦義  C.葉俊榮  D.黃國昌", "B"],
              ["以下何者不是台大法學院的研究中心？\n\nA.公法學中心  B.民事法學中心  C.商事法學中心  D.資訊法學中心", "D"],
              ["法律學院圖書館於幾年開始正式對外營運？\n\nA.2008  B.2009  C.2010  D.2011", "B"]]
        p5 = [["目前文學院大學部共有幾個系？\n\nA.6  B.7  C.8  D.9", "C"],
              ["下列哪一個文學院的學系是最晚成立的？\n\nA.戲劇系  B.圖資系  C.人類系  D.日文系", "A"],
              ["下列哪一個名人不是台大文學院畢業的？\n\nA.李敖  B.白先勇  C.余光中  D.李家同", "D"],
              ["下列哪個文學院的科系有自己的獨立系館？\n\nA.歷史系  B.圖資系  C.日文系  D.外文系", "B"],
              ["請問文學院下列獎學金何者金額最高？\n\nA.許倬雲院士暨夫人論文獎學金  B.鄭因百教授紀念獎學金\n\nC.校友文化基金會獎學金  D.美國北加州校友會劉氏獎學金", "D"],
              ["文學院沒有哪個研究中心？\n\nA.佛學研究中心  B.臺灣研究中心  C.日本研究中心  D.台灣海峽研究中心", "D"]]
        p6 = [["何者為資工系館？\n\nA.博理館  B.德田館  C.資訊館  D.工程館", "B"],
              ["電機系學習的是何種程式語言？\n\nA.Python  B.C++  C.C  D.Java", "A"],
              ["哪個活動不是電資學院一起舉辦的？\n\nA.嘉年華  B.野台  C.宿營  D.體育競賽", "C"],
              ["國立臺灣大學電機資訊學院的英文縮寫是什麼？\n\nA.EESC B.EECS C.ECES D.ESEC", "B"],
              ["請問電資學院目前院長或副院長有幾位是生理女性？\n\nA.0  B.1  C.3  D.5", "B"],
              ["請問下列電資學院教授何者在2019年榮獲國際重要學會學士(Fellow)？\n\nA.劉致為  B.陳怡然  C.黃升龍  D.林恭如", "C"]]
        p7 = [["活大禮堂的別稱為？\n\nA.僑光堂  B.怡仁堂  C.冠德堂  D.仁德堂", "B"],
              ["活大麥當勞幾點開始營業？\n\nA.6:00  B.7:00  C.8:00  D.9:00", "B"],
              ["活大的建築設計師是？\n\nA.李顯榮  B.王大閎  C.黃聲遠  D.陳仁和", "B"],
              ["活大內的便利商店是哪一家？\n\nA.全家  B.7-11  C.OK  D.萊爾富", "D"],
              ["下列哪個社團的社辦在活大？\n\nA.魔術社  B.薇友會  C.烏克麗麗社  D.咖啡社", "C"],
              ["下列哪個不是活大的店家？\n\nA.四海遊龍  B.比斯多  C.韓風小舖  D.阿諾廚房", "B"]]
        p8 = ["獲得椰林小舖發放的優惠券一張，多2學分",
              "得到管爺青睞，多2學分",
              "想耍帥放雙手騎車，結果烙賽扑街，少2學分",
              "腳踏車被水源阿伯拖走了，少2學分",
              "修到一門很硬的課，決定停修，少2學分",
              "想停休但超過停休截止時間，少2學分"]
        p9 = [["社科圖的別稱是_____先生紀念圖書館？\n\nA.辜振甫  B.辜顯榮  C.辜寬敏  D.辜仲諒", "A"],
              ["社科圖平日幾點閉館？\n\nA.21:00  B.21:30  C.22:00  D.22:30", "C"],
              ["社科圖落成時由董陽孜女士哪段文字作為勗勉？\n\nA.持之以恆  B.學而第一  C.百年樹人  D.奮發向上", "B"],
              ["下列著名建築師何者為社科院的設計者？\n\nA.安藤忠雄  B.貝聿銘  C.伊東豊雄  D.王大閎", "C"],
              ["下列哪一個科系不隸屬於社科院？\n\nA. 圖資  B.經濟  C.社工  D.政治", "A"],
              ["下列哪個台大畢業的政治人物不是社科院畢業的？\n\nA.李登輝  B.江宜樺  C.丁守中  D.連戰", "A"]]
        p10 = [["台大理學院剛創立的時候沒有哪個系?\n\nA.化學  B.生物  C.農學  D.物理", "D"],
              ["台大理學院院辦在哪裡?\n\nA.思亮館  B.天文數學館  C.積學館  D.浩瀚樓", "A"],
              ["中華民國哪位諾貝爾獎得主是台大理學院校友?\n\nA.丁肇中  B.李遠哲  C.李政道  D.楊振寧", "B"],
              ["請問天文數學館中哪個樓層為中研院所管？\n\nA.1  B.3  C.5  D.7", "D"],
              ["下列哪個計劃並沒有在理學院的計畫平台裡？\n\nA.邁向頂尖大學計畫  B.醉月湖平台計畫\n\nC.高教深耕計畫  D.迎接職場培訓計畫", "D"],
              ["理學院沒有哪個研究所？\n\nA.海洋研究所  B.天文物理研究所\nC.大氣資源與災害研究所  D.應用物理研究所", "C"]]
        p11 = [["下列科系何者隸屬於醫學院？\n\nA.物理治療學系  B.生命科學系  C.公共衛生學系  D.心理學系", "A"],
              ["醫學院的大門位於哪一條路上？\n\nA.徐州路  B.仁愛路  C.林森南路  D.中山南路", "B"],
              ["2020台大學生會會長選舉的哪位候選人是醫學院的?\n\nA.陳怡安  B.梁聖宇  C.楊子昂  D.以上皆非", "C"],
              ["醫學院大學部目前有幾個科系？\n\nA.6  B.7  C.8  D.9", "C"],
              ["醫學院的哪個研究中心屬於校級合作？\n\nA.基因體暨精準醫學研究中心  B.癌症研究中心\n\nC.藥物研究中心  D.實驗動物中心", "A"],
              ["台大醫學院網站右上角沒有什麼連結？\n\nA.捐款  B.台大醫院  C.台大癌醫  D.醫學圖書館", "C"]]
        p12 = [["哪個男宿不在總區？\n\nA.男一  B.男二  C.男七  D.男八", "B"],
              ["哪個男宿有影印店?\n\nA.男三  B.男五  C.男四  D.男一", "D"],
              ["總共有幾棟女生宿舍位於總區？\n\nA.6  B.7  C.8  D.9", "B"],
              ["男一B1的商店名稱是什麼？\n\nA.松田超商  B.男一福利社  C.勻福超商  D.松下超商", "C"],
              ["下列哪個宿舍房間學期宿費最貴？\n\nA.男五舍2樓  B.女六舍4樓  C.男研三舍1樓  D.女研三舍9樓", "D"],
              ["下列哪個宿舍沒有電梯？\n\nA.男八舍  B.男研一舍  C.女研一舍  D.女六舍", "B"]]
        p13 = [["計中影印室有安裝下列哪個軟體？\n\nA.Adobe photoshop cc  B. Python 3.8  C.Scratch2.0  D.WinRAR", "A"],
              ["計中每學期每人之免費列印配額為多少單位？\n\nA.50  B.100  C.150  D.200", "B"],
              ["計中黑白雙面列印9面要多少錢？\n\nA.6  B.7 C.8  D.9", "B"],
              ["如果違反計中規定(如攜入飲料、食物等)會被停止\n\n使用計算機中心各項服務多久？\n\nA. 一週  B.兩週  C.一個月  D.三個月", "C"],
              ["計中影印一次最多能印幾頁?\n\nA.15  B.30  C.45  D.60", "B"],
              ["計中沒有提供下列哪個雲端服務？\n\nA. NTU Cloud  B.G Suite  C.NTU Space  D.NTU Map", "D"]]
        p14 = [["下列哪一個不是圖書館？\n\nA.數圖  B.醫圖  C.管圖  D.社科圖", "C"],
              ["地下室自習室的哪一區開放使用電腦、滑鼠等發出聲響的裝置？\n\nA.A區  B.B區  C.AB兩區都可以  D.AB兩區都不行", "A"],
              ["台大大學部學生一次最多能借幾件圖書資料？\n\nA.20  B.40  C.60  D.80", "D"],
              ["請問總圖幾樓可以看電影？\n\nA.1  B.2  C.3  D.4", "D"],
              ["請問台大校友可以借閱視聽資料幾天？\n\nA.0  B.5  C.7  D.14", "A"],
              ["以下情況何者不屬於不能辦理續借的原因？\n\nA.所要續借圖書已逾期  B.所要續借之書已有他人預約\n\nC.借書讀者已被凍結停借  D.非持有學生證者", "D"]]
        p15 = [["下列哪一個是醉月湖的舊稱？\n\nA.大貝湖  B.梅花湖  C.小華湖  D.牛湳池", "D"],
              ["醉月湖先前是哪個水圳的調節池？\n\nA.曹公圳  B.瑠公圳  C.大坪林圳  D.八堡圳", "B"],
              ["醉月湖中央的亭子名稱為？\n\nA.湖心亭  B.觀音亭  C.獅子亭  D.益壽亭", "A"],
              ["醉月湖的平均水深約為多少？\n\nA.50cm  B.1m  C.2m  D.5m", "C"],
              ["如果在醉月湖看見白色的鳥類，最有可能是什麼？\n\nA.鵝  B.鴨  C.黑面琵鷺  D.雞", "B"],
              ["醉月湖旁的商店沒有販售什麼？\n\nA.咖啡  B.輕食  C.簡餐  D.烤鴨", "D"]]
        p16 = [["傅鐘一次敲響幾下？\n\nA.13  B.21  C.24  D.27", "B"],
              ["傅鐘是為了紀念下列哪個人物？\n\nA.傅斯年  B.傅崐萁  C.傅達仁  D.傅立葉", "A"],
              ["傅鐘在椰林大道上，在傅鐘對面的是哪一個學院？\n\nA.農學院  B.理學院  C.工學院  D.文學院", "D"],
              ["傅鐘有哪一項傳聞？\n\nA.21傳聞  B.31傳聞  C.脫魯傳聞  D.鬧鬼傳聞", "A"],
              ["最近拆傅鐘的傳聞是由哪裡傳出的？\n\nA.學務處  B.台大學生會  C.台大校友中心  D.校園轉型正義小組", "C"],
              ["傅鐘曾經是以人工敲打且每節下課敲一次，每次有幾響？\n\nA.21  B.22  C.23  D.24", "B"]]
        p17 = [["以下哪個系所不是位於水源校區？\n\nA.哲學系  B.人類學系  C.植物病理與微生物學系  D.以上皆是", "C"],
              ["只要你的腳踏車被水源阿伯拖超過__次後會開始罰錢？\n\nA.2  B.3  C.5  D.6", "B"],
              ["在水源對面的「台北水道水源地」的古蹟分級為？\n\nA.國家級古蹟  B.直轄市定古蹟  C.縣市級古蹟  D.不是古蹟", "B"],
              ["水源二手腳踏車沒有下列哪個價位？\n\nA.600  B.800  C.1000  D.1200", "C"],
              ["腳踏車被拖吊超出規定次數後每次罰款多少錢？\n\nA.50  B.100  C.150  D.200", "A"],
              ["下列哪個建築物在水源校區？\n\nA.食品科技館  B.鄭江樓  C.澄思樓  D.芳蘭大厝", "C"]]
        self.problem_list = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17]

    def call_a_problem(self, location):  # 隨機叫出該位置的一個問題或機會命運
        global result
        global penalty
        number = random.randint(0, len(self.problem_list[location]) - 1)
        if location != 8:
            problem = self.problem_list[location][number][0]
            correct_ans = self.problem_list[location][number][1]
            master(1, problem, correct_ans)
        else:
            chance_destiny = self.problem_list[location][number]
            master(0, chance_destiny)
            if number <= 1:  # 加2學分
                result = True
            else:  # 少2學分
                penalty = True


"""
紀錄四個玩家分數
"""
score_1 = score_2 = score_3 = score_4 = 0

dice_availible = True

class ProblemWindow(tk.Toplevel):  # 彈出問題的視窗
    def __init__(self, text, ans, root):
        tk.Toplevel.__init__(self)
        self.text = text
        self.ans = ans
        self.grid()
        self.createWidgets()
        self.root = root
        self.geometry("+%d+%d" % (350, 150))

    def createWidgets(self):
        self.buttonA = tk.Button(self, height = 4, width = 6, bg = "sky blue2", fg='white', font = "20", text = "A", command = self.click_buttonA)
        self.buttonB = tk.Button(self, height = 4, width = 6, bg = "sky blue3", fg='white', font = "20", text = "B", command = self.click_buttonB)
        self.buttonC = tk.Button(self, height = 4, width = 6, bg = "sky blue2", fg='white', font = "20", text = "C", command = self.click_buttonC)
        self.buttonD = tk.Button(self, height = 4, width = 6, bg = "sky blue3", fg='white', font = "20", text = "D", command = self.click_buttonD)
        global player, n
        print(player)
        if player == 1:
            self.lbProblem = tk.Label(self, height = 15, width = 55, bg='sky blue', fg='white', font = "20", text = 'Player1:\n\n'+self.text)
        elif player == 2:
            self.lbProblem = tk.Label(self, height = 15, width = 55, bg='sky blue', fg='white', font = "20", text = 'Player2:\n\n'+self.text)
        elif player == 3:
            self.lbProblem = tk.Label(self, height = 15, width = 55, bg='sky blue', fg='white', font = "20", text = 'Player3:\n\n'+self.text)
        else:
            self.lbProblem = tk.Label(self, height = 15, width = 55, bg='sky blue', fg='white', font = "20", text = 'Player4:\n\n'+self.text)
        self.buttonA.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.buttonB.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.buttonC.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
        self.buttonD.grid(row = 1, column = 3, sticky = tk.NE + tk.SW)
        self.lbProblem.grid(row = 0, column = 0, columnspan = 4, sticky = tk.NE + tk.SW)

    def click_buttonA(self):
        global player
        global result
        global penalty
        self.destroy()
        if self.ans == "A":
            self.root.switch_frame(ShowResult, "Correct!\n\n+2學分")
            result = True
        else:
            self.root.switch_frame(ShowResult, "Wrong!")
            result = False

    def click_buttonB(self):
        global player
        global result
        self.destroy()
        if self.ans == "B":
            self.root.switch_frame(ShowResult, "Correct!\n\n+2學分")
            result = True
        else:
            self.root.switch_frame(ShowResult, "Wrong!")
            result = False

    def click_buttonC(self):
        global player
        global result
        self.destroy()
        if self.ans == "C":
            self.root.switch_frame(ShowResult, "Correct!\n\n+2學分", )
            result = True
        else:
            self.root.switch_frame(ShowResult, "Wrong!")
            result = False

    def click_buttonD(self):
        global player        
        global result
        self.destroy()
        if self.ans == "D":
            self.root.switch_frame(ShowResult, "Correct!\n\n+2學分")
            result = True
        else:
            self.root.switch_frame(ShowResult, "Wrong!")
            result = False


class ShowResult(tk.Toplevel):  # 切換作答結果頁面
    def __init__(self, result, root):
        tk.Toplevel.__init__(self)
        self.text = result
        self.grid()
        self.createWidgets()
        self.root = root
        self.geometry("+%d+%d" % (350, 150))


    def createWidgets(self):
        self.lbResult = tk.Label(self, height = 15, width = 55, bg='sky blue', fg='white', font = "40", text = self.text)
        self.buttonSure = tk.Button(self, height = 2, width = 5, bg = "sky blue3", fg='white', font = "20", text = "確認", command = self.click_buttonSure)
        self.buttonSure.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.lbResult.grid(row = 0, column = 0, sticky = tk.NE + tk.SW)

    def click_buttonSure(self):
        self.destroy()


class ChanceDestinyWindow(tk.Toplevel):  # 彈出機會命運的視窗
    def __init__(self, text, root):
        tk.Toplevel.__init__(self)
        self.text = text
        self.grid()
        self.createWidgets()
        self.root = root
        self.geometry("+%d+%d" % (350, 150))

    def createWidgets(self):
        if player == 1:
            self.lbChance = tk.Label(self, height = 15, width = 55, bg='pink2', fg='white', font = "20", text = 'Player1:\n\n'+self.text)
        elif player == 2:
            self.lbChance = tk.Label(self, height = 15, width = 55, bg='pink2', fg='white', font = "20", text = 'Player2:\n\n'+self.text)
        elif player == 3:
            self.lbChance = tk.Label(self, height = 15, width = 55, bg='pink2', fg='white', font = "20", text = 'Player3:\n\n'+self.text)
        else:
            self.lbChance = tk.Label(self, height = 15, width = 55, bg='pink2', fg='white', font = "20", text = 'Player4:\n\n'+self.text)
        self.buttonSure = tk.Button(self, height = 2, width = 5,  bg='pink3', fg='white', font = "20", text = "確認", command = self.click_buttonSure)
        self.buttonSure.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.lbChance.grid(row = 0, column = 0, sticky = tk.NE + tk.SW)

    def click_buttonSure(self):
        self.destroy()


class master(tk.Tk):
    def __init__(self, frame_class, text1 = None, text2 = None):
        if frame_class == 1:
            self._frame = ProblemWindow(text1, text2, self)
        else:
            self.frame = ChanceDestinyWindow(text1, self)
    def switch_frame(self, frame_class, result):
        new_frame = frame_class(result, self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame



player = 1
player_loc_dict = {'player1':0, 'player2':0, 'player3':0, 'player4':0}


class NewFrame(tk.Frame):  # 遊戲開始的畫面
    def __init__(self):
        tk.Frame.__init__(self)
        self.problems = Problems()
        self.grid()
        self.create_widgets()


    def roll_dice(self):
        self.dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        self.steps = f"{random.choice(self.dice)}"
        self.step_num = int()
        if self.steps == "\u2680":
            self.step_num = 1
        elif self.steps == "\u2681":
            self.step_num = 2
        elif self.steps == "\u2682":
            self.step_num = 3
        elif self.steps == "\u2683":
            self.step_num = 4
        elif self.steps == "\u2684":
            self.step_num = 5
        elif self.steps == "\u2685":
            self.step_num = 6
        global player
        global player_loc_dict
        global dice_availible
        if player == 1:
            player_loc_dict['player1'] += self.step_num
            if player_loc_dict['player1'] > 17:
                player_loc_dict['player1'] -= 18
            self.problems.call_a_problem(player_loc_dict['player1'])
            player += 1
        elif player == 2:
            player_loc_dict['player2'] += self.step_num
            if player_loc_dict['player2'] > 17:
                player_loc_dict['player2'] -= 18
            self.problems.call_a_problem(player_loc_dict['player2'])
            player += 1
        elif player == 3:
            player_loc_dict['player3'] += self.step_num
            if player_loc_dict['player3'] > 17:
                player_loc_dict['player3'] -= 18
            self.problems.call_a_problem(player_loc_dict['player3'])
            player += 1
        else:
            player_loc_dict['player4'] += self.step_num
            if player_loc_dict['player4'] > 17:
                player_loc_dict['player4'] -= 18
            self.problems.call_a_problem(player_loc_dict['player4'])
            player += 1
        if player > n:
            player = 1
        print(player_loc_dict)
        self.label = tk.Label(self, text = self.steps, font = ("Helvetica", 120))
        self.label.place(x = 570, y = 200)
        dice_availible = False  # 不能按骰子
    def player_move(self, playerid):
        for i in range(18):
            if player_loc_dict[playerid] == i:
                place_list[i] += chooseplayerdict[playerid]
    """
    按分數更新後啟用dice的函式
    """
    def activate_dice(self):
        self.dice_button = tk.Button(self, text = "ROLL", height = 3, width = 7, foreground = "white", bg = "pink2", font=('Arial', 12), command=lambda:[self.roll_dice(), self.create_widgets()])
        self.dice_button.place(x = 460, y = 200)
    
    """
    這個函式用來更新原本的記分板
    """
    def change_score(self):
        global score_1
        global score_2
        global score_3
        global score_4
        global result
        global penalty

        if result == True:  
            if player == 2:
                score_1 += 2
                if chooseplayerdict['player1'] == " ★ ":
                    self.score_variable_1 = tk.StringVar(self, f'★ credits: {score_1}')
                elif chooseplayerdict['player1'] == ' ❤ ':
                    self.score_variable_1 = tk.StringVar(self, f'❤ credits: {score_1}')
                elif chooseplayerdict['player1'] == ' ✿ ':
                    self.score_variable_1 = tk.StringVar(self, f'✿ credits: {score_1}')
                elif chooseplayerdict['player1'] == ' 😀 ':
                    self.score_variable_1 = tk.StringVar(self, f'😀 credits: {score_1}')
                self.score_lb1 = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_1, font=('Arial', 12))
                self.score_lb1.place(x = 280, y = 190)
                if score_1 >= 20:
                    newframe.destroy()
                    global GAMEOVER
                    GAMEOVER = GameOverWindow()
                    GAMEOVER.mainloop()
            
            elif player == 3:
                score_2 += 2
                if chooseplayerdict['player2'] == ' ★ ':
                    self.score_variable_2 = tk.StringVar(self, f'★ credits: {score_2}')
                elif chooseplayerdict['player2'] == ' ❤ ':
                    self.score_variable_2 = tk.StringVar(self, f'❤ credits: {score_2}')
                elif chooseplayerdict['player2'] == ' ✿ ':
                    self.score_variable_2 = tk.StringVar(self, f'✿ credits: {score_2}')
                elif chooseplayerdict['player2'] == ' 😀 ':
                    self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_2}')
                self.score_lb2 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_2, font=('Arial', 12))
                self.score_lb2.place(x = 280, y = 240)
                if score_2 >= 20:
                    newframe.destroy()
                    GAMEOVER = GameOverWindow()
                    GAMEOVER.mainloop()

            elif player == 4:
                score_3 += 2
                if chooseplayerdict['player3'] == ' ★ ':
                    self.score_variable_3 = tk.StringVar(self, f'★ credits: {score_3}')
                elif chooseplayerdict['player3'] == ' ❤ ':
                    self.score_variable_3 = tk.StringVar(self, f'❤ credits: {score_3}')
                elif chooseplayerdict['player3'] == ' ✿ ':
                    self.score_variable_3 = tk.StringVar(self, f'✿ credits: {score_3}')
                elif chooseplayerdict['player3'] == ' 😀 ':
                    self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_3}')
                self.score_lb3 = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_3, font=('Arial', 12))
                self.score_lb3.place(x = 280, y = 290)
                if score_3 >= 20:
                    newframe.destroy()
                    GAMEOVER = GameOverWindow()
                    GAMEOVER.mainloop()
            elif player == 1:
                if n == 2:
                    score_2 += 2
                    if chooseplayerdict['player2'] == ' ★ ':
                        self.score_variable_2 = tk.StringVar(self, f'★ credits: {score_2}')
                    elif chooseplayerdict['player2'] == ' ❤ ':
                        self.score_variable_2 = tk.StringVar(self, f'❤ credits: {score_2}')
                    elif chooseplayerdict['player2'] == ' ✿ ':
                        self.score_variable_2 = tk.StringVar(self, f'✿ credits: {score_2}')
                    elif chooseplayerdict['player2'] == ' 😀 ':
                        self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_2}')
                    self.score_lb2 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_2, font=('Arial', 12))
                    self.score_lb2.place(x = 280, y = 240)
                    if score_2 >= 20:
                        newframe.destroy()
                        GAMEOVER = GameOverWindow()
                        GAMEOVER.mainloop()
                elif n == 3:
                    score_3 += 2
                    if chooseplayerdict['player3'] == ' ★ ':
                        self.score_variable_3 = tk.StringVar(self, f'★ credits: {score_3}')
                    elif chooseplayerdict['player3'] == ' ❤ ':
                        self.score_variable_3 = tk.StringVar(self, f'❤ credits: {score_3}')
                    elif chooseplayerdict['player3'] == ' ✿ ':
                        self.score_variable_3 = tk.StringVar(self, f'✿ credits: {score_3}')
                    elif chooseplayerdict['player3'] == ' 😀 ':
                        self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_3}')
                    self.score_lb3 = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_3, font=('Arial', 12))
                    self.score_lb3.place(x = 280, y = 290)
                    if score_3 >= 20:
                        newframe.destroy()
                        GAMEOVER = GameOverWindow()
                        GAMEOVER.mainloop()
                elif n == 4:
                    score_4 += 2
                    if chooseplayerdict['player4'] == ' ★ ':
                        self.score_variable_4 = tk.StringVar(self, f'★ credits: {score_4}')
                    elif chooseplayerdict['player4'] == ' ❤ ':
                        self.score_variable_4 = tk.StringVar(self, f'❤ credits: {score_4}')
                    elif chooseplayerdict['player4'] == ' ✿ ':
                        self.score_variable_4 = tk.StringVar(self, f'✿ credits: {score_4}')
                    elif chooseplayerdict['player4'] == ' 😀 ':
                        self.score_variable_4 = tk.StringVar(self, f'😀 credits: {score_4}')
                    self.score_lb4 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_4, font=('Arial', 12))
                    self.score_lb4.place(x = 280, y = 340)
                    if score_4 >= 20:
                        newframe.destroy()
                        GAMEOVER = GameOverWindow()
                        GAMEOVER.mainloop()
            result = False  # 把result改回來
        elif penalty == True:
            if player == 2:
                score_1 -= 2
                if score_1 < 0:
                    score_1 = 0

                if chooseplayerdict['player1'] == " ★ ":
                    self.score_variable_1 = tk.StringVar(self, f'★ credits: {score_1}')
                elif chooseplayerdict['player1'] == ' ❤ ':
                    self.score_variable_1 = tk.StringVar(self, f'❤ credits: {score_1}')
                elif chooseplayerdict['player1'] == ' ✿ ':
                    self.score_variable_1 = tk.StringVar(self, f'✿ credits: {score_1}')
                elif chooseplayerdict['player1'] == ' 😀 ':
                    self.score_variable_1 = tk.StringVar(self, f'😀 credits: {score_1}')
                self.score_lb1 = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_1, font=('Arial', 12))
                self.score_lb1.place(x = 280, y = 190)
            
            elif player == 3:
                score_2 -= 2
                if score_2 < 0:
                    score_2 = 0

                if chooseplayerdict['player2'] == ' ★ ':
                    self.score_variable_2 = tk.StringVar(self, f'★ credits: {score_2}')
                elif chooseplayerdict['player2'] == ' ❤ ':
                    self.score_variable_2 = tk.StringVar(self, f'❤ credits: {score_2}')
                elif chooseplayerdict['player2'] == ' ✿ ':
                    self.score_variable_2 = tk.StringVar(self, f'✿ credits: {score_2}')
                elif chooseplayerdict['player2'] == ' 😀 ':
                    self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_2}')
                self.score_lb2 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_2, font=('Arial', 12))
                self.score_lb2.place(x = 280, y = 240)

            elif player == 4:
                score_3 -= 2
                if score_3 < 0:
                    score_3 = 0

                if chooseplayerdict['player3'] == ' ★ ':
                    self.score_variable_3 = tk.StringVar(self, f'★ credits: {score_3}')
                elif chooseplayerdict['player3'] == ' ❤ ':
                    self.score_variable_3 = tk.StringVar(self, f'❤ credits: {score_3}')
                elif chooseplayerdict['player3'] == ' ✿ ':
                    self.score_variable_3 = tk.StringVar(self, f'✿ credits: {score_3}')
                elif chooseplayerdict['player3'] == ' 😀 ':
                    self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_3}')
                self.score_lb3 = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_3, font=('Arial', 12))
                self.score_lb3.place(x = 280, y = 290)
            elif player == 1:
                if n == 2:
                    score_2 -= 2
                    if score_2 < 0:
                        score_2 = 0

                    if chooseplayerdict['player2'] == ' ★ ':
                        self.score_variable_2 = tk.StringVar(self, f'★ credits: {score_2}')
                    elif chooseplayerdict['player2'] == ' ❤ ':
                        self.score_variable_2 = tk.StringVar(self, f'❤ credits: {score_2}')
                    elif chooseplayerdict['player2'] == ' ✿ ':
                        self.score_variable_2 = tk.StringVar(self, f'✿ credits: {score_2}')
                    elif chooseplayerdict['player2'] == ' 😀 ':
                        self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_2}')
                    self.score_lb2 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_2, font=('Arial', 12))
                    self.score_lb2.place(x = 280, y = 240)   
                elif n == 3:
                    score_3 -= 2
                    if score_3 < 0:
                        score_3 = 0

                    if chooseplayerdict['player3'] == ' ★ ':
                        self.score_variable_3 = tk.StringVar(self, f'★ credits: {score_3}')
                    elif chooseplayerdict['player3'] == ' ❤ ':
                        self.score_variable_3 = tk.StringVar(self, f'❤ credits: {score_3}')
                    elif chooseplayerdict['player3'] == ' ✿ ':
                        self.score_variable_3 = tk.StringVar(self, f'✿ credits: {score_3}')
                    elif chooseplayerdict['player3'] == ' 😀 ':
                        self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_3}')
                    self.score_lb3 = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_3, font=('Arial', 12))
                    self.score_lb3.place(x = 280, y = 290)                                                    
                elif n == 4:
                    score_4 -= 2
                    if score_4 < 0:
                        score_4 = 0

                    if chooseplayerdict['player4'] == ' ★ ':
                        self.score_variable_4 = tk.StringVar(self, f'★ credits: {score_4}')
                    elif chooseplayerdict['player4'] == ' ❤ ':
                        self.score_variable_4 = tk.StringVar(self, f'❤ credits: {score_4}')
                    elif chooseplayerdict['player4'] == ' ✿ ':
                        self.score_variable_4 = tk.StringVar(self, f'✿ credits: {score_4}')
                    elif chooseplayerdict['player4'] == ' 😀 ':
                        self.score_variable_4 = tk.StringVar(self, f'😀 credits: {score_4}')
                    self.score_lb4 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_4, font=('Arial', 12))
                    self.score_lb4.place(x = 280, y = 340)
            penalty = False  # 把penalty改回來

    def create_widgets(self):  # 接遊戲開始後的畫面

        # 外圈圖片
        self.picture00Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\校門-0000.gif")
        self.picture00= tk.Label(self, height=90, width=135, image=self.picture00Image)
        self.picture00.grid(row=0, column=0)
        self.picture01Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\管院-0000.gif")
        self.picture01= tk.Label(self, height=90, width=110, image=self.picture01Image)
        self.picture01.grid(row=0, column=2)
        self.picture02Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\小福-0000.gif")
        self.picture02= tk.Label(self, height=90, width=110, image=self.picture02Image)
        self.picture02.grid(row=0, column=3)
        self.picture03Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\新體-0000.gif")
        self.picture03= tk.Label(self, height=90, width=110, image=self.picture03Image)
        self.picture03.grid(row=0, column=4)
        self.picture04Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\法學院-0000.gif")
        self.picture04= tk.Label(self, height=90, width=110, image=self.picture04Image)
        self.picture04.grid(row=0, column=5)
        self.picture05Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\文學院-0000.gif")
        self.picture05= tk.Label(self, height=90, width=135, image=self.picture05Image)
        self.picture05.grid(row=0, column=7)
        self.picture06Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\電資學院-0000.gif")
        self.picture06= tk.Label(self, height=74, width=135, image=self.picture06Image)
        self.picture06.grid(row=2, column=7)
        self.picture07Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\活大-0000.gif")
        self.picture07= tk.Label(self, height=74, width=135, image=self.picture07Image)
        self.picture07.grid(row=3, column=7)
        self.picture08= tk.Label(self, height=3, width=16)
        self.picture08.grid(row=4, column=7)
        self.picture09Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\社科院-0000.gif")
        self.picture09= tk.Label(self, height=90, width=135, image=self.picture09Image)
        self.picture09.grid(row=6, column=7)
        self.picture10Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\理學院-0000.gif")
        self.picture10= tk.Label(self, height=90, width=110, image=self.picture10Image)
        self.picture10.grid(row=6, column=5)
        self.picture11Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\醫學院-0000.gif")
        self.picture11= tk.Label(self, height=90, width=110, image=self.picture11Image)
        self.picture11.grid(row=6, column=4)
        self.picture12Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\宿舍-0000.gif")
        self.picture12= tk.Label(self, height=90, width=110, image=self.picture12Image)
        self.picture12.grid(row=6, column=3)
        self.picture13Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\計中-0000.gif")
        self.picture13= tk.Label(self, height=90, width=110, image=self.picture13Image)
        self.picture13.grid(row=6, column=2)
        self.picture14Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\總圖-0000.gif")
        self.picture14= tk.Label(self, height=90, width=135, image=self.picture14Image)
        self.picture14.grid(row=6, column=0)
        self.picture15Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\醉月湖-0000.gif")
        self.picture15= tk.Label(self, height=74, width=135, image=self.picture15Image)
        self.picture15.grid(row=4, column=0)
        self.picture16Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\傅鐘-0000.gif")
        self.picture16= tk.Label(self, height=74, width=135, image=self.picture16Image)
        self.picture16.grid(row=3, column=0)
        self.picture17Image=tk.PhotoImage(file="C:\\Users\\User\\Documents\\GitHub\\final_project\\final圖片\\水源-0000.gif")
        self.picture17= tk.Label(self, height=74, width=135, image=self.picture17Image)
        self.picture17.grid(row=2, column=0)
        self.picture18= tk.Label(self, height=3, width=16)
        self.picture18.grid(row=0, column=1)
        self.picture19= tk.Label(self, height=3, width=16)
        self.picture19.grid(row=0, column=6)
        self.picture20= tk.Label(self, height=3, width=16)
        self.picture20.grid(row=1, column=0)
        self.picture21= tk.Label(self, height=3, width=16)
        self.picture21.grid(row=1, column=7)
        self.picture22= tk.Label(self, height=3, width=16)
        self.picture22.grid(row=5, column=0)
        self.picture23= tk.Label(self, height=3, width=16)
        self.picture23.grid(row=5, column=7)
        self.picture24= tk.Label(self, height=3, width=16)
        self.picture24.grid(row=6, column=1)
        self.picture25= tk.Label(self, height=3, width=16)
        self.picture25.grid(row=6, column=6)

        # 各地點和在該地點的玩家
        global place_list
        place_list = ['校門\n\n', '管院\n\n', '小福\n\n', '新體\n\n', '法學院\n\n', '文學院\n\n', '電資學院\n\n',
                    '活大\n\n', '機會/命運\n\n', '社科院\n\n', '理學院\n\n', '醫學院\n\n', '宿舍\n\n',
                    '計中\n\n', '總圖\n\n', '醉月湖\n\n', '傅鐘\n\n', '水源校區\n\n']

        if n >=2:
            self.player_move('player1')
            self.player_move('player2')
        if n >=3:        
            self.player_move('player3')
        if n >=4:        
            self.player_move('player4')


        # 內圈格子
        self.place00 = tk.Label(self, height=4, width=13, bg='sky blue', text=place_list[0], fg='white', font=('Arial', 12))
        self.place00.grid(row=1, column=1)
        self.place01 = tk.Label(self, height=4, width=12, bg='pink2', text=place_list[1], fg='white', font=('Arial', 12))
        self.place01.grid(row=1, column=2)
        self.place02 = tk.Label(self, height=4, width=12, bg='sky blue', text=place_list[2], fg='white', font=('Arial', 12))
        self.place02.grid(row=1, column=3)
        self.place03 = tk.Label(self, height=4, width=12, bg='pink2', text=place_list[3], fg='white', font=('Arial', 12))
        self.place03.grid(row=1, column=4)
        self.place04 = tk.Label(self, height=4, width=12, bg='sky blue', text=place_list[4], fg='white', font=('Arial', 12))
        self.place04.grid(row=1, column=5)
        self.place05 = tk.Label(self, height=4, width=13, bg='pink2', text=place_list[5], fg='white', font=('Arial', 12))
        self.place05.grid(row=1, column=6)
        self.place06 = tk.Label(self, height=4, width=13, bg='sky blue', text=place_list[6], fg='white', font=('Arial', 12))
        self.place06.grid(row=2, column=6)
        self.place07 = tk.Label(self, height=4, width=13, bg='pink2', text=place_list[7], fg='white', font=('Arial', 12))
        self.place07.grid(row=3, column=6)
        self.place08 = tk.Label(self, height=4, width=13, bg='sky blue', text=place_list[8], fg='white', font=('Arial', 12))
        self.place08.grid(row=4, column=6)
        self.place09 = tk.Label(self, height=4, width=13, bg='pink2', text=place_list[9], fg='white', font=('Arial', 12))
        self.place09.grid(row=5, column=6)
        self.place10 = tk.Label(self, height=4, width=12, bg='sky blue', text=place_list[10], fg='white', font=('Arial', 12))
        self.place10.grid(row=5, column=5)
        self.place11 = tk.Label(self, height=4, width=12, bg='pink2', text=place_list[11], fg='white', font=('Arial', 12))
        self.place11.grid(row=5, column=4)
        self.place12 = tk.Label(self, height=4, width=12, bg='sky blue', text=place_list[12], fg='white', font=('Arial', 12))
        self.place12.grid(row=5, column=3)
        self.place13 = tk.Label(self, height=4, width=12, bg='pink2', text=place_list[13], fg='white', font=('Arial', 12))
        self.place13.grid(row=5, column=2)
        self.place14 = tk.Label(self, height=4, width=13, bg='sky blue', text=place_list[14], fg='white', font=('Arial', 12))
        self.place14.grid(row=5, column=1)
        self.place15 = tk.Label(self, height=4, width=13, bg='pink2', text=place_list[15], fg='white', font=('Arial', 12))
        self.place15.grid(row=4, column=1)
        self.place16 = tk.Label(self, height=4, width=13, bg='sky blue', text=place_list[16], fg='white', font=('Arial', 12))
        self.place16.grid(row=3, column=1)
        self.place17 = tk.Label(self, height=4, width=13, bg='pink2', text=place_list[17], fg='white', font=('Arial', 12))
        self.place17.grid(row=2, column=1)
        

        global score_1
        if chooseplayerdict['player1'] == ' ★ ':
            self.score_variable_1 = tk.StringVar(self, f'★ credits: {score_1}')
        elif chooseplayerdict['player1'] == ' ❤ ':
            self.score_variable_1 = tk.StringVar(self, f'❤ credits: {score_1}')
        elif chooseplayerdict['player1'] == ' ✿ ':
            self.score_variable_1 = tk.StringVar(self, f'✿ credits: {score_1}')
        elif chooseplayerdict['player1'] == ' 😀 ':
            self.score_variable_1 = tk.StringVar(self, f'😀 credits: {score_1}')
        self.score_lbl = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_1, font=('Arial', 12))
        self.score_lbl.place(x = 280, y = 190)
        
        """
        #改變玩家2的學分數
        """
        global score_2 
        if chooseplayerdict['player2'] == ' ★ ':
            self.score_variable_2 = tk.StringVar(self, f'★ credits: {score_2}')
        elif chooseplayerdict['player2'] == ' ❤ ':
            self.score_variable_2 = tk.StringVar(self, f'❤ credits: {score_2}')
        elif chooseplayerdict['player2'] == ' ✿ ':
            self.score_variable_2 = tk.StringVar(self, f'✿ credits: {score_2}')
        elif chooseplayerdict['player2'] == ' 😀 ':
            self.score_variable_2 = tk.StringVar(self, f'😀 credits: {score_2}')
        self.score_lb2 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_2, font=('Arial', 12))
        self.score_lb2.place(x = 280, y = 240)


        if n >= 3:
            global score_3
            if chooseplayerdict['player3'] == ' ★ ':
                self.score_variable_3 = tk.StringVar(self, f'★ credits: {score_3}')
            elif chooseplayerdict['player3'] == ' ❤ ':
                self.score_variable_3 = tk.StringVar(self, f'❤ credits: {score_3}')
            elif chooseplayerdict['player3'] == ' ✿ ':
                self.score_variable_3 = tk.StringVar(self, f'✿ credits: {score_3}')
            elif chooseplayerdict['player3'] == ' 😀 ':
                self.score_variable_3 = tk.StringVar(self, f'😀 credits: {score_3}')
            self.score_lb3 = tk.Label(self, height = 2, width = 18, bg = 'skyblue', textvariable = self.score_variable_3, font=('Arial', 12))
            self.score_lb3.place(x = 280, y = 290)
        

            if n == 4:
                global score_4
                if chooseplayerdict['player4'] == ' ★ ':
                    self.score_variable_4 = tk.StringVar(self, f'★ credits: {score_4}')
                elif chooseplayerdict['player4'] == ' ❤ ':
                    self.score_variable_4 = tk.StringVar(self, f'❤ credits: {score_4}')
                elif chooseplayerdict['player4'] == ' ✿ ':
                    self.score_variable_4 = tk.StringVar(self, f'✿ credits: {score_4}')
                elif chooseplayerdict['player4'] == ' 😀 ':
                    self.score_variable_4 = tk.StringVar(self, f'😀 credits: {score_4}')
                self.score_lb4 = tk.Label(self, height = 2, width = 18, bg = 'pink2', textvariable = self.score_variable_4, font=('Arial', 12))
                self.score_lb4.place(x = 280, y = 340)
        if dice_availible == True:
            self.dice_button = tk.Button(self, text = "ROLL", height = 3, width = 7, foreground = "white", bg = "pink2", font=('Arial', 12), command=lambda:[self.roll_dice(), self.create_widgets()])
        else:
            self.dice_button = tk.Button(self, text = "ROLL", height = 3, width = 7, foreground = "white", bg = "pink2", font=('Arial', 12))
        self.dice_button.place(x = 460, y = 200)    
        
        self.update_score_button = tk.Button(self, text = "UPDATE", height = 3, width = 7, foreground = "white", bg = "skyblue", font=('Arial', 12), command = lambda:[self.change_score(), self.activate_dice()])
        self.update_score_button.place(x = 460, y = 280)

        
mywindow = Window()
mywindow.master.title("台大大富翁")

mywindow.mainloop()
