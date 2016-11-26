import os,sys
from utils import Board

class Play:

    def __init__(self,board,state):
        """ """

        self.board = board 
        self.player = 1
        self.state = state

    def get_column(self,column):
        return [self.state[row][column] for row in range(self.board.width)] 

    def column_height(self,column,**kwargs):
        col = self.get_column(column)
        try:
            col_height = col.index(0)
        except:
            col_height = self.board.height 
        return col_height


    def available_plays(self, **kwargs):
        """return columns numbers that can be dropped into """
        state = kwargs.get('state', self.state)
        plays = []
        for irow in range(self.board.width):
            #if state[irow][self.board.height - 1] == 0:
            if self.column_height(irow) < self.board.height:
                plays.append(irow)
        return plays

    def make_play(self,play_row):
        
        player = self.player
        self.state[self.column_height(play_row)][play_row] = player

        self.player = 1 if player == 2 else 2

        return 1
    
        
        
        
        

        plays = []
        return plays