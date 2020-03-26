def setup():
    size(600,600)
    global x, y, i
    x = 0; y = 300; i=0
    kolor = {"red":(255,0,0), "green":(0,255,0), "blue":(0,0,255)}
    global kolor
    fill(*kolor["red"])
    
def f0():
    global x, y, i, kolor
    x+=1
    y+=1
    if y == 540:
        i = 1
        fill(*kolor["green"])
def f1():
    global x, y, i
    x += 1
    y -= 1
    if x == 540:
        i = 2
        fill(*kolor["blue"])

def f2():
    global x, y, i
    x -= 1
    y -= 1
    if y == 0:
        i=3
        fill(*kolor["red"])

def f3():
    global x, y, i
    x -= 1
    y += 1
    if x==0:
        i=0
        fill(*kolor["red"])

def draw():
    global x, y, i
    rect(x, y, width/10, height/10) # warto używać zależnych zamiast sztywnych wartości
    listf = [f0,f1,f2,f3]
    listf[i]()
    
# zapomniałeś o opcji dodania zamknięcia programu
# 1,75pkt


    
