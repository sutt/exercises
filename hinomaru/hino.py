#http://puzzles.bostonpython.com/hinomaru.html
import os, sys, random, time, math

from data.data import import_data

from utils.utils import recurse_dims, mod
from utils.utils import Solution    
from utils.utils import strikeout
from utils.types import tileHolder, playHolder, playplusHolder
from utils.search import puzzle

from utils.printout import build_solution_graphic

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
#so_data = zip([p.tilenum for p in valids], valids_misc)
so = [strikeout(i,v,valids,valids_misc) for i,v in enumerate(valids)]

    
print so[:1]
print so[1:2]
outs = map(len,so)
print '----'
print outs
print '----'
print max(outs),min(outs)


#demo puzzle algo
ret = puzzle(valids, so, tries = 20, Log=True)
ret2 = reduce( lambda x,y: str(x) + "\n" + str(y), ret)
print ret2


#Run a search
def do_some(some):
    if some:
        wins = []
        for trial in range(2):
            wins.append(puzzle(valids, so, tries=100000,Log = False))   
        print wins    
    else:
        wins = [([104, 30, 64, 119, 45, 13, 63, 35, 76, 111, 89, 11], 4848), ([17, 10, 116, 65, 44, 62, 90, 107, 34, 82, 110, 33], 8738)]
    return wins
    
wins = do_some(False)

#Printout results
win1 = wins[0][0]
playplus = playplusHolder()
ppWin1 = [playplus(play = valids[w] \
                   ,xyt = valids_misc[w] \
                   ,data = TILES[valids[w].tilenum] \
                    )  for w in win1]

out = build_solution_graphic(ppWin1, sol, dots=False)
print out

out = build_solution_graphic(ppWin1, sol, dots=True)
print out

print ppWin1[0]
