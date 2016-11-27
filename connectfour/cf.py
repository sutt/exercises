import os, sys, random, copy, time, argparse

from src.utils import Board
from src.play import Play
from src.utils import Log

ap = argparse.ArgumentParser()
ap.add_argument("--analytics", action="store_true", default=False)
ap.add_argument("--stat", default='t')
ap.add_argument("--readfile", default="")
ap.add_argument("--runs", default = 10)
args = vars(ap.parse_args())

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
INIT_STATE = [[0 for row in range(BOARD_WIDTH)] for col in range(BOARD_HEIGHT)]

def batch():
    
    board = Board(BOARD_WIDTH,BOARD_HEIGHT)  #refactor out board
    log = Log(noisy = True)

    for game_i in range(args['runs']):
        
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
            if play.check_win(log = log):    #this writes to log too
                log.game_win_print(win_state = play.state)    
                break

        log.game_end()

    log.end_runs()


def analytics(**kwargs):

    log = Log(noisy = False)
    data = log.load_from_file(filename = args['readfile'] ) 
    stat_str = kwargs.get('stat', args['stat'])
    stat = log.get_stat(data, stat = stat_str )

    
    #filter the Nones
    stat_v = [val for val in stat if val is not None]

    #analytics
    avg = float(sum(stat_v)) / float(len(stat_v))
    _min, _max = min(stat_v), max(stat_v)
    
    print 'Var: ', str(stat_str.upper())
    print 'N: ', str(len(stat))
    print 'Avg: ',  str(avg)[:5]
    print 'Min: ', str(_min), ' Max: ', str(_max)


if __name__ == "__main__":
    if args['analytics']: 
        analytics()
    else:
        batch()
