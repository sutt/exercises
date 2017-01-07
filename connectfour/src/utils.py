import time,os,sys,random,copy,json

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



class Log:


    def __init__(self, noisy = False, **kwargs):

        #list of each game in a batch-loop        
        self.games = []
        self.strats = []
        self.moves = []

        self.game = copy.copy(game)
        self.strat = None
        self.move = []

        #settings
        self.noisy = noisy
        self.record = True
        self.persist = True
        
        self.record_strategy = True
        self.record_plays = True


    def game_start(self, game_i = None, noisy = False ):
        
        self.game = copy.copy(game)    #reset
        self.strat = None
        self.move = []
        
        self.game['count_turn'] = 0

        self.game['t0'] =  time.time()
        
        self.game['game_i'] = game_i 
        
        if noisy or self.noisy:
            print "GAME: ", str(game_i)

    def batch_board_params(self, inp_board):
        self.batch_board = {}
        self.batch_board["board_width"] = inp_board.width
        self.batch_board["board_height"] = inp_board.height

    def batch_strat_params(self, obj_strat):
        """  record strat used params """
        self.batch_strat = {}
        self.batch_strat['connect_three_me'] = obj_strat.connect_three_me
        self.batch_strat['connect_three_you'] = obj_strat.connect_three_you
        self.batch_strat['fork_me'] = obj_strat.fork_me

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

        if False:   #old way
            out_data = str(data)
        
        out_dict = {'batch':data}
        out_data = json.dumps(out_dict)

        f = open(fnpath,'w')
        f.writelines(out_data)
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
    
    def strat_played(self, ret, current_play, noisy=False, just_strats = True):        
                
        _turn = self.game.get('count_turn', -1) + 1      # +1 b/c its called before make_play
        _player = copy.copy(current_play.player)
        _col =  ret[0]
        _type = ret[1]
        
        if self.record_strategy:

            self.strat =  {'turn': _turn 
                            ,'player': _player 
                            ,'stratcol': _col
                            ,'type': _type } 
            
        if noisy:            
            
            if not(just_strats) or (_type is not None):   #dont print non-strategy moves, "Random"s
            
                sTurn =  str(_turn)
                sStrat = 'Random' if ret[1] is None else ('Strat-' + ret[1] )
                sCol = '' if ret[1] is None else str(ret[0])
                sPlayer = str(_player)

                print 'player ' , sPlayer, ' t', sTurn, ' ', sStrat, ' at col ', sCol


    def game_play(self, playcol, play, noisy = False):

        self.game['count_turn'] += 1
        
        if self.record_plays:
            this_play = (copy.copy(play.player), playcol)
            self.move.append(this_play)


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
            self.strats.append(self.strat)
            self.moves.append(self.move)

        if noisy or self.noisy:
            pass        
            
    def end_runs(self):
        print 'ENDING -----'
        if self.persist:
            #writes games to file as 
            #was previously sent as pure str(data) -> out, eval(str) -> in
            data = {'strategy':self.batch_strat,
                    'board': self.batch_board,
                    'games':self.games}
            self.persist_to_file(data = data, noisy = True)
            


    
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