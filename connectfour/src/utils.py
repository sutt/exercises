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
game['win_player'] = None
game['strat_found'] = None


class Log:


    def __init__(self, noisy = False, **kwargs):
        
        self.game = copy.copy(game)

        self.games = []

        self.noisy = noisy
        self.record = True
        self.persist = True


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

    def persist_to_file(self,data,**kwargs):

        def new_output(all_files):
            i = 1
            f_prefix = "output"
            while True:
                fn = f_prefix + str(i) + ".txt"
                if fn in all_files:
                    i += 1
                else:
                    return fn

        datadir = os.path.join( os.getcwd(), 'data')
        all_files = os.listdir(datadir)
        fn = new_output(all_files)
        fnpath = os.path.join( os.getcwd(), 'data', fn )

        f = open(fnpath,'w')
        f.writelines(str(data))
        f.close()

        if kwargs.get('noisy',False):
            print 'Saving to data/', str(fn)

    def load_from_file(self,filename,**kwargs):

        datadir = os.path.join( os.getcwd(), 'data')
        all_files = os.listdir(datadir)
        fnpath = os.path.join('data', filename)
        f = open(fnpath,'r')
        inp_str = f.read()
        f.close()
        data = eval(inp_str)

        return data

    def get_stat(self,data,stat):

        ret = []
        for elem in data:
            ret.append(elem.get(stat))
        
        return ret

    def game_tie(self, noisy = False):
        
        self.game['win_bool'] = False
        if noisy or self.noisy:
            print 'Game Ends in Draw at turn: ', str(self.game.get('count_turn','TURN_UNKNOWN'))
    
    def strat_played(self, ret_strat,current_play, noisy=False):
        
        if ret_strat > -1:
                
            self.game['strat_found'] =  {'turn': self.game.get('count_turn', None)
                                         ,'player': copy.copy(current_play.player)
                                         ,'stratcol': ret_strat }
            
            if noisy:
                print 'STRAT! turn ', str(self.game.get('count_turn', "unknown")), \
                      ' col ',str(ret_strat) , \
                      ' player ', str(copy.copy(current_play.player))
        


    def game_play(self, noisy = False):

        self.game['count_turn'] += 1


    def game_win(self, player = None, win_type = None, win_type_ind = None, noisy = False):

        self.game['win_player'] = player
        self.game['win_type'] = win_type
        self.game['win_type_ind'] = win_type_ind 
        self.game['win_bool'] = True
        self.game['win_turns'] = self.game['count_turn']

        if noisy or self.noisy:
            
            s_win_type = 'unknown' if win_type is None else str(win_type)
            s_win_type_ind = 'unknown' if win_type_ind is None else str(win_type_ind)
            s_player = str(player)

            print 'ConnectFour at ', s_win_type, ' ', s_win_type_ind, ' by Player ', s_player


    def game_win_print(self, win_state = None, noisy = False):

        if noisy or self.noisy:

            print 'WINNING at turn:', str(self.game.get('count_turn', 'TURN_UNKNOWN'))
            
            if win_state is not None:
                self.print_board(win_state)

    def game_end(self,noisy = False):
        
        self.game['t1'] = time.time()
        
        if self.game['t0'] is not None:
            self.game['t'] = self.game['t1'] - self.game['t0']

        if self.record:
            self.games.append(self.game)

        if noisy or self.noisy:
            pass        
            
    def end_runs(self):
        print 'ENDING -----'
        if self.persist:
            #writes games to file as json
            self.persist_to_file(data = self.games, noisy = True)
            


    
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