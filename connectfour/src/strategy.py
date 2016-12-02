import os,sys,time,random

from play import Play
from utils import Log


class KnownRules:
    
    def __init__(self, players = (1,2), **kwargs ):
        
        self.players = players    # which players to apply the rules to
        self.connect_three_me = kwargs.get('c3me', False)
        self.connect_three_you = kwargs.get('c3you', False)

    def test_connect_three_me(self,current_play, passin_board,**kwargs):
        
        if not(self.test_connect_three_me): return False

        temp_log = Log(noisy = False)

        available_plays = play.available_plays()

        for play_col_i in range(play.board.width):
            
            temp_play = Play(board = passin_board, state = copy.deepcopy(current_play.state))
            
            if not(play_col_i in available_plays): continue
            
            temp_play.make_play(play_col_i)

            if temp_play.check_win(log = None):
                return  
            
        return False
                

            


    def connect_three(self,data):
        
        return True

