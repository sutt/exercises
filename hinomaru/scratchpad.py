from utils.types import tileHolder, playHolder

#inp_rows = rows_letter if kwargs.get('dots',False) else rows_mark

w = 1 if False else 2
print w
a = list('abc')
print a

play = playHolder()
p1 = play(1,2,3,4,5,6)

from utils.types import tileHolder, playHolder
play = playHolder()
p2 = play(flip=10,tilenum=1,tileside=1,x=1,y=0,z=0)
print p2

class MyClass:
    def hello(self):
        print 'World'
        return 1

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
        # X allow it to start with a certain known layout
        # X back a random amount
        # X select from available
        # TOTAL_PLAYS constant: (solution_area / tile area)
            #another way to do this is (tiles / sides)
    
    #after search result
        # X modularize
        # X refactor tilemark ->solution.get_tile_dot
        # refactor hardcoded 

###TODO 10/20
    #Xpuzzle - get a win
    #Xprintout - get a printout
    
    # why is this version so much faster than ipython? 
        #because valids is much smaller than valid2?
    
    #[([104, 30, 64, 119, 45, 13, 63, 35, 76, 111, 89, 11], 4848), ([17, 10, 116, 65, 44, 62, 90, 107, 34, 82, 110, 33], 8738)]
    
###TODO 10/22

    # X puzzle takes a set of valids into layout
    #  little refactoring up top for consistency
    
###Notes 10/28
    #HackerRank, LeetCode, TopCoder, CodeFights, Stockfighter, etc.?
    #http://play.elevatorsaga.com/
    #Starfighter obituary: https://news.ycombinator.com/item?id=12415786
