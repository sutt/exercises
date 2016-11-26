import os, sys, random

from src.utils import Board
from src.play import Play

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
STATE = [[0 for row in range(BOARD_WIDTH)] for col in range(BOARD_HEIGHT)]  


def main():
    #for i in range(PLAYS):
    board = Board(BOARD_WIDTH,BOARD_HEIGHT)    
    board.print_board(board_header = True)

    play = Play(board = board, state = STATE)

    
    for i in range(100):
        
        ap = play.available_plays(state = STATE)
        
        if len(ap) < BOARD_WIDTH:
            print 'exiting i: ', str(i)
            print 'Available Plays:'
            print ap
            break

        play_1 = random.sample(ap,1)[0]
        ret = play.make_play(play_1)
        
    board.print_board(board_state = play.state[:], board_header = True)


if __name__ == "__main__":
    main()
