import os, sys, random

from src.utils import Board
from src.play import Play

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
#INIT_STATE = [[0 for row in range(BOARD_WIDTH)] for col in range(BOARD_HEIGHT)]  
import copy

# class Data:
#     INIT_STATE = [[0 for row in range(BOARD_WIDTH)] for col in range(BOARD_HEIGHT)]

def main():
    
    board = Board(BOARD_WIDTH,BOARD_HEIGHT)
    INIT_STATE = [[0 for row in range(BOARD_WIDTH)] for col in range(BOARD_HEIGHT)]    

    for game in range(10):
        print "GAME: ", str(game)
        
        local_data = copy.deepcopy(INIT_STATE)
        play = Play(board = board, state = local_data)
        
        for i in range(100):
            
            ap = play.available_plays()

            if len(ap) < 1:
                print 'Game Ends in Draw at i: ', str(i)
                break

            play.make_play(random.sample(ap,1)[0])

            if play.check_win(play = i):
                if play.extra:  #a diag-win
                    print 'WINNING at i:', str(i)
                    board.print_board(board_state = play.state[:], board_header = True)
                break

    


if __name__ == "__main__":
    main()
