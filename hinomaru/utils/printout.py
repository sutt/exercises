from utils import Solution
from types import playHolder, playplusHolder

#tilemark -> sol.tiledot


dletters = {}
letters = list('abcdefghijkl')
for i,v in enumerate(letters):
    dletters[i]=v.capitalize() 

    
#valid2: (tile, flip,tileside,xyz,indt, (xyt's))

def lookup_letter(_xyt, mywin):

    _playplus = filter(lambda pp: _xyt in pp.xyt, mywin)

    if len(_playplus) != 1:
        return "?"
    _playplus = _playplus[0]
    
    try:
        tilenum = _playplus.play.tilenum
        return dletters[tilenum]
    except:
        return "?"
    
    
def lookup_mark(_xyt, mywin, sol):
    
    _playplus = filter(lambda pp: _xyt in pp.xyt, mywin)
    
    if len(_playplus) != 1:
        return "?"
    _playplus = _playplus[0]
    
    try:
        
        tside = _playplus.play.tileside
        tdata = _playplus.data[tside]
        
        x0,y0 = _playplus.play.x, _playplus.play.y
        x1, y1 = sol.code2xy(_xyt)
        x,y = x1 - x0, y1 - y0
        
        return str(sol.get_tile_dot(tdata, _playplus.play, x, y))
        #return str(sol.get_tile_dot(tdata, _playplus.play, 0, 0))
    except:
        return "?"

def build_2d_graphic(inp_rows):
    s = ""
    for row in inp_rows:
        s += "".join(str(row))
        s += "\n"
    return s
        
def build_solution_graphic(mywin, sol, **kwargs):
    
    rows_letter,rows_mark = [], []
    for y in range(12):
        row_l,row_m = "",""
        for x in range(18):
            xyt = x + (y*18)
            row_l += lookup_letter(xyt, mywin)
            row_m += lookup_mark(xyt, mywin, sol)
        rows_letter.append(row_l)
        rows_mark.append(row_m)
    
    inp_rows = rows_mark if kwargs.get('dots',False) else rows_letter
    
    return build_2d_graphic(inp_rows)
    