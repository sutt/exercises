import os, sys, random, copy, time

from src.utils import Board
from src.play import Play
from src.utils import Log

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
INIT_STATE = [[0 for row in range(BOARD_WIDTH)] for col in range(BOARD_HEIGHT)]

def main():
    
    board = Board(BOARD_WIDTH,BOARD_HEIGHT)  #refactor out board
    log = Log(noisy = True)

    for game_i in range(10):
        
        log.game_start(game_i = game_i)       
        play = Play(board = board, state = copy.deepcopy(INIT_STATE))
        
        for i in range(BOARD_WIDTH*BOARD_HEIGHT + 1):
            
            #ACTION-SPACE
            ap = play.available_plays()
            if len(ap) < 1:
                log.game_tie()
                break
            
            #DECISION-ACTION
            play.make_play(random.sample(ap,1)[0])
            log.game_play()

            #OBSERVE
            if play.check_win():    #this writes to log too
                log.game_win(win_state = play.state)    
                break

        log.game_end()

    log.end_runs()


if __name__ == "__main__":
    main()
