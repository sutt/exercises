import os,sys, copy
from utils import Board

class Play:

    def __init__(self,board,state):
        """ """
        self.board = board 
        self.player = 1
        self.state = state
        self.extra = False

    def reset_state(self):
        self.state = copy.copy(self.state)

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
    
    @staticmethod
    def four(vec):
        """are there any 4-mer's within the vec that have the same player number? if true, return that players number """
        for player in [1,2]:
            win = any( map(lambda kmer: kmer == 4, [vec[i:i+4].count(player) for i in range(len(vec) - 4)] ) )
            if win:
                return player
        return False
        

    def check_win(self,**kwargs):

        for i in range(self.board.height):
            row = self.state[i][:]        
            player = self.four(row)
            if player:
                print 'WIN at row: ', str(i), ' by player', str(player)
                return player 
        
        for i in range(self.board.height):
            col = self.get_column(i)[:]
            player = self.four(col)        
            if player:
                print 'WIN at col: ', str(i), ' by player', str(player)
                return player

            
        #diagonals bottom-left is left-column "down and to right"-check
        for i in range(self.board.height):
            maxj = min( self.board.width, self.board.height ) - i 
            diag = [self.state[i+j][j] for j in range(0,maxj)]
            if len(diag) >= 4:
                player = self.four(diag)
                if player:
                    print 'WIN at diag ', str(i), ' by player', str(player)
                    #self.extra = True
                    return player
        
        #if kwargs.get('play',0) < 20:
        #    return False
            

        #diagonals bottom-left is bottom-row
        for i in range(self.board.width):
            maxj = min( self.board.width, self.board.height ) - i 
            diag = [self.state[j][i+j] for j in range(0,maxj)]
            if len(diag) >= 4:
                player = self.four(diag)
                if player:
                    print 'WIN at diag ', str(i), ' by player', str(player)
                    self.extra = True
                    return player
        
        #mirror image horizontally "left-to-right" flip, check the diagonals again
        #just reverse each of the rows
        copy_state = copy.deepcopy(self.state)
        mirror_state = []
        for row in copy_state:
            mirror_state.append(copy_state[::-1])


        return False
    
        
        
        
        

        plays = []
        return plays