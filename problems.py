import tkinter as tttk
import random


class Problems:
    def __init__(self):  # 題庫
        p0 = [["台大校門屬於哪個等級的古蹟？\n\nA.國定古蹟  B.直轄市定古蹟  C.縣（市）定古蹟  D.不是古蹟", "B"],
              ["校門中間的「國立臺灣大學」字樣是由誰題字的？\n\nA.朱家驊  B.梅貽琦  C.曾志朗  D.杜正勝", "A"],
              ["椰林大道有幾棵椰子樹？\n\nA.200  B.201  C.202  D.203", "B"],
              ["傅園內的斯年堂為何種建築風格？\n\nA.巴洛克  B.哥德式  C.日式  D.古希臘", "D"]]
        p1 = [["管理學院的院長是？\n\nA.管中閔  B.胡星陽  C.陳家麟  D.劉順仁", "B"],
              ["管院的系辦都在？\n\nA.管一  B.管二  C.管圖  D.教研館", "A"],
              ["哪個不是台大管院的系？\n\nA.工管  B.經濟  C.國企  D.資管", "B"],
              ["以下哪個球隊是隸屬於管院而非單獨系所？\n\nA.桌球  B.羽球  C.壘球  D.網球", "D"]]
        p2 = [["下列地點何者沒有出現在Coco臺大店的菜單中？\n\nA.椰林大道  B.總圖  C.醉月湖  D.陳三鼎", "B"],
              ["小福沒有下列哪個店家? \n\nA.摩斯  B.金興發  C.文湯武醬  D.八方雲集", "D"],
              ["下列哪一種食物包含在小福最受歡迎的餐點「摩斯特餐」裡？\n\nA.薯條  B.雞塊  C.蘑菇湯  D.薯餅", "D"]]
        p3 = [["新體裡面沒有哪項設備？\n\nA.游泳池  B.健身房  C.壁球室  D.攀岩場", "D"],
              ["學生使用健身房的年費為多少錢？\n\nA.$1100  B.$1200  C.$1350  D.$1500", "C"],
              ["新體的健身房在哪一層樓？\n\nA.B1  B.1F  C.2F  D.3F", "A"]]
        p4 = [["法圖位在哪一個館？\n\nA.霖澤館  B.辛亥館  C.裏新館  D.萬才館", "D"],
              ["何者為法律系雙轉輔考試的考試科目？\n\nA.刑總  B.民總  C.著作權法  D.行政法", "B"],
              ["法學院設有幾個研究中心?\n\nA.9  B.11  C.14  D.17", "C"],
              ["下列何者並非台大法律系畢業？\n\nA.吳淡如  B.吳敦義  C.葉俊榮  D.黃國昌", "B"]]
        p5 = [["目前文學院大學部共有幾個系？\n\nA.6  B.7  C.8  D.9", "C"],
              ["下列哪一個文學院的學系是最晚成立的？\n\nA.戲劇系  B.圖資系  C.人類系  D.日文系", "A"],
              ["下列哪一個名人不是台大文學院畢業的？\n\nA.李敖  B.白先勇  C.余光中  D.李家同", "D"],
              ["下列哪個文學院的科系有自己的獨立系館？\n\nA.歷史系  B.圖資系  C.日文系  D.外文系", "B"]]
        p6 = [["何者為資工系館？\n\nA.博理館  B.德田館  C.資訊館  D.工程館", "B"],
              ["電機系學習的是何種程式語言？\n\nA.Python  B.C++  C.C  D.Java", "A"],
              ["哪個活動不是電資學院一起舉辦的？\n\nA.嘉年華  B.野台  C.宿營  D.體育競賽", "C"]]
        p7 = [["活大禮堂的別稱為？\n\nA.僑光堂  B.怡仁堂  C.冠德堂  D.仁德堂", "B"],
              ["活大麥當勞幾點開始營業？\n\nA.6:00  B.7:00  C.8:00  D.9:00", "B"],
              ["活大的建築設計師是？\n\nA.李顯榮  B.王大閎  C.黃聲遠  D.陳仁和", "B"],
              ["活大內的便利商店是哪一家？\n\nA.全家  B.7-11  C.OK  D.萊爾富", "D"],
              ["下列哪個社團的社辦在活大？\n\nA.魔術社  B.薇友會  C.烏克麗麗社  D.咖啡社", "C"]]
        p8 = ["獲得椰林小舖發放的優惠券一張，多2學分",
              "得到管爺青睞，多2學分",
              "想耍帥放雙手騎車，結果烙賽扑街，暫停一回合",
              "腳踏車被水源阿伯拖走了，暫停一回合",
              "修到一門很硬的課，決定停修，少2學分"]
        p9 = [["社科圖的別稱是_____先生紀念圖書館？\n\nA.辜振甫  B.辜顯榮  C.辜寬敏  D.辜仲諒", "A"],
              ["社科圖平日幾點閉館？\n\nA.21:00  B.21:30  C.22:00  D.22:30", "C"],
              ["社科圖落成時由董陽孜女士哪段文字作為勗勉？\n\nA.持之以恆  B.學而第一  C.百年樹人  D.奮發向上", "B"],
              ["下列著名建築師何者為社科院的設計者？\n\nA.安藤忠雄  B.貝聿銘  C.伊東豊雄  D.王大閎", "C"]]
        p10 = [["台大理學院剛創立的時候沒有哪個系?\n\nA.化學  B.生物  C.農學  D.物理", "D"],
              ["台大理學院院辦在哪裡?\n\nA.思亮館  B.天文數學館  C.積學館  D.浩瀚樓", "A"],
              ["中華民國哪位諾貝爾獎得主是台大理學院校友?\n\nA.丁肇中  B.李遠哲  C.李政道  D.楊振寧", "B"],
              ["請問天文數學館中哪個樓層為中研院所管？\n\nA.1  B.3  C.5  D.7", "D"]]
        p11 = [["下列科系何者隸屬於醫學院？\n\nA.物理治療學系  B.生命科學系  C.公共衛生學系  D.心理學系", "A"],
              ["醫學院的大門位於哪一條路上？\n\nA.徐州路  B.仁愛路  C.林森南路  D.中山南路", "B"],
              ["2020台大學生會會長選舉的哪位候選人是醫學院的?\n\nA.陳怡安  B.梁聖宇  C.楊子昂  D.以上皆非", "C"]]
        p12 = [["哪個男宿不在總區？\n\nA.男一  B.男二  C.男七  D.男八", "B"],
              ["哪個男宿有影印店?\n\nA.男三  B.男五  C.男四  D.男一", "D"],
              ["總共有幾棟女生宿舍位於總區？\n\nA.6  B.7  C.8  D.9", "B"]]
        p13 = [["計中影印室有安裝下列哪個軟體？\n\nA.Adobe photoshop cc  B. Python 3.8  C.Scratch2.0  D.WinRAR", "A"],
              ["計中每學期每人之免費列印配額為多少單位？\n\nA.50  B.100  C.150  D.200", "B"],
              ["計中黑白雙面列印9面要多少錢？\n\nA.12  B.12.5 C.13  D.13.5", "D"]]
        p14 = [["下列哪一個不是圖書館？\n\nA.數圖  B.醫圖  C.管圖  D.社科圖", "C"],
              ["地下室自習室的哪一區開放使用電腦、滑鼠等發出聲響的裝置？\n\nA.A區  B.B區  C.AB兩區都可以  D.AB兩區都不行", "A"],
              ["台大大學部學生一次最多能借幾件圖書資料？\n\nA.20  B.40  C.60  D.80", "D"],
              ["請問總圖幾樓可以看電影？\n\nA.1  B.2  C.3  D.4", "D"]]
        p15 = [["下列哪一個是醉月湖的舊稱？\n\nA.大貝湖  B.梅花湖  C.小華湖  D.牛湳池", "D"],
              ["醉月湖先前是哪個水圳的調節池？\n\nA.曹公圳  B.瑠公圳  C.大坪林圳  D.八堡圳", "B"],
              ["醉月湖中央的亭子名稱為？\n\nA.湖心亭  B.觀音亭  C.獅子亭  D.益壽亭", "A"]]
        p16 = [["傅鐘一次敲響幾下？\n\nA.13  B.21  C.24  D.27", "B"],
              ["傅鐘是為了紀念下列哪個人物？\n\nA.傅斯年  B.傅崐萁  C.傅達仁  D.傅立葉", "A"],
              ["傅鐘在椰林大道上，在傅鐘對面的是哪一個學院？\n\nA.農學院  B.理學院  C.工學院  D.文學院", "D"],
              ["傅鐘有哪一項傳聞？\n\nA.21傳聞  B.31傳聞  C.脫魯傳聞  D.鬧鬼傳聞", "A"]]
        p17 = [["以下哪個系所不是位於水源校區？\n\nA.哲學系  B.人類學系  C.植物病理與微生物學系  D.以上皆是", "C"],
              ["只要你的腳踏車被水源阿伯拖超過__次後會開始罰錢？\n\nA.2  B.3  C.5  D.6", "B"],
              ["在水源對面的「台北水道水源地」的古蹟分級為？\n\nA.國家級古蹟  B.直轄市定古蹟  C.縣市級古蹟  D.不是古蹟", "B"],
              ["水源二手腳踏車沒有下列哪個價位？\n\nA.600  B.800  C.1000  D.1200", "C"]]
        self.problem_list = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17]

    def call_a_problem(self, location):  # 隨機叫出該位置的一個問題或機會命運
        number = random.randint(0, len(self.problem_list[location]) - 1)
        if location != 8:
            problem = self.problem_list[location][number][0]
            correct_ans = self.problem_list[location][number][1]
            master(1, problem, correct_ans)
        else:
            chance_destiny = self.problem_list[location][number]
            master(0, chance_destiny)
            if number == 0 or 1:
                score = 2
            elif number == 2 or 3:
                score = -1
                # 加進暫停list
            else:
                score = -2
            return score


