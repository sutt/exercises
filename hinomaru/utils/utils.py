from types import tileHolder, playHolder
play = playHolder()

def recurse_dims(obj):
    """Takes [nested] list, Return list of length-of-list at each recursive level of input-list. Must be non-jagged in that each level has same length for each member."""
    
    try:
        next = obj[:]
    except:
        return []
    dims = []
    for i in range(1000):
        try:
            if len(next) > 0:
                dims.append(len(next))
            else:
                break
        except:
            break            
        next = next[0]
    return dims
    
def mod(tile_dims,solution_dim):
    return filter(lambda p: \
            any( map(lambda dim: (p) % (dim) == 0, tile_dims) ), \
            range(0,solution_dim) )

            

        
class Solution:
    
    """functions which use data from solution"""

    def __init__(self,**kwargs):
        self.s = kwargs.get('s',[])
        self._Y = kwargs.get('_Y',0)
        self._X = kwargs.get('_X',0)
        
    def get_tile_dot(self,tdata,p,xx,yy):
        """xx, yy: relative to top-left corner of tile"""
        
        f = -1 if p.flip else 1
        tdata_f = [x[::f] for x in tdata[::f]]
        
        if not(p.z):
            out = tdata_f[yy][xx]
        else:    
            out = tdata_f[2-xx][yy]
        return out
        
    def match_tile_to_board(self,tiles,p):
        """returns Boolean of whether each tile-dot matches the corresponding spot on the solution"""
        
        x0,y0 = p.x, p.y
        tdata = tiles[p.tilenum][p.tileside]
        
        r0, r1 = range(3), range(6)
        xiter, yiter = (r0,r1) if p.z else (r1,r0)
        
        try:
            matches = [self.s[y0 + _y][x0 + _x] == self.get_tile_dot(tdata,p,_x,_y) for _x in xiter for _y in yiter] 
            return all(matches)
        except:
            return False #error: a portion of tile is off the board
        
        
    def v2xy(self,p):
        x,y,z = p.x,p.y,p.z
        _xr, _yr = (3, 6) if z else (6, 3)
        xy = [(xx + x, yy + y) for xx in range(_xr) for yy in range(_yr)]
        return xy

    def xy2code(self,xy):
        x,y=xy[0],xy[1]
        return (y*self._X)+x   #numbering across, then down

    def xyt(self,play_i):
        return tuple(map(self.xy2code,self.v2xy(play_i)))

class SearchData:

    def __init__(self):
        self.x = []         
    
def strikeout(i,play_i,valids,valids_misc):    
    # each v in valid will strike out a portion of other v's
    # -> so we can update strikeout vec as union of preproc's stikeouts
    ivalids = ((i,v) for i,v in enumerate(valids))
    tile_i  = play_i.tilenum 
    out1 = filter(lambda p: p[1].tilenum == tile_i ,ivalids)
    ind1 = map(lambda v: v[0] ,out1)
    
    ixyt = ((i,v) for i,v in enumerate(valids_misc))
    xylist_i = valids_misc[i]
    out2 = filter(lambda v:any(map(lambda xyt: xyt in xylist_i ,v[1]) ),ixyt)
    ind2 = map(lambda v: v[0] ,out2)
    
    return list( set.union(set(ind1), set(ind2) ) )