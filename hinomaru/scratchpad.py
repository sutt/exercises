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
    
    #after search result
        # Xmodularize
        # refactor tilemark ->solution.get_tile_dot