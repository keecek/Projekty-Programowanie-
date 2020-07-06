def setup():
    size(600, 600)
    background(180)
    global obraz
    obraz = loadImage("obrazek.jpg")
    strokeWeight(6)
    textSize(16)
    noFill()
 
def draw():
    try:
        image(obraz, width/6, height/6, 400, 400) # tylko tą linię testujesz pod kątem błędu, wszystko inne powinno być w else    
    except:
        stroke("#FF0000")
        text("Blad wczytywania obrazu", 25, 25)
    else:
        stroke("#0000FF")
    finally:
        rect(width/6, height/6, 400, 400)

# 1,5pkt
