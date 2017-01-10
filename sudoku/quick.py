import copy
import os
import random
import sys

#easy
p1 = """
410070005
080006090
000500000
007401300
530000012
004308700
000004000
090800070
700060028
"""
#hard
p1 = """
000084020
100002500
000007006
078005001
004206900
600800240
700400000
003700009
010560000
"""

#evil
p0 = """
000004200
500000004
040960000
008030070
405070902
060020400
000043080
700000003
001800000
"""

#evil
p1 = """
000004200
500000004
040960000
008030070
405070902
060020400
000043080
700000003
001800000
"""

print p0 == p1  #yes you typed it in the same type
def text_to_puzzle(text):
    return filter(str.isdigit,text)
    
def string_to_puzzle(string, spaces = False):
    s = ""
    for i in range(9):
       line = string[ (i*9) : ((i+1)*9)]
       if spaces: 
           line = ' '.join(list(line))
       s += line
       s+= "\n"
    return s

def ij_to_c(i,j): return (i * 8) + j

def c_to_ij(c): return ((c/9),c%9)

def return_shares():
    board = range(81)
    cols = [[c for c in board if (c%9) == col ] for col in range(9)]
    rows = [[c for c in board if (c/9) == row ] for row in range(9)]
    areas = [[c for c in board if c_to_ij(c)[0] / 3 == i and c_to_ij(c)[1] / 3 == j ] for i in range(3) for j in range(3)]   #across, then down
    return rows, cols, areas

p = text_to_puzzle(p1)

rows, cols, areas = return_shares()
#print rows[0]

def get_that( ind, board):
    return [board[i] for i in ind]

#print get_that(rows[0], p)
#print get_that(areas[5], p)
def fun(i,p):
    if p[i] == '0':
        return tuple(map(str,range(1,10)))
    else:
        return tuple(p[i])

board = range(81)
space = tuple([fun(i,p) for i in board])

space = tuple([fun(i,space) for i in board])
#print space[:5]

# each spot has three constraints associated with iter
#for i in board:

#each of the spaces forms a constraint
shares = []
shares.extend(areas)
shares.extend(rows)
shares.extend(cols)
#print shares
#print len(shares)



def constraint(space):
    
    cntr = 0
    needed = (set(map(str,range(1,10))))
    space2 = list(space)[:]

    for _i in range(10):
        
        spots_1 = len(filter(lambda x: len(x) == 1, space))

        for s in shares:
            
            knowns = set()
            for spot in s:
                if len(space[spot]) == 1:
                    knowns = knowns.union(space[spot])
            
            for spot in s:
                if len(space[spot]) != 1:
                    space2[spot] = tuple(filter(lambda k: k not in knowns, space[spot]))
                    if len(space2[spot]) == 0:
                        return -1

            #needed = set(map(str,range(1,10)).difference(knowns))
            for spot in s:
                if len(space[spot]) != 1:
                    _s = s[:]
                    _s.remove(spot)
                    available = map(lambda c: space[c], _s)
                    available = [item for sublist in available for item in sublist]
                    available = set(available)
                    if len(available) < 9:
                        space2[spot] = tuple(needed.difference(available))

            space = tuple(space2[:])
        
        #--- shares ----------------
        
        spots_2 = len(filter(lambda x: len(x) == 1, space))
        
        print str(spots_2)
        
        if spots_2 - spots_1 == 0:
            cntr +=1
        else:
            cntr = 0
        if cntr == 2:
            print 'exiting...'
            return space



#discovered = filter(lambda i: len(space[i]) == 1 and int(p[i]) == 0, board)
#print discovered
#print map(c_to_ij,discovered)
#print get_that(discovered,space)



def print_opens(space):
    a = filter(lambda x: len(x) > 1, space)
    s = ""
    b = [ str((i,v)) for i,v in enumerate(a)]
    print '\n'.join(b)
    return 1

#print len(filter(lambda x: int(x) > 0, p))

def search(space):
    
    opens = filter(lambda x: len(x) > 1, space)
    min_open = min(map(lambda x: len(x), opens))
    ind = map(lambda x: len(x), space).index(min_open)

    possible = space[ind]
    print possible
    guess = random.sample(possible,1)[0]
    print 'guess: ',str(guess)
    def add_guess(i):
        if i  == ind:
            return tuple(guess)
        else:
            return space[i]

    
    space2 = tuple([add_guess(i) for i in board])
    return space2


#MAIN

print 'printing known spaces on each iter'
print len(filter(lambda x: len(x) == 1, space))
constraint(space)

space = constraint(space)

for i in range(20):    
    save_space = space[:]
    space = search(space)
    space = constraint(space)
    if space == -1:
        space = saved_space
    
    if len(filter(lambda x: len(x) == 1, space)) == 81:
        puzzle81 = text_to_puzzle(p1)
        print string_to_puzzle(puzzle81, spaces=True)

        space_str = [item for sublist in space for item in sublist]
        space_str = ''.join(space_str)
        print string_to_puzzle(space_str, spaces=True)

#print map(len,space)


#Random thoughts -------

 #How to understand which rows/cols are part of which area? 
    #All rows meet all cols, but each area only hits 3 rows, 3 cols
    #each area shares common, rows+cols with 4 other areas

#working stuff --------
if False:
    puzzle81 = text_to_puzzle(p1)
    print puzzle81
    print 'len p1:', str(len(p1))
    print 'len puzzle81:', str(len(puzzle81))

    for i in range(12):
        print str(i), " : ", str(puzzle81[i])
