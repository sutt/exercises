
class Board:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def print_board(self,**kwargs):
        
        _blank, _X, _O = "~", "X", "O"
        chars = [_blank,_X,_O]

        lines = [ list(_blank * self.width) for _ in range(self.height)]
        
        state = kwargs.get('board_state',[])
        if len(state) != 0:
            lines = []
            for row in range(len(state)-1,-1,-1):
                line = [chars[spot] for spot in state[row]]  
                lines.append(line)
        
        out = ""
        if kwargs.get('board_header',False):
            out += " ".join([str(i) for i in range(self.width)]) 
            out += "\n"
        for line in lines:
            out += " ".join(line) + "\n"
        print out