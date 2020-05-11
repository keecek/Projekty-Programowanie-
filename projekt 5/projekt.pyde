class powitanie():
    def __init__(self, argX, argY, argZ):
        self.pozycReki = 1 
        self.x = argX
        self.y = argY
        self.z = argZ
        self.kierunek = 1
        self.ruchReki = argX
        
    def reka(self, stopnie):
        if self.pozycReki >= 30 or self.pozycReki <= 0:
            self.kierunek *= -1
        self.pozycReki += stopnie * self.kierunek
        self.ruchReki += 1.5 * self.kierunek
        
        
    def czlowiek(self):
        circle(self.x, self.y, self.z)
        line(self.x, self.y+12, self.x, self.y+60)
        line(self.x, self.y+60, self.x+20, self.y+90)
        line(self.x, self.y+60, self.x-20, self.y+90)
        line(self.x, self.y+25, self.x-30, self.y+50) 
        line(self.x, self.y+25, self.ruchReki+30, self.y-10+self.pozycReki)
    
def setup():
    size(300, 300)
    global Powitanie, stopnie, czlowiek
    Powitanie = powitanie(width/2, height/2, 25)
    
    
def mouseWheel(event):
    Powitanie.reka(5)
    
def draw():
    background(120)
    if Powitanie.pozycReki >= 15:    
        textSize(18)
        text("eluwina", 180, 100)
    Powitanie.czlowiek()

    
