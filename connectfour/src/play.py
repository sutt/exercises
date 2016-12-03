import os,sys, copy
from utils import Board
from utils import Log

class Play:

    def __init__(self,board,state, **kwargs):
        """ """
        self.board = board 
        self.player = kwargs.get('player_init', 1)
        self.state = state
        self.extra = False

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

    def make_play(self,play_row,**kwargs):
        
        player = self.player
        self.state[self.column_height(play_row)][play_row] = player
        
        if kwargs.get('switch_player', True):
            self.player = 1 if player == 2 else 2

        return 1
    
    @staticmethod
    def four(vec, ret_bool = True):
        """are there any 4-mer's within the vec that have the same player number? if true, return that players number """
        for player in [1,2]:
            win = any( map(lambda kmer: kmer == 4, [vec[i:i+4].count(player) for i in range(len(vec) - 4)] ) )
            if win:
                return True if ret_bool else player
        return False
        

    def check_win(self, log ,**kwargs):
        """return True if a player has won, well check all players since house rules could cause a random-action player to lose"""

        for i in range(self.board.height):
            row = self.state[i][:]        
            if self.four(row):
                player = self.four(row,ret_bool=False)
                if log is not None: log.game_win(player = player, win_type = 'row', win_type_ind = i)
                return True

        for i in range(self.board.height):
            col = self.get_column(i)[:]
            if self.four(col):        
                player =  self.four(col,ret_bool=False)
                if log is not None: log.game_win(player = player, win_type = 'col', win_type_ind = i)
                return True

        #mirror image horizontally "left-to-right" flip, check the diagonals again
        copy_state = copy.deepcopy(self.state)
        mirror_state = []
        for row in copy_state:
            mirror_state.append(row[::-1])
            
        
        for state_i in (self.state,mirror_state):

            #diagonals bottom-left is left-column "down and to right"-check
            for i in range(self.board.height):
                maxj = min( self.board.width, self.board.height ) - i 
                diag = [state_i[i+j][j] for j in range(0,maxj)]
                if len(diag) >= 4:
                    if self.four(diag):
                        player = self.four(diag, ret_bool = False)
                        if log is not None: log.game_win(player = player, win_type = 'diag_a', win_type_ind = i)
                        return True
                                        
            #diagonals bottom-left is bottom-row
            for i in range(self.board.width):
                maxj = min( self.board.width, self.board.height ) - i 
                diag = [state_i[j][i+j] for j in range(0,maxj)]
                if len(diag) >= 4:
                    if self.four(diag):
                        player = self.four(diag, ret_bool = False)
                        if log is not None: log.game_win(player = player, win_type = 'diag_b', win_type_ind = i)
                        return True
        return False
    
        
        
        
        

        plays = []
        return plays