import time, copy

class GameLog:

    ''' Holds all data collected within the game.
        Used as data-structure when returned from a test. '''

    def __init__(self,**kwargs):
        
        #TODO - remove these
        self.board_pre_turn = True
        self.board_pre_turn_oppoenent = kwargs.get('b_log_show_opponent', False)
        self.manual_control = kwargs.get('manual_control', ())
        
        self.b_log_move = kwargs.get('b_log_move', False)
        self.log_move = []
        
        self.b_num_available = kwargs.get('b_num_available',False)
        self.log_num_available = []
        
        self.b_turn_time = kwargs.get('b_turn_time',False)
        self.log_turn_time = []
        self.t0 = time.time()
        

    def add_turn_log(self
                     ,move
                     ,num_available = 0
                     ):
        
        '''each turn append a data element on to each of these logs'''

        if self.b_log_move:
            self.log_move.append(move)
        
        if self.b_num_available:
            self.log_num_available.append(num_available)
        
        if self.b_turn_time:
            _time = time.time() - self.t0
            self.log_turn_time.append(_time)
            self.t0 = time.time()


    def get_log_move(self):
        return copy.deepcopy(self.log_move)

    def get_log_num_available(self):
        return copy.deepcopy(self.log_num_available)

    def get_log_turn_time(self):
        return copy.deepcopy(self.log_turn_time)

    
  
