def setup():
    size(600, 600)
    rectMode(RADIUS)
    imageMode(CENTER)
    noStroke()
    
    global bluepic
    bluepic = loadImage('Pinwheel blue.png')
    global graypic
    graypic = loadImage('Pinwheel gray.png')
    
i = 0
dir = 2.5

def draw():
    global i
    global dir
    
    if dir > 0: #if i < 90
        background(28)
        unitarray(0, 0, 7, 7, 50, i, bluepic)
    else:
        background(41, 144, 234)
        unitarray(-100, 0, 8, 8, 50, i, graypic)
    
    i += dir
    if i >= 90 or i <= 0:
        dir = dir*-1
    
    #if frameCount < 73:
    #    saveFrame('frame-###.png')
    
    """i += 2.5
    if i <= 180:
       i = 0"""  #For gray going forwards
    
def imgunit(x, y, d, photo):
    pushMatrix()
    translate(x, y)
    rotate(radians(d))
    
    image(photo, 0, 0)
    
    popMatrix()
    
def unitarray(x, y, w, h, r, d, photo):
    for over in range(w):
        if over % 2 == 0:
            for down in range(ceil(h/2.0)):
                imgunit(x + over*2*r, y + down*4*r, d, photo)
        else:
            for down in range(floor(h/2.0)):
                imgunit(x + over*2*r, y + 2*r + down*4*r, d, photo)
                