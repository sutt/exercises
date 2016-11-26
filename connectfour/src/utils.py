import time,os,sys,random,copy

game = {}
game['game_i'] = None
game['t0'] = None
game['t1'] = None
game['t'] = None
game['count_turn'] = None
game['win_bool'] = None
game['win_turns'] = None
game['win_type'] = None
game['player_win'] = None


class Log:
    
    


    def __init__(self, noisy = False, **kwargs):
        
        self.game = copy.copy(game)

        self.games = []

        self.noisy = noisy
        self.record = False
        self.persist = False

    
    def reset_game(self):
        pass

    def game_start(self, game_i = None, noisy = False ):
        
        self.game = copy.copy(game)    #reset
        
        self.game['count_turn'] = 0

        self.game['t0'] =  time.time()
        
        self.game['game_i'] = game_i 
        
        if noisy or self.noisy:
            print "GAME: ", str(game_i)


    def print_board(self, state):
    
        _blank, _X, _O = "~", "X", "O"
        chars = [_blank,_X,_O]

        lines = []
        for irow in range(len(state)-1,-1,-1):
            line = [chars[spot] for spot in state[irow]]  
            lines.append(line)
        
        out = ""
        for line in lines:
            out += " ".join(line) + "\n"
        print out


    def game_tie(self, noisy = False):
        
        self.game['win_bool']
        if noisy or self.noisy:
            print 'Game Ends in Draw at turn: ', str(self.game.get('count_turn','TURN_UNKNOWN'))

    def game_play(self, noisy = False):

        self.game['count_turn'] += 1

    def game_win(self, win_state = None, noisy = False):

        if noisy or self.noisy:
            print 'WINNING at turn:', str(self.game.get('count_turn', 'TURN_UNKNOWN'))
            if win_state is not None:
                self.print_board(win_state)

    def game_end(self,noisy = False):
        
        self.game['t1'] = time.time()
        
        if self.game['t0'] is not None:
            self.game['t'] = self.game['t1'] - self.game['t0']

        if self.record:
            self.games.append(game)

        if noisy or self.noisy:
            pass        
            
    def end_runs(self):
        print 'ENDING -----'
        if self.persist:
            #writes games to file as json
            pass


    
class Board:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    #""" Deprecated stuff: -------------------------"""
    def print_board(self,**kwargs):
        
        _blank, _X, _O = "~", "X", "O"
        chars = [_blank,_X,_O]

        lines = [ list(_blank * self.width) for _ in range(self.height)]
        
        state = kwargs.get('state',[])
        if len(state) != 0:
            lines = []
            for irow in range(len(state)-1,-1,-1):
                line = [chars[spot] for spot in state[irow]]  
                lines.append(line)
        
        out = ""
        if kwargs.get('board_header',False):
            out += " ".join([str(i) for i in range(self.width)]) 
            out += "\n"
        for line in lines:
            out += " ".join(line) + "\n"
        print out