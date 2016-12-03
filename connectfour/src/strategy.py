import os,sys,time,random, copy

from play import Play
from utils import Log


class KnownRules:
    
    def __init__(self, players = (1,2), **kwargs ):
        
        self.players = players    # which players to apply the rules to
        self.connect_three_me = kwargs.get('c3me', False)
        self.connect_three_you = kwargs.get('c3you', False)

    def test_connect_three_me(self,current_play, passin_board, passin_log, **kwargs):
        
        if not(self.test_connect_three_me): return False
        if not( current_play.player in self.players): return False

        temp_log = Log(noisy = False)
        available_plays = current_play.available_plays()

        for play_col_i in range(current_play.board.width):
            
            temp_play = Play(board = passin_board, \
                             state = copy.deepcopy(current_play.state), \
                             player_init = copy.copy(current_play.player))
            
            if not(play_col_i in available_plays): continue
            
            temp_play.make_play(play_col_i, switch_player = False)

            if temp_play.check_win(log = passin_log):
                return  play_col_i
            
        return -1
                

            


    def connect_three(self,data):
        
        return True

