import copy
import os
import random
import sys
import time

from play import Play
from utils import Log


class KnownRules:
    
    def __init__(self, players = (1,2), **kwargs ):
        
        self.players = players    # which players to apply the rules to
        self.connect_three_me = kwargs.get('c3me', (0,0))
        self.connect_three_you = kwargs.get('c3you', (0,0))
        self.fork_me = kwargs.get('forkme', (0,0))
        self.fork_you = kwargs.get('forkyou', (0,0))

    def test_connect_three_me(self,current_play, passin_board, passin_log, **kwargs):
        
        if not( current_play.player in self.connect_three_me): return -1

        available_plays = current_play.available_plays()

        for play_col_i in range(current_play.board.width):
            
            temp_play = Play(board = passin_board, \
                             state = copy.deepcopy(current_play.state), \
                             player_init = copy.copy(current_play.player))
            
            if not(play_col_i in available_plays): continue
            
            temp_play.make_play(play_col_i, switch_player = False)

            if temp_play.check_win(log = None):
                return  play_col_i
            
        return -1
                
    def test_connect_three_you(self,current_play, passin_board, passin_log, **kwargs):
        
        if not( current_play.player in self.connect_three_you): return -1
            
        available_plays = current_play.available_plays()

        current_player = copy.copy(current_play.player)
        other_player = 1 if current_player == 2 else 2 

        list_blocking_plays = []
        for play_col_i in range(current_play.board.width):
            
            temp_play = Play(board = passin_board, \
                             state = copy.deepcopy(current_play.state), \
                             player_init = other_player)
            
            if not(play_col_i in available_plays): continue
            
            temp_play.make_play(play_col_i, switch_player = False)

            if temp_play.check_win(log = None):
                list_blocking_plays.append(play_col_i)

        if len(list_blocking_plays) > 0:
            if kwargs.get('ret_multi',False):
                return list_blocking_plays
            else:
                return list_blocking_plays[0]
        
        return -1


    def test_fork_me(self, current_play, passin_board, log, **kwargs):
        """ this looks for forks you can play, where you create two connect3's simulatenously"""

        if not( current_play.player in self.fork_me): return -1

        for play_col_i in range(current_play.board.width):
            
            temp_play = Play(board = passin_board, \
                             state = copy.deepcopy(current_play.state), \
                             player_init = copy.copy(current_play.player))
            
            available_plays = current_play.available_plays()
            if not(play_col_i in available_plays): continue
            
            temp_play.make_play(play_col_i, switch_player = True)

            blocking_cols = self.test_connect_three_you(temp_play,passin_board, log, ret_multi = True)
            
            if blocking_cols == -1: continue
            
            if len(blocking_cols) > 1:
                return play_col_i

        return -1

    def final_strat(self,iter_strats, **kwargs):
        
        ret_strat_1, ret_strat_2 = iter_strats[0], iter_strats[1] 
        if len(iter_strats) > 2: ret_strat_3 = iter_strats[2]

        ret_col = -1
        ret = (ret_col,None) 

        if ret_strat_1 > -1:
            ret =  (ret_strat_1, 'Winner')
        elif ret_strat_2 > -1:
            ret =  (ret_strat_2, 'Block')
        elif ret_strat_3 > -1:
            ret =  (ret_strat_3, 'Fork')

        return ret

    def strategize(self, play, log, board, **kwargs):

        ret_strat_1 = self.test_connect_three_me( play, board, log )
        ret_strat_2 = self.test_connect_three_you( play, board, log ) 
        ret_strat_3 = -1
        if ret_strat_1 == -1 and ret_strat_2 == -1:
            ret_strat_3 = self.test_fork_me( play, board, log )
        
        ret_strat, strat_type = self.final_strat(iter_strats = (ret_strat_1, ret_strat_2, ret_strat_3), noisy = False)
        
        ret = (ret_strat, strat_type)

        return ret