class ProblemWindow(tttk.Frame):  # 彈出問題的視窗
    def __init__(self, text, ans, root):
        tttk.Frame.__init__(self)
        self.text = text
        self.ans = ans
        self.grid()
        self.createWidgets()
        self.root = root

    def createWidgets(self):
        self.buttonA = tttk.Button(self, height = 4, width = 6, bg = "sky blue2", fg='white', font = "20", text = "A", command = self.click_buttonA)
        self.buttonB = tttk.Button(self, height = 4, width = 6, bg = "sky blue3", fg='white', font = "20", text = "B", command = self.click_buttonB)
        self.buttonC = tttk.Button(self, height = 4, width = 6, bg = "sky blue2", fg='white', font = "20", text = "C", command = self.click_buttonC)
        self.buttonD = tttk.Button(self, height = 4, width = 6, bg = "sky blue3", fg='white', font = "20", text = "D", command = self.click_buttonD)
        self.lbProblem = tttk.Label(self, height = 15, width = 55, bg='sky blue', fg='white', font = "20", text = self.text)
        self.buttonA.grid(row = 1, column = 0, sticky = tttk.NE + tttk.SW)
        self.buttonB.grid(row = 1, column = 1, sticky = tttk.NE + tttk.SW)
        self.buttonC.grid(row = 1, column = 2, sticky = tttk.NE + tttk.SW)
        self.buttonD.grid(row = 1, column = 3, sticky = tttk.NE + tttk.SW)
        self.lbProblem.grid(row = 0, column = 0, columnspan = 4, sticky = tttk.NE + tttk.SW)

    def click_buttonA(self):
        self.destroy()
        if self.ans == "A":
            self.root.switch_frame(ShowResult, "Correct!\n\n+2學分")
            score = 2
        else:
            self.root.switch_frame(ShowResult, "Wrong!")
            score = 0

    def click_buttonB(self):
        self.destroy()
        if self.ans == "B":
            self.root.switch_frame(ShowResult, "Correct!\n\n+2學分")
            score = 2
        else:
            self.root.switch_frame(ShowResult, "Wrong!")
            score = 0

    def click_buttonC(self):
        self.destroy()
        if self.ans == "C":
            self.root.switch_frame(ShowResult, "Correct!\n\n+2學分", )
            score = 2
        else:
            self.root.switch_frame(ShowResult, "Wrong!")
            score = 0

    def click_buttonD(self):
        self.destroy()
        if self.ans == "D":
            self.root.switch_frame(ShowResult, "Correct!\n\n+2學分")
            score = 2
        else:
            self.root.switch_frame(ShowResult, "Wrong!")
            score = 0


