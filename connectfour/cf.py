import os, sys, random

print 'connect four'

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

def print_board(**kwargs):
    
    _blank, _X, _O = "~", "X", "O"
    
    lines = [ list(_blank * BOARD_WIDTH) for _ in range(BOARD_HEIGHT)]
    
    state = kwargs.get('board_state',[])
    
    if len(state) != 0:
        #lines = process_state(lines,_X,_O)
        pass 
    
    out = ""
    
    if kwargs.get('board_header',False):
        out += " ".join([str(i) for i in range(BOARD_WIDTH)]) 
        out += "\n"

    for line in lines:
        out += " ".join(line) + "\n"
    print out


def main():
    #for i in range(PLAYS):    
    print_board(board_header = True)


if __name__ == "__main__":
    main()
