import tkinter
from tkinter import *
from time import sleep
import Schachfigur


class Spielfeld():
    final = ""
    geo = "850x750"
    black_pawn = "\u265F"
    black_knight = "\u265E"
    black_bishop = "\u265D"
    black_rook = "\u265C"
    black_queen = "\u265B"
    black_king = "\u265A"

    white_pawn = "\u2659"
    white_knight = "\u2658"
    white_bishop = "\u2657"
    white_rook = "\u2656"
    white_queen = "\u2655"
    white_king = "\u2654"

    white_figuren = [white_king,white_queen,white_rook,white_knight,white_bishop,white_pawn]
    black_figuren = [black_king,black_queen,black_rook,black_knight,black_bishop,black_pawn]

    field_labels = {}
    istWeiß = False
    x = 0
    y = 0
    ziel_x = 0
    ziel_y = 0
    current_key = ""

    b1_pressed = False
    figur_pressed = ""
    alte_pos = ""
    neue_pos = ""
    current_value = ""
    felder = []
    alte_farben = []
    weiß_am_zug = True
    background_labels = []
    blocked_t_weiß = False
    def __init__(self):
        self.root = Tk()
        self.root.geometry(self.geo)
        self.root.title("Schach by Fufu")
        self.root.iconbitmap(r"C:\Users\user\Desktop\Artua-Mac-Chess.ico")
        self.root.configure(background="black")
        self.scale_var = IntVar()
        self.scale = Scale(self.root, orient=HORIZONTAL, variable=self.scale_var,activebackground="blue", command=lambda x: self.check_slider(),length=500, to=755,bg="#00ff00",troughcolor="green", showvalue=False)
        self.scale.pack(anchor=CENTER)

        #koordinaten anzeigen
        self.coord_frame = Frame(self.root)
        self.coord_frame.place(x=75, y=650)
        self.alp = "abcdefgh"
        for i in range(8):
            self.label = Label(self.coord_frame, text= self.alp[i], width= 11, font=("Arial", 9),bg="black", fg="white")
            self.label.pack(side=LEFT)
            self.background_labels.append(self.label)

        self.nums = "87654321"
        self.brauche_y = 95
        for e in range(8):
            label = Label(self.root, text=self.nums[e], bg="black", fg="white")
            label.place(x=30, y=self.brauche_y)
            self.background_labels.append(label)
            self.brauche_y += 70


        fontsize = 50

        #place fields

        for u in range(1,9):
            frame = Frame(self.root)
            frame.place(x=80, y=u*69)
            for i in range(1,9):
                if (u+i) % 2 == 0:
                    bg_color = "white"
                else:
                    bg_color = "grey"
                if u == 2:
                    label = Label(frame, text=self.black_pawn,bg=bg_color,relief=RAISED, font=("italic", fontsize),padx = 0,pady=0,width=2)
                    label.pack(side=LEFT)
                    self.field_labels["P:" + str(u) + "_" + str(i)] = label

                elif u == 7:
                    label = Label(frame, text=self.white_pawn,relief=RAISED, bg=bg_color, font=("italic", fontsize),padx = 0,pady=0,width=2)
                    label.pack(side=LEFT)
                    self.field_labels["P:" + str(u) + "_" + str(i)] = label

                elif u == 1:
                    if i == 1 or i == 8:
                        figur = self.black_rook
                    elif i == 2 or i == 7:
                        figur = self.black_knight
                    elif i == 3 or i == 6:
                        figur = self.black_bishop
                    elif i == 4:
                        figur = self.black_queen
                    elif i == 5:
                        figur = self.black_king

                    label = Label(frame, text=figur, bg=bg_color,relief=RAISED, font=("italic", fontsize),padx = 0,pady=0,width=2)
                    label.pack(side=LEFT)
                    self.field_labels["P:" + str(u) + "_" + str(i)] = label


                elif u == 8:
                    if i == 1 or i == 8:
                        figur = self.white_rook
                    elif i == 2 or i == 7:
                        figur = self.white_knight
                    elif i == 3 or i == 6:
                         figur = self.white_bishop
                    elif i == 4:
                        figur = self.white_queen
                    elif i == 5:
                        figur = self.white_king

                    label = Label(frame, text=figur, bg=bg_color ,relief=RAISED,padx = 0,pady=0, font=("italic", fontsize), width=2)
                    label.pack(side=LEFT)
                    self.field_labels["P:" + str(u) + "_" + str(i)] = label



                else:
                    label = Label(frame,text="", bg=bg_color, padx=0,pady=0, relief=RAISED,font=("italic", fontsize),width=2)
                    label.pack(side=LEFT)
                    self.field_labels["P:" + str(u) + "_" + str(i)] = label

        # change fields

        self.root.bind("<1>", lambda x: self.pressedButton(x, self.weiß_am_zug))
        self.root.bind("<Motion>", lambda x: self.motion(x))

        self.root.mainloop()

    def change_label_background(self):
        for label in self.background_labels:
            label["bg"] =self.final
            fg_color = "#"

            ik = "0x" + self.final[1:3]
            ik = int(ik, base=16) + 125
            ik = hex(ik)
            fg_color += str(ik)

            ik2 = "0x" + self.final[3:5]
            ik2 = int(ik2, base=16) + 125
            ik2 = hex(ik2)
            fg_color += str(ik2)

            ik3 = "0x" + self.final[5:7]
            ik3 = int(ik3, base=16) + 125
            ik3 = hex(ik3)
            fg_color += str(ik3)

            fg_color = fg_color.replace("0x", "")
            fg_color = fg_color[:7]
            label["fg"] = fg_color









    def getFigur(self,m_x, m_y):
        for key, value in self.field_labels.items():
            current_key = key
            x = int(current_key[2])
            y = int(current_key[4])
            if x == m_x and y == m_y:
                new = value
                return new["text"]
        return ""


        """for key, value in self.field_labels.items():
            new = value
            break
        print(new["text"])"""

    def FigurFarbeIstWeiß(self, m_x, m_y):
        for key, value in self.field_labels.items():
            current_key = key
            x = int(current_key[2])
            y = int(current_key[4])
            if x == m_x and y == m_y:
                new = value
                if new["text"] in self.white_figuren:
                    return True
                if new["text"] in self.black_figuren:
                    return False

        return None



    def getFeld(self, m_x, m_y):
        for key, value in self.field_labels.items():
            current_key = key
            x = int(current_key[2])
            y = int(current_key[4])
            if x == m_x and y == m_y:
                new = value
                return new

    def check_slider(self):

        _hex = hex(int(self.scale_var.get()))
        current = int(_hex, base=16)
        if current <= 255:
            self.final += str(hex(current)[2:])
        elif current <= 510:
            self.final += "ff"
            self.final += str(hex(current-255)[2:])
        else:
            self.final += "ffff"
            self.final += str(hex(current-510)[2:])
        self.final.replace("x", "")
        self.final = "#" + self.final
        if len(self.final) <= 7:
            self.final += (7-len(self.final))*"0"
        #stelle farbenwert ein
        self.root.configure(background=self.final)
        self.change_label_background()
        self.final = ""



    def motion(self, event):
        """try:
            if event.widget["text"] != "":
                 print(event.widget["text"])


        except:
            pass"""
        pass

    def change_back_color(self, felder, alte_farben):
        count = len(alte_farben)
        for i in range(count):
            felder[i]["bg"] = alte_farben[i]


    def pressedButton(self, event, weißZug):
        try:
            #figur das erste mal geklickt
                if self.figur_pressed == "":
                    self.alte_pos = event.widget
                    for key, value in self.field_labels.items():
                        if value == self.alte_pos:
                            current_key = key
                            self.x = int(current_key[2])
                            self.y = int(current_key[4])

                    if self.weiß_am_zug == self.FigurFarbeIstWeiß(self.x, self.y):
                        pass
                    else:
                        return None


                    self.b1_pressed = True
                    self.figur_pressed = event.widget["text"]



                    """if (self.color_pressed == "white" and weißZug) or (self.color_pressed == "grey" and not weißZug):
                        pass
                    else:
                        print("falsche farbe")"""





                        #self.getFigur(8, 7)
                    color = "#ffd700"
                    for i in range(1, 9):
                            self.blocked_t_weiß = False
                            for u in range(1,9):
                                    for e, fig in enumerate(self.white_figuren):  # king queen rook knight bishop pawn
                                        if fig == self.alte_pos["text"]:
                                            if e == 5:
                                                bauer_weiß = Schachfigur.Bauer(self.x, self.y, True)
                                                if bauer_weiß.bewegeNach(i, u) and not self.FigurFarbeIstWeiß(i, u):
                                                    feld = self.getFeld(i, u)
                                                    alte_farbe = feld["bg"]
                                                    self.alte_farben.append(alte_farbe)
                                                    feld["bg"] = color
                                                    self.felder.append(feld)

                                            if e == 0:
                                                könig_weiß = Schachfigur.König(self.x, self.y, True)
                                                if könig_weiß.bewegeNach(i, u) and not self.FigurFarbeIstWeiß(i, u):
                                                    feld = self.getFeld(i, u)
                                                    alte_farbe = feld["bg"]
                                                    self.alte_farben.append(alte_farbe)
                                                    feld["bg"] = color
                                                    self.felder.append(feld)

                                            elif e == 1:
                                                dame_weiß = Schachfigur.Dame(self.x, self.y, True)
                                                if dame_weiß.bewegeNach(i, u) and not self.FigurFarbeIstWeiß(i, u):

                                                        feld = self.getFeld(i, u)
                                                        alte_farbe = feld["bg"]
                                                        self.alte_farben.append(alte_farbe)
                                                        feld["bg"] = color
                                                        self.felder.append(feld)

                                            elif e == 2:
                                                turm_weiß = Schachfigur.Turm(self.x, self.y, True)
                                                if turm_weiß.bewegeNach(i, u) and self.FigurFarbeIstWeiß(i, u) == None:

                                                        #eigene pos: self.x, self.y ... ziel pos: i, u
                                                        feld = self.getFeld(i, u)
                                                        alte_farbe = feld["bg"]
                                                        self.alte_farben.append(alte_farbe)
                                                        feld["bg"] = color
                                                        self.felder.append(feld)






                                            elif e == 3:
                                                springer_weiß = Schachfigur.Springer(self.x, self.y, True)
                                                if springer_weiß.bewegeNach(i, u) and not self.FigurFarbeIstWeiß(i, u):
                                                    feld = self.getFeld(i, u)
                                                    alte_farbe = feld["bg"]
                                                    self.alte_farben.append(alte_farbe)
                                                    feld["bg"] = color
                                                    self.felder.append(feld)
                                            elif e == 4:
                                                läufer_weiß = Schachfigur.Läufer(self.x, self.y, True)
                                                if läufer_weiß.bewegeNach(i, u) and not self.FigurFarbeIstWeiß(i, u):
                                                    feld = self.getFeld(i, u)
                                                    alte_farbe = feld["bg"]
                                                    self.alte_farben.append(alte_farbe)
                                                    feld["bg"] = color
                                                    self.felder.append(feld)





                                    for e, fig in enumerate(self.black_figuren): # king queen rook knight bishop pawn
                                         if fig == self.alte_pos["text"]:
                                                if e == 5:
                                                    bauer_weiß = Schachfigur.Bauer(self.x, self.y, False)
                                                    if bauer_weiß.bewegeNach(i, u) and ((self.FigurFarbeIstWeiß(i, u)) or (self.FigurFarbeIstWeiß(i, u) == None)):
                                                        feld = self.getFeld(i, u)
                                                        alte_farbe = feld["bg"]
                                                        self.alte_farben.append(alte_farbe)
                                                        feld["bg"] = color
                                                        self.felder.append(feld)

                                                if e == 0:
                                                    könig_weiß = Schachfigur.König(self.x, self.y, False)
                                                    if könig_weiß.bewegeNach(i, u) and ((self.FigurFarbeIstWeiß(i, u)) or (self.FigurFarbeIstWeiß(i, u) == None)):
                                                        feld = self.getFeld(i, u)
                                                        alte_farbe = feld["bg"]
                                                        self.alte_farben.append(alte_farbe)
                                                        feld["bg"] = color
                                                        self.felder.append(feld)

                                                elif e == 1:
                                                    dame_weiß = Schachfigur.Dame(self.x, self.y, False)
                                                    if dame_weiß.bewegeNach(i, u) and ((self.FigurFarbeIstWeiß(i, u)) or (self.FigurFarbeIstWeiß(i, u) == None)):
                                                        feld = self.getFeld(i, u)
                                                        alte_farbe = feld["bg"]
                                                        self.alte_farben.append(alte_farbe)
                                                        feld["bg"] = color
                                                        self.felder.append(feld)
                                                elif e == 2:
                                                    turm_weiß = Schachfigur.Turm(self.x, self.y, False)
                                                    if turm_weiß.bewegeNach(i, u) and ((self.FigurFarbeIstWeiß(i, u)) or (self.FigurFarbeIstWeiß(i, u) == None)):
                                                        feld = self.getFeld(i, u)
                                                        alte_farbe = feld["bg"]
                                                        self.alte_farben.append(alte_farbe)
                                                        feld["bg"] = color
                                                        self.felder.append(feld)
                                                elif e == 3:
                                                    springer_weiß = Schachfigur.Springer(self.x, self.y, False)
                                                    if springer_weiß.bewegeNach(i, u) and ((self.FigurFarbeIstWeiß(i, u)) or (self.FigurFarbeIstWeiß(i, u) == None)):
                                                        feld = self.getFeld(i, u)
                                                        alte_farbe = feld["bg"]
                                                        self.alte_farben.append(alte_farbe)
                                                        feld["bg"] = color
                                                        self.felder.append(feld)
                                                elif e == 4:
                                                    läufer_weiß = Schachfigur.Läufer(self.x, self.y, False)
                                                    if läufer_weiß.bewegeNach(i, u) and ((self.FigurFarbeIstWeiß(i, u)) or (self.FigurFarbeIstWeiß(i, u) == None)):
                                                        feld = self.getFeld(i, u)
                                                        alte_farbe = feld["bg"]
                                                        self.alte_farben.append(alte_farbe)
                                                        feld["bg"] = color
                                                        self.felder.append(feld)



                #zweites mal
                else:
                    self.root.after(0, self.change_back_color(self.felder, self.alte_farben))
                    self.alte_farben = []
                    self.felder = []
                    self.b1_pressed = False
                    self.neue_pos = event.widget
                    for key, value in self.field_labels.items():
                        if value == self.alte_pos:
                            current_key = key
                            self.x = int(current_key[2])
                            self.y = int(current_key[4])

                    for key, value in self.field_labels.items():
                        if value == self.neue_pos:
                            current_key = key
                            self.ziel_x = int(current_key[2])
                            self.ziel_y = int(current_key[4])

                    #print(str(self.x), str(self.y) + " nach: " + str(self.ziel_x), str(self.ziel_y))


                    if self.alte_pos["text"] in self.white_figuren:#weiß

                            for e, fig in enumerate(self.white_figuren):  # king queen rook knight bishop pawn
                                if fig == self.alte_pos["text"]:
                                    if e == 0:
                                        könig_weiß = Schachfigur.König(self.x, self.y, True)
                                        if könig_weiß.bewegeNach(self.ziel_x, self.ziel_y) and not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            event.widget["text"] = self.figur_pressed
                                            self.alte_pos["text"] = ""
                                            self.figur_pressed = ""
                                        elif könig_weiß.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                            self.figur_pressed = ""
                                            return None
                                        elif self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            self.figur_pressed = ""
                                            return None
                                        else:
                                            self.figur_pressed = ""

                                    elif e == 1:
                                        dame_weiß = Schachfigur.Dame(self.x, self.y, True)
                                        if dame_weiß.bewegeNach(self.ziel_x, self.ziel_y) and not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            event.widget["text"] = self.figur_pressed
                                            self.alte_pos["text"] = ""
                                            self.figur_pressed = ""
                                        elif dame_weiß.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                            self.figur_pressed = ""
                                            return None
                                        elif self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            self.figur_pressed = ""
                                            return None
                                        else:
                                            self.figur_pressed = ""
                                    elif e == 2:
                                        turm_weiß = Schachfigur.Turm(self.x, self.y, True)
                                        if turm_weiß.bewegeNach(self.ziel_x, self.ziel_y) and not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            event.widget["text"] = self.figur_pressed
                                            self.alte_pos["text"] = ""
                                            self.figur_pressed = ""
                                        elif turm_weiß.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                            self.figur_pressed = ""
                                            return None
                                        elif self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            self.figur_pressed = ""
                                            return None
                                        else:
                                            self.figur_pressed = ""
                                    elif e == 3:
                                        springer_weiß = Schachfigur.Springer(self.x, self.y, True)
                                        if springer_weiß.bewegeNach(self.ziel_x, self.ziel_y) and not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            event.widget["text"] = self.figur_pressed
                                            self.alte_pos["text"] = ""
                                            self.figur_pressed = ""
                                        elif springer_weiß.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                            self.figur_pressed = ""
                                            return None
                                        elif self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            self.figur_pressed = ""
                                            return None
                                        else:
                                            print("hi23")
                                            self.figur_pressed = ""
                                    elif e == 4:
                                        läufer_weiß = Schachfigur.Läufer(self.x, self.y, True)
                                        if läufer_weiß.bewegeNach(self.ziel_x, self.ziel_y) and not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            event.widget["text"] = self.figur_pressed
                                            self.alte_pos["text"] = ""
                                            self.figur_pressed = ""
                                        elif läufer_weiß.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                            self.figur_pressed = ""
                                            return None
                                        elif self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            self.figur_pressed = ""
                                            return None
                                        else:
                                            self.figur_pressed = ""
                                    elif e == 5:
                                        bauer_weiß = Schachfigur.Bauer(self.x, self.y, True)
                                        if bauer_weiß.bewegeNach(self.ziel_x, self.ziel_y) and not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            event.widget["text"] = self.figur_pressed
                                            self.alte_pos["text"] = ""
                                            self.figur_pressed = ""
                                        elif bauer_weiß.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                            self.figur_pressed = ""
                                            return None
                                        elif self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                            self.figur_pressed = ""
                                            return None
                                        else:
                                            self.figur_pressed = ""
                    else:


                                for e, fig in enumerate(self.black_figuren):  # king queen rook knight bishop pawn
                                    if fig == self.alte_pos["text"]:
                                        if e == 0:
                                            könig_schwarz = Schachfigur.König(self.x, self.y, False)
                                            if könig_schwarz.bewegeNach(self.ziel_x, self.ziel_y) and ((self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y) == None) or (self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y))):
                                                event.widget["text"] = self.figur_pressed
                                                self.alte_pos["text"] = ""
                                                self.figur_pressed = ""
                                            elif könig_schwarz.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                                self.figur_pressed = ""
                                                return None
                                            elif not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                                self.figur_pressed = ""
                                                return None
                                            else:
                                                self.figur_pressed = ""

                                        elif e == 1:
                                            dame_schwarz = Schachfigur.Dame(self.x, self.y,False)
                                            if dame_schwarz.bewegeNach(self.ziel_x, self.ziel_y) and ((self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y) == None) or (self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y))):
                                                event.widget["text"] = self.figur_pressed
                                                self.alte_pos["text"] = ""
                                                self.figur_pressed = ""
                                            elif dame_schwarz.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                                self.figur_pressed = ""
                                                return None
                                            elif not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                                self.figur_pressed = ""
                                                return None
                                            else:
                                                self.figur_pressed = ""
                                        elif e == 2:
                                            turm_schwarz = Schachfigur.Turm(self.x, self.y, False)
                                            if turm_schwarz.bewegeNach(self.ziel_x, self.ziel_y) and ((self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y) == None) or (self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y))):
                                                event.widget["text"] = self.figur_pressed
                                                self.alte_pos["text"] = ""
                                                self.figur_pressed = ""
                                            elif turm_schwarz.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                                self.figur_pressed = ""
                                                return None
                                            elif not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                                self.figur_pressed = ""
                                                return None
                                            else:
                                                self.figur_pressed = ""
                                        elif e == 3:
                                            springer_schwarz = Schachfigur.Springer(self.x, self.y, False)
                                            if springer_schwarz.bewegeNach(self.ziel_x, self.ziel_y) and ((self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y) == None) or (self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y))):
                                                print(self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y))
                                                event.widget["text"] = self.figur_pressed
                                                self.alte_pos["text"] = ""
                                                self.figur_pressed = ""
                                            elif springer_schwarz.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                                self.figur_pressed = ""
                                                return None
                                            elif not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                                self.figur_pressed = ""
                                                return None
                                            else:
                                                self.figur_pressed = ""
                                        elif e == 4:
                                            läufer_schwarz = Schachfigur.Läufer(self.x, self.y, False)
                                            if läufer_schwarz.bewegeNach(self.ziel_x, self.ziel_y) and ((self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y) == None) or (self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y))):
                                                event.widget["text"] = self.figur_pressed
                                                self.alte_pos["text"] = ""
                                                self.figur_pressed = ""
                                            elif läufer_schwarz.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                                self.figur_pressed = ""
                                                return None
                                            elif not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                                self.figur_pressed = ""
                                                return None
                                            else:
                                                self.figur_pressed = ""
                                        elif e == 5:
                                            bauer_schwarz = Schachfigur.Bauer(self.x, self.y, False)
                                            if bauer_schwarz.bewegeNach(self.ziel_x, self.ziel_y) and ((self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y) == None) or (self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y))):
                                                event.widget["text"] = self.figur_pressed
                                                self.alte_pos["text"] = ""
                                                self.figur_pressed = ""
                                            elif bauer_schwarz.bewegeNach(self.ziel_x, self.ziel_y) == False:
                                                self.figur_pressed = ""
                                                return None
                                            elif not self.FigurFarbeIstWeiß(self.ziel_x, self.ziel_y):
                                                self.figur_pressed = ""
                                                return None
                                            else:
                                                self.figur_pressed = ""

                    if self.weiß_am_zug:
                        self.weiß_am_zug = False
                    else:
                        self.weiß_am_zug = True

        except:
            pass


















