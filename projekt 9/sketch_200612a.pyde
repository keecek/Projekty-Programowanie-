def setup():
    size(600, 600)
    background(180)
    global obraz
    obraz = loadImage("obrazek.jpg")
    strokeWeight(6)
    textSize(16)
 
def draw():
    rect(width/6, height/6, 400, 400)
    try:
        stroke("#0000FF")
        image(obraz, width/6, height/6, 400, 400)
           
    except:
        stroke("#FF0000")
        text("Blad wczytywania obrazu", 25, 25)
