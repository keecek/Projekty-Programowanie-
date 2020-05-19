class Czlowiek(): # klasy mają wskazywać na obiekty
    def __init__(self, argX, argY, argZ):
        self.pozycReki = 1 
        self.x = argX
        self.y = argY
        self.z = argZ
        self.kierunek = 1
        self.ruchReki = argX
        
    def witaj(self, stopnie):
        if self.pozycReki >= 30 or self.pozycReki <= 0:
            self.kierunek *= -1
        self.pozycReki += stopnie * self.kierunek
        self.ruchReki += 1.5 * self.kierunek
        
        
    def rysuj(self): # metody to czynności
        circle(self.x, self.y, self.z)
        line(self.x, self.y+12, self.x, self.y+60)
        line(self.x, self.y+60, self.x+20, self.y+90)
        line(self.x, self.y+60, self.x-20, self.y+90)
        line(self.x, self.y+25, self.x-30, self.y+50) 
        line(self.x, self.y+25, self.ruchReki+30, self.y-10+self.pozycReki)
    
def setup():
    size(300, 300)
    global kewin, jacek
    kewin = Czlowiek(width/2, height/2, 25) # praktyki wskazują, aby zmienne były z małej, a nazwy klas z dużej ;)
    jacek = Czlowiek(width/4, height/4, 35) # miały być dwa obiekty, zwróć uwagę, że dzieki klasie wystaczy dopisać na prawdę niewiele by osiągnąć kolejny obiekt o tak samo skomplikowanej logice
    
def mouseWheel(event):
    kewin.witaj(5)
    jacek.witaj(10)
    
def draw():
    background(120)
    if kewin.pozycReki >= 15:    
        textSize(18)
        text("eluwina", 180, 100) # to spokojnie mogłaby być metoda w klasie, a tekst powitania być agumentem i być indywidualny dla ludków, możnaby też dorysować chmurkę :)
    kewin.rysuj()
    jacek.rysuj()

# miło się sprawdza takie zadania domowe :) plus do aktywnosci za pomysł, lubię ten machający do mnie tłum stickmanów, nawet jeśli wyglądają bardziej jakby chcieli zatrzymać machaniem autobus ;D
# 1,75pkt
