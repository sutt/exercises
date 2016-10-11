from utils.types import tileHolder, playHolder

play = playHolder()
p1 = play(1,2,3,4,5,6)

#'tile_num tileside x y z flip'
print p1
print p1.tileside

p = [[1,2,3],[4,5,6]]
w = [q[::-1] for q in p[::-1]]
print w

from collections import namedtuple as nt

tt = nt('i'=2,'j'=3)
print tt