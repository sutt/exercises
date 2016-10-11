#http://puzzles.bostonpython.com/hinomaru.html
import os, sys, random, time, math

from data.data import import_data

from utils.utils import recurse_dims, mod
from utils.utils import Solution    
from utils.utils import strikeout
from utils.types import tileHolder, playHolder

SOLUTION, TILES = import_data()

#Solution functions and mappings
_SYVECS, _SXDOTS = recurse_dims(SOLUTION)
sol = Solution( s=SOLUTION, _Y=_SYVECS, _X=_SXDOTS)

#Build all possilbe Plays
play = playHolder()

_TILES, _SIDES,_TYVECS, _TXDOTS = recurse_dims(TILES)

tile_dims = (_TXDOTS,_TYVECS)
modx, mody = mod(tile_dims,_SXDOTS), mod(tile_dims,_SYVECS)
Z,Flip = range(2),range(2)

combos = [ play(tilenum,tileside,x,y,z,flip) \
                for tilenum in range(_TILES) \
                for tileside in range(_SIDES) \
                for x in modx \
                for y in mody \
                for z in Z    \
                for flip in Flip ]
                
print len(combos)

#Reduce combos to valid plays
valids = filter(lambda play_i: sol.match_tile_to_board(TILES,play_i), combos) 
print len(valids)

#Enhance the information on each play-object
valids_misc = map(lambda p: sol.xyt(p) ,valids)
print valids_misc[:3]



#Analyze preprocessed data and heuristic computed from data
so = [[] for i in range(len(valid2))]
for i in range(len(valid2)) :
    so[i].extend(strikeout(i))
    
print so[:5]
outs = map(len,so)
print '----'
print outs
print '----'
print max(outs),min(outs)


def puzzle(**kwargs):
    layout = []
    struckout = []
    allv = range(len(valid2))
    log = []
    valid3 = [(i,v) for i,v in enumerate(valid2)]
    Log = kwargs.get('Log',False)
    
    for try_i in range(kwargs.get('tries',20)):

        if len(layout) == 12: 
            print 'SUCCESS:', layout
            print 'IN TRIES:', try_i
            if Log:
                return (layout,log)
            else:
                return (layout,try_i)

        if len(struckout) > 0:
            notavail = reduce(lambda x,y: x+y, struckout)
        else:
            notavail = ()
        available = [x for x in allv if x not in notavail]

        #Prune Condition: Not enough valid plays to complete puzzle.
        if len(available) < (12 - len(layout)):
            
            back = random.randint(1,len(layout))
            if kwargs.get('allback',False): back = len(layout)
            if Log: log.append([(try_i, "_BACK:", back)])
                           
            for b in range(back):
                lp = layout.pop()
                sp = struckout.pop()
                if Log: log.append([(try_i, "POP:", lp)])
                
        else:
            
            #Extend layout list with a play from available list
            r = random.sample(available,1)[0]
            layout.append(r)
            struckout.append(so[r])
            if Log: log.append([(try_i, "_APP:", len(layout), layout[:])])

    return log

ret = puzzle(tries = 20, Log=True)

ret2 = reduce( lambda x,y: str(x) + "\n" + str(y), ret)
print ret2


#ret = puzzle(tries = 100000, Log=False)

#Run a search
wins = []
for trial in range(2):
    wins.append(puzzle(tries=100000,Log = False))   
print wins    

win1 = wins[0][0]
win_v = [valid2[w] for w in win1]

#printout results
letters = 'abcdefghijkl'
letters = list(letters)
dletters = {}
for i,v in enumerate(letters):
    dletters[i]=v.capitalize() 
print dletters


def build_puzzle_letter(inp_rows):
    s = ""
    for row in inp_rows:
        s += "".join(row)
        s += "\n"
    return s

def build_puzzle_mark(inp_rows):
    s = ""
    for row in inp_rows:
        s += "".join(str(row))
        s += "\n"
    return s

def lookup_letter(xyt):
    v = filter(lambda v: xyt in v[5],win_v)
    try:
        tilenum = v[0][4]
        return dletters[tilenum]
    except:
        return "?"
    
def code2xy(xyt):
    y = int(xyt / 18)
    x =  xyt % 18
    return (x,y)

def lookup_mark(xyt):
    vv = filter(lambda v: xyt in v[5],win_v)
    try:
        v = vv[0]
        tside = v[2]
        tdata = v[0][tside]
        
        z,f =  v[3][2], v[1]
        
        x0,y0, = v[3][0], v[3][1]
        x1, y1 = code2xy(xyt)
        x,y = x1 - x0, y1 - y0
        #return str(x)
        #return str(1)
        return str(tilemark(tdata,x,y,z,f))
    except:
        return "?"

rows,rows2 = [], []
for y in range(12):
    row,row2 = "",""
    for x in range(18):
        xyt = x + (y*18)
        row += lookup_letter(xyt)
        row2 += lookup_mark(xyt)
    rows.append(row)
    rows2.append(row2)
    
out = build_puzzle_letter(rows)
print out

out = build_puzzle_mark(rows2)
print out

