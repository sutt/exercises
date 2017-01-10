import os,sys, copy

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
print rows[0]

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
print space[:5]

# each spot has three constraints associated with iter
#for i in board:

#each of the spaces forms a constraint
shares = []
shares.extend(areas)
shares.extend(rows)
shares.extend(cols)
#print shares
#print len(shares)

needed = (set(map(str,range(1,10))))
space2 = list(space)[:]
for _i in range(5):
    
    for s in shares:
        
        knowns = set()
        for spot in s:
            if len(space[spot]) == 1:
                knowns = knowns.union(space[spot])
        
        for spot in s:
            if len(space[spot]) != 1:
                space2[spot] = tuple(filter(lambda k: k not in knowns, space[spot]))

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
    
    print len(filter(lambda x: len(x) == 1, space))
    discovered = filter(lambda i: len(space[i]) == 1 and int(p[i]) == 0, board)
    print discovered

print map(c_to_ij,discovered)

print get_that(discovered,space)

#print len(filter(lambda x: len(x) == 1, space))
print len(filter(lambda x: int(x) > 0, p))

puzzle81 = text_to_puzzle(p1)
print string_to_puzzle(puzzle81, spaces=True)

space_str = [item for sublist in space for item in sublist]
space_str = ''.join(space_str)
print string_to_puzzle(space_str, spaces=True)

print map(len,space)


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

 