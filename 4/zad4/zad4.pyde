add_library('pdf')     
def setup():
    global img, img1, img2, img3, pressed 
    size(492, 633) 
    img = loadImage("lenna2.jpg") 
    img1 = loadImage("okular.png")
    img2 = loadImage("unnamed.png")
    #? img3 = loadImage("")
    beginRecord(PDF, "PeDeEfik.pdf") 
    
def draw():
    global img, img1, img2, img3
    image(img, 0,0, width, height)
    if key == CODED:
        if keyCode == LEFT:
            image(img1, 190,190, width/6, height/10) # nie zostało to dopasowane do zgodnego ze specyfikacją zdjęcia dokumentowego
        if keyCode == RIGHT:
            image(img2, 185,150, width/5, height/9) 

def mousePressed():
    endRecord() # umieszczenie tego dopiero na kliknięcie powoduje, że co klatkę dorysuje się kolejna warstwa z obrazem i z każdą klatką przed kliknięciem zapisany pdf wyjściowy będzie coraz cięższy
    exit()

#1,75p
