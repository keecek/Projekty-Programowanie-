def setup():
    global firstLetterPos, secondLetterPos, sizeofText
    global initials, colors, isKeyPressed
    size(600,600)
   
    firstLetterPos = [width/2, height/2]; secondLetterPos = [width/2 + width/10, height/2]
    sizeofText = 60
    initials = ["K", "W", LEFT, RIGHT]
    isKeyPressed = {initials[0] : 0, initials[1] : 0, LEFT : 0, RIGHT : 0}
    colors = ["#AAAAAA", "#FFDDBB"]
    textAlign(LEFT, TOP)
    textSize(sizeofText)
    line(350,160,240,500);
    line(240,500,500,300);
    line(500,300,180,300);
    line(180,300,500,500);
    line(500,500,350,160);
   
def draw():
    firstColor = isKeyPressed[initials[0]] + hover(firstLetterPos[0], firstLetterPos[1])
    secondColor = isKeyPressed[initials[1]] + hover(secondLetterPos[0], secondLetterPos[1])
    if isKeyPressed[initials[2]] == 1 or isKeyPressed[initials[3]] == 1:
        firstColor, secondColor = secondColor, firstColor
   
    fill(colors[1 if firstColor > 0 else 0])
    text(initials[0], firstLetterPos[0], firstLetterPos[1])
    fill(colors[1 if secondColor > 0 else 0])
    text(initials[1], secondLetterPos[0], secondLetterPos[1])
   
    firstColor = 0; secondColor = 0
   
def keyPressed():
    if keyCode in initials:
            isKeyPressed[keyCode] = 1
    if str(key).upper() in initials:
            isKeyPressed[str(key).upper()] = 1
       
def keyReleased():
    if keyCode in initials:
            isKeyPressed[keyCode] = 0
    if str(key).upper() in initials:
            isKeyPressed[str(key).upper()] = 0
 
def hover(x, y):
    return (1 if (mouseX >= x and mouseX <= x + sizeofText and
                 mouseY >= y and mouseY <= y + sizeofText)
             else 0)
