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

rows, cols, areas = return_shares()
print rows[0]


def get_that( ind, board):
    return [i for i in ind]
    #return [board[i] for i in ind]

p = text_to_puzzle(p1)
print p[2]

print get_that[rows[0][:], p]
print get_that[areas[5], p]

#puzzle81 = text_to_puzzle(p1)
#print string_to_puzzle(puzzle81, spaces=True)



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
