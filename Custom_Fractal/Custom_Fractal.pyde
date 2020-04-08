from math import atan2

def setup():
    size(3600, 2000)
    colorMode(HSB, 1000, 100, 100)   #2nd param is value at which hues wrap around

GLOS = [(1780, 980), (1820, 980), (1820, 1020), (1000, 1000), (1020, 1020)]#, (980, 980)]
SELECTED = -1
SAVE = False
DRAW = True
SIZE = 16
DEPTH = 4



def draw():
    global SELECTED
    global DEPTH
    global SAVE
    global DRAW
    global RELS
    global preDepth
    
    if keyPressed:
        if int(key) in list(range(1, 10)):
            SAVE = True
            DRAW = True
            preDepth = DEPTH
            DEPTH = int(key)
            print('Saving at depth ' + str(DEPTH))
        elif key == 'p':
            print(GLOS)
    
    RELS = globalToRel()
    
    if DRAW:#frameCount == 1 or SELECTED > -1 or SAVE:
        
        background(0, 0, 100)   #(255)
    
        strokeWeight(1)
        #stroke(0, 0, 0, 100)
        fractal( (GLOS[0][0], GLOS[0][1]), (GLOS[-1][0], GLOS[-1][1]), DEPTH )
    
        if not SAVE:
            strokeWeight(SIZE)
            stroke(0, 0, 0, 150)
            for glo in GLOS:
                point( glo[0], glo[1] )
    
    DRAW = True
    if not SAVE:
        if mousePressed:
            if SELECTED == -1:
                for n in range(len(GLOS)):
                    if dist(mouseX, mouseY, GLOS[n][0], GLOS[n][1]) <= SIZE/2.0:
                        SELECTED = n
            else: GLOS[SELECTED] = (mouseX, mouseY)
        else:
            SELECTED = -1
            DRAW = False
    
    else:
        saveFrame('frame_####.png')
        print('...Done!')
        DEPTH = preDepth
        SAVE = False

    

def fractal(A, B, depth):
    """
    A is (x, y) float tuple of starting point
    B is (x, y) float tuple of ending poing
    depth is integer of recursion depth
    """
    theta = atan2( A[1]-B[1], B[0]-A[0] )
    disAB = dist( A[0], A[1], B[0], B[1] )
    
    # Make list of global point coords from relative data
    points = [A]
    for rel in RELS:
        points.append((A[0] - disAB*rel[0]*cos(PI-theta) + disAB*rel[1]*cos(PI+HALF_PI-theta),
                       A[1] - disAB*rel[0]*sin(PI-theta) + disAB*rel[1]*sin(PI+HALF_PI-theta)))
    points.append(B)
    
    # Use global coords to recurse or draw
    if depth > 0:
        for n in range(len(points)-1):
            fractal( points[n], points[n+1], depth-1 )
    else:
        for n in range(len(points)-1):
            leng = dist( points[n][0], points[n][1], points[n+1][0], points[n+1][1] )
            stroke( 90, 100, (40-leng)%100)# (100-leng**2)%100  )#stroke( leng+530, 100, 100 )
            line( points[n][0], points[n][1], points[n+1][0], points[n+1][1] )
            
            
def globalToRel():
    
    rel = [(0.0, 0.0)]
    
    mainVec = ( GLOS[-1][0] - GLOS[0][0], GLOS[-1][1] - GLOS[0][1] )
    mainLen  = dist( 0, 0, mainVec[0], mainVec[1] )
    mainUnit = ( mainVec[0] / mainLen, mainVec[1] / mainLen )
    
    for n in range(1, len(GLOS)-1):
        # Vector from start global to n-th global
        vec = ( GLOS[n][0] - GLOS[0][0], GLOS[n][1] - GLOS[0][1] )
        
        # Dot product of vec & mainUnit gives component of vec along mainVec
        dotProd = vec[0] * mainUnit[0] + vec[1] * mainUnit[1]
        fracAlong = dotProd / mainLen
        
        alongMain = ( mainVec[0] * fracAlong, mainVec[1] * fracAlong )
        distPerp  = dist( 0, 0, vec[0] - alongMain[0], vec[1] - alongMain[1] )
        if vec[1] > alongMain[1]:
            distPerp = distPerp * -1
        fracPerp  = distPerp / mainLen
        
        rel.append( (fracAlong, fracPerp) )
    
    rel.append( (1.0, 0.0) )
    return rel