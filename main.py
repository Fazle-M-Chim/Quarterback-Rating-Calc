class Quarterback:
    def __init__(self):
        self.com = float(input("Enter the number of passes completed : "))
        self.att = float(input("Enter the number of passes attempted : "))
        self.yd = float(input("Enter the number of gross yards passing : "))
        self.td = float(input("Enter the number of touchdowns thrown : "))
        self.int = float(input("Enter the number of interceptions thrown : "))
        self.QR = 0

    def calcQR(self):
        self.QR = 100 * (((self.com/self.att * 100 - 30)/20) + ((self.yd/self.att - 3)/4)
                         + ((self.td/self.att * 100)/5) + ((1/4) * (9.5 - (self.int/self.att) * 100))) / 6
        return self.QR

    def printQR(self):
        print("The Quarterback Rating is", self.calcQR())

    def setData(self, c, a, y, t, i):
        self.com = c
        self.att = a
        self.yd = y
        self.td = t
        self.int = i


# main
myobj = Quarterback()
myobj.printQR()
