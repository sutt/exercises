from utils.types import tileHolder, playHolder

a = list('abc')
print a

play = playHolder()
p1 = play(1,2,3,4,5,6)

#'tile_num tileside x y z flip'
print p1
print p1.tileside

p = [[1,2,3],[4,5,6]]
w = [q[::-1] for q in p[::-1]]
print w

from collections import namedtuple as nt

#tt = nt('i'=2,'j'=3)
#print tt

###TODO 10/18
    # search.puzzle()
        # allow it to start with a certain known layout
        # back a random amount
        # select from available
        # TOTAL_PLAYS constant: (solution_area / tile area)
            #another way to do this is (tiles / sides)
    
    #after search result
        # Xmodularize
        # refactor tilemark ->solution.get_tile_dot
        # refactor hardcoded 

###TODO 10/20
    #Xpuzzle - get a win
    # printout - get a printout
    
    # why is this version so much faster than ipython? 
        #because valids is much smaller than valid2?
    
    [([104, 30, 64, 119, 45, 13, 63, 35, 76, 111, 89, 11], 4848), ([17, 10, 116, 65, 44, 62, 90, 107, 34, 82, 110, 33], 8738)]