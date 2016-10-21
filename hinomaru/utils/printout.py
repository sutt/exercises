from utils.utils import Solution
from utils.types import playHolder

#tilemark -> sol.tiledot


dletters = {}
letters = list('abcdefghijkl')
for i,v in enumerate(letters):
    dletters[i]=v.capitalize() 


def build_2d_graphic(inp_rows):
    s = ""
    for row in inp_rows:
        s += "".join(str(row))
        s += "\n"
    return s

def lookup_letter(xyt):
    v = filter(lambda v: xyt in v[5],win_v)
    try:
        tilenum = v[0][4]
        return dletters[tilenum]
    except:
        return "?"
    
    
def lookup_mark(xyt):
    vv = filter(lambda v: xyt in v[5],win_v)
    try:
        v = vv[0]
        tside = v[2]
        tdata = v[0][tside]
        
        z,f =  v[3][2], v[1]
        
        x0,y0, = v[3][0], v[3][1]
        x1, y1 = code2xy(xyt)
        x,y = x1 - x0, y1 - y0
        
        return str(tilemark(tdata,x,y,z,f))
    except:
        return "?"

def build_solution_graphic(**kwargs):
    rows_letter,rows_mark = [], []
    for y in range(12):
        row,row2 = "",""
        for x in range(18):
            xyt = x + (y*18)
            row_l += lookup_letter(xyt)
            row_m += lookup_mark(xyt)
        rows_letter.append(row_l)
        rows_mark.append(row_m)
    
    inp_rows = rows_letter if kwargs.get('dots',False) else rows_mark
    return build_2d_graphic(inp_rows)
    