class ShowResult(tttk.Frame):  # 切換作答結果頁面
    def __init__(self, result, root):
        tttk.Frame.__init__(self)
        self.text = result
        self.grid()
        self.createWidgets()
        self.root = root

    def createWidgets(self):
        self.lbResult = tttk.Label(self, height = 15, width = 55, bg='sky blue', fg='white', font = "40", text = self.text)
        self.buttonSure = tttk.Button(self, height = 2, width = 5, bg = "sky blue3", fg='white', font = "20", text = "確認", command = self.click_buttonSure)
        self.buttonSure.grid(row = 1, column = 0, sticky = tttk.NE + tttk.SW)
        self.lbResult.grid(row = 0, column = 0, sticky = tttk.NE + tttk.SW)

    def click_buttonSure(self):
        self.root.destroy()


class ChanceDestinyWindow(tttk.Frame):  # 彈出機會命運的視窗
    def __init__(self, text, root):
        tttk.Frame.__init__(self)
        self.text = text
        self.grid()
        self.createWidgets()
        self.root = root

    def createWidgets(self):
        self.lbChance = tttk.Label(self, height = 15, width = 55, bg='pink2', fg='white', font = "20", text = self.text)
        self.buttonSure = tttk.Button(self, height = 2, width = 5,  bg='pink3', fg='white', font = "20", text = "確認", command = self.click_buttonSure)
        self.buttonSure.grid(row = 1, column = 0, sticky = tttk.NE + tttk.SW)
        self.lbChance.grid(row = 0, column = 0, sticky = tttk.NE + tttk.SW)

    def click_buttonSure(self):
        self.root.destroy()


class master(tttk.Tk):
    def __init__(self, frame_class, text1 = None, text2 = None):
        tttk.Tk.__init__(self)
        if frame_class == 1:
            self._frame = ProblemWindow(text1, text2, self)
            self.title("Problem Window")
        else:
            self.frame = ChanceDestinyWindow(text1, self)
            self.title("Chance and Destiny Window")
        self.mainloop()
    def switch_frame(self, frame_class, result):
        new_frame = frame_class(result, self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


problems = Problems()
for i in range(17):
    score = problems.call_a_problem(i)
    print(score)