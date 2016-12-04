import os,sys,time,random, copy

from play import Play
from utils import Log


class KnownRules:
    
    def __init__(self, players = (1,2), **kwargs ):
        
        self.players = players    # which players to apply the rules to
        self.connect_three_me = kwargs.get('c3me', (0,0))
        self.connect_three_you = kwargs.get('c3you', (0,0))

    def test_connect_three_me(self,current_play, passin_board, passin_log, **kwargs):
        
        if not( current_play.player in self.connect_three_me): return -1

        temp_log = Log(noisy = False)
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

        temp_log = Log(noisy = False)
        available_plays = current_play.available_plays()

        current_player = copy.copy(current_play.player)
        other_player = 1 if current_player == 2 else 2 

        for play_col_i in range(current_play.board.width):
            
            temp_play = Play(board = passin_board, \
                             state = copy.deepcopy(current_play.state), \
                             player_init = other_player)
            
            if not(play_col_i in available_plays): continue
            
            temp_play.make_play(play_col_i, switch_player = False)

            if temp_play.check_win(log = None):
                return  play_col_i
            
        return -1

    def final_strat(self,iter_strats, **kwargs):
        
        ret_strat_1, ret_strat_2 = iter_strats[0], iter_strats[1] 
        
        ret_strat = -1 

        if ret_strat_1 > -1:
            return (ret_strat_1, 'Winner')
        elif ret_strat_2 > -1:
            return (ret_strat_2, 'Block')

        return (ret_strat, None)

    

