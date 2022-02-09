import Spielfeld
from tkinter import *
import playsound
def kappa():
    print("yo")

class Springer():
    istWeiß = None
    x_ = 0
    y_ = 0
    def __init__(self, x, y, istWeiß=True):
        self.istWeiß = istWeiß
        self.x_ = x
        self.y_ = y

    def bewegeNach(self, ziel_x, ziel_y):
        if (abs(ziel_x-self.x_) == 2 and abs(ziel_y-self.y_) == 1) or (abs(ziel_x-self.x_) == 1 and abs(ziel_y - self.y_) == 2):
            return True
        return False


class König():
    istWeiß = None
    x_ = 0
    y_ = 0

    def __init__(self, x, y, istWeiß=True):
        self.istWeiß = istWeiß
        self.x_ = x
        self.y_ = y

    def bewegeNach(self, x, y):
        if abs(x-self.x_) <= 1 and abs(y-self.y_) <= 1:
            if self.x_ == x and self.y_ == y:
                return False
            return True





class Dame():
    istWeiß = None
    x_ = 0
    y_ = 0

    def __init__(self, x, y, istWeiß=True):
        self.istWeiß = istWeiß
        self.x_ = x
        self.y_ = y

    def bewegeNach(self, x, y):
        pass


class Läufer():
    istWeiß = None
    x_ = 0
    y_ = 0

    def __init__(self, x, y, istWeiß=True):
        self.istWeiß = istWeiß
        self.x_ = x
        self.y_ = y

    def bewegeNach(self, x, y):
        pass


class Turm():
    istWeiß = None
    x_ = 0
    y_ = 0

    def __init__(self, x, y, istWeiß=True):
        self.istWeiß = istWeiß
        self.x_ = x
        self.y_ = y

    @staticmethod
    def getFiigur(m_x, m_y):
        for key, value in Spielfeld.Spielfeld.field_labels.items():
            current_key = key
            x = int(current_key[2])
            y = int(current_key[4])
            if x == m_x and y == m_y:
                new = value
                return new["text"]
        return ""

    def FigurFarbeIstWeiß(self, m_x, m_y):
        for key, value in Spielfeld.Spielfeld.field_labels.items():
            current_key = key
            x = int(current_key[2])
            y = int(current_key[4])
            if x == m_x and y == m_y:
                new = value
                if new["text"] in Spielfeld.Spielfeld.white_figuren:
                    return True
                if new["text"] in Spielfeld.Spielfeld.black_figuren:
                    return False

        return None


    def bewegeNach(self, x, y):
        # x
        if x == self.x_:
            if y < self.y_:
                smallest = y
            else:
                smallest = self.y_
            if y > self.y_:
                highest = y
            else:
                highest = self.y_
            for i in range(smallest+1, highest):
                    if not self.getFiigur(x, i) == "":
                        return False
            else:
                return True
            return False
        elif y == self.y_:
            if x < self.x_:
                smallest = x
            else:
                smallest = self.x_
            if x > self.x_:
                highest = x
            else:
                highest = self.x_
            for i in range(smallest+1, highest):
                    if not self.getFiigur(i, y) == "":
                        return False
            else:
                return True
            return False





class Bauer():
    istWeiß = None
    x_ = 0
    y_ = 0
    def __init__(self, x, y, istWeiß=True):
        self.istWeiß = istWeiß
        self.x_ = x
        self.y_ = y

    @staticmethod
    def getFigur(m_x, m_y):
        for key, value in Spielfeld.Spielfeld.field_labels.items():
            current_key = key
            x = int(current_key[2])
            y = int(current_key[4])
            if x == m_x and y == m_y:
                new = value
                return new["text"]
        return ""

    def FigurFarbeIstWeiß(self, m_x, m_y):
        for key, value in Spielfeld.Spielfeld.field_labels.items():
            current_key = key
            x = int(current_key[2])
            y = int(current_key[4])
            if x == m_x and y == m_y:
                new = value
                if new["text"] in Spielfeld.Spielfeld.white_figuren:
                    return True
                if new["text"] in Spielfeld.Spielfeld.black_figuren:
                    return False

        return None

    def bewegeNach(self, ziel_x, ziel_y):
        if self.istWeiß:#weiß
            if self.x_ == 7:
                if (self.x_ - ziel_x <= 2 and self.x_ - ziel_x >=0) and self.y_ == ziel_y:
                    if self.getFigur(self.x_-1, self.y_) != "" or self.getFigur(self.x_-2, self.y_) != "":
                        return False
                    return True
            if self.x_ - ziel_x == 1 and self.y_ == ziel_y and self.FigurFarbeIstWeiß(ziel_x, ziel_y) == None:
                return True
            #figur schlagen
            if abs(self.y_ - ziel_y) == 1 and self.x_ - ziel_x == 1 and self.FigurFarbeIstWeiß(ziel_x, ziel_y) == False:
                return True
            return False


        else:#schwarz
            if self.x_ == 2:
                if (ziel_x - self.x_ <= 2 and ziel_x -self.x_ >=1) and ziel_y == self.y_:
                    if self.getFigur(self.x_ + 1, self.y_) != "" or self.getFigur(self.x_ + 2, self.y_) != "":
                        return False
                    return True
            elif ziel_x - self.x_ == 1 and self.y_ == ziel_y and self.FigurFarbeIstWeiß(ziel_x, ziel_y) == None:
                return True
            if abs(ziel_y - self.y_) == 1 and ziel_x - self.x_ == 1 and self.FigurFarbeIstWeiß(ziel_x, ziel_y):
                return True
            return False
