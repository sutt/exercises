import os, sys, random, copy, time, argparse

from src.utils import Board
from src.play import Play
from src.utils import Log
from src.strategy import KnownRules   #add .find_fork - this should open game back up


ap = argparse.ArgumentParser()

ap.add_argument("--analytics", action="store_true", default=False)
ap.add_argument("--stat", default='t')
ap.add_argument("--readfile", default="")
ap.add_argument("--pct_analytics", default ="")

ap.add_argument("--runs", default = 1)

def_arg = "(0,0)" #"(1,2)"  for debugging
ap.add_argument("--strat_me", default = def_arg) #action="store_true", default=False)
ap.add_argument("--strat_you", default = def_arg) #action="store_true", default=False)
ap.add_argument("--strat_fork", default = def_arg) #action="store_true", default=False)
ap.add_argument("--strat_players", default="(1,2)")
ap.add_argument("--board_height", default="8")
ap.add_argument("--board_width", default="8")

ap.add_argument("--noisy_gamewin", action="store_true", default=False)
ap.add_argument("--noisy_strat", action="store_true", default=False)

args = vars(ap.parse_args())

c3me, c3you, forkme,  = eval(args['strat_me']), eval(args['strat_you']), eval(args['strat_fork'])
strat_players = eval(args['strat_players'])
BOARD_WIDTH = int(args["board_width"])
BOARD_HEIGHT = int(args["board_height"])


INIT_STATE = [[0 for col in range(BOARD_WIDTH)] for row in range(BOARD_HEIGHT)]

def batch():
    
    log = Log(noisy = False, noisy_win = args["noisy_gamewin"])
    board = Board(BOARD_WIDTH,BOARD_HEIGHT)
    log.batch_board_params(board)
    
    #AI-Rules
    strat = KnownRules(players = strat_players ,c3me = c3me ,c3you = c3you , forkme = forkme)
    log.batch_strat_params(strat)

    for game_i in range(int(args['runs'])):
        
        log.game_start(game_i = game_i)       
        play = Play(board = board, state = copy.deepcopy(INIT_STATE))
        
        for i in range(BOARD_WIDTH*BOARD_HEIGHT + 1):
            
            #ACTION-SPACE
            ap = play.available_plays()
            if len(ap) < 1:
                log.game_tie()
                break

            #DECISION-ACTION
            ret = strat.strategize(play,log,board) 
            log.strat_played(ret, play, noisy = args["noisy_strat"] )
            
            playcol = ret[0] if int(ret[0]) > -1 else random.sample(ap,1)[0]
            log.game_play(playcol, play)
            play.make_play(playcol)
            

            #EVAL-PAYOFF-FUNCTION
            if play.check_win(log = log):    #this writes to log too
                log.game_win_print(win_state = play.state, noisy = args["noisy_gamewin"])    
                break

        log.game_end()

    log.end_runs()


def analytics(**kwargs):

    # python cf.py --analytics --readfile output12.txt --stat t
    # python cf.py --analytics --readfile output12.txt --stat win_player --pct_analytics 1
    # python cf.py --runs 300 --strat_player (1,) --strat_me --strat_you
    # python cf.py --runs 300 --strat_fork (1,)
    # python cf.py --analytics --readfile output91.txt --stat win_player --pct_analytics 1

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
    print 'N: ', str(len(stat_v))
    print 'Avg: ',  str(avg)[:5]
    print 'Min: ', str(_min), ' Max: ', str(_max)

    if len(args['pct_analytics']) > 0:

        match = str(args['pct_analytics'])

        num_match = [str(x) for x in stat_v].count(match)

        pct_match = 100.0 * float(num_match) / float(len(stat_v))

        print 'PCT of ', stat_str, ' = ', match , ' : ', str(pct_match)[:5]

if __name__ == "__main__":
    if args['analytics']: 
        analytics()
    else:
        batch()
