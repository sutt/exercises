import random

winners = [[1,5,9],[3,5,7],[4,5,6],[2,5,8]]

def win(p):
    return 3 in map(lambda x1: sum(map(lambda x2: x2 in p, x1)), winners)

def game(**kwargs):
    x, o = [], []
    turn = 1
    spots = range(1,10)
    gridout = kwargs.get('gridout', False)
    
    for i in range(9):
        
        new = random.sample(spots, 1)[0]
        spots.remove(new)
        
        if turn == 1:
            x.append(new)
        else:
            o.append(new)
            
        if win(x):return ( 1, [1,x,o]) [1*gridout]
        if win(o):return (-1, [-1,x,o])[1*gridout]
        
        turn = 1 if turn != 1 else 2
        
    return ( 0, [0,x,o]) [1*gridout]

def n2g(n):
    return ((n - 1) / 3) + n - 1

def grid(g,**kwargs):
    win,x,o = g[0],g[1],g[2]
    
    vec = "~"*3
    vec +="\n"
    mat = vec*3

    xs = [n2g(a) for a in x]
    os = [n2g(a) for a in o]
    
    for a in xs:
        mat = mat[:a] + "X" + mat[a+1:]
    for a in os:
        mat = mat[:a] + "O" + mat[a+1:]
    
    if kwargs.get('winner',False):
        vec = " " + str(win)
        mat += vec  
    return mat
	
def multi(N):
    out = [game() for i in range (N)]
    #print out[:40]
    print " winO, draw, winX: "+ " | ".join(map(lambda x: str(out.count(x)),[-1,0,1]) )
    print "advantage: ", str(sum(out))

for i in range(10):
    print grid( game(gridout = 1), winner = True) 
    print "\n"
	
multi(100000)
multi(100000)
multi(100000)