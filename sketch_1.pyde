def setup():
    size(1000,1000)
    rectMode(CORNERS)
    
    
def draw():
    print(height,width, mouseX, mouseY)
    if(mousePressed):
        clear()
        rect(mouseY,mouseX, mouseX, mouseY)
    else:
        line(500,500, mouseX, mouseY)
    
