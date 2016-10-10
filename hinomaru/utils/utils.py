def recurse_dims(obj):
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
    
def mod(dims,solution):
    return filter(lambda p: \
            any( map(lambda dim: (p) % (dim) == 0, dims) ), \
            range(0,solution) )


def tilemark(tx,xx,yy,zz,ff):
    #if flip = -1 -> y can be bigger than x
    flip = -1 if ff else 1
    tt = [x[::flip] for x in tx[::flip]]
    if not(zz):
        out = tt[yy][xx]
    else:    
        out = tt[2-xx][yy]
    return out

def matchtile(tile,flip,xyz,s):
    x,y,z = xyz[0], xyz[1], xyz[2]
    r0, r1 = range(3), range(6)
    xiter, yiter = (r0,r1) if z else (r1,r0)
    try:
        out = all( [s[y+ y0][x + x0] == tilemark(tile,x0,y0,z,flip) for x0 in xiter for y0 in yiter])
        return out
    except:
        return False #error occurs because some shapes are bigger than smallest mod
        
#valid2: (tile, flip,tileside,xyz,indt, (xyt's))
def v2xy(v,_Y,_X):
    x,y,z = v[3][0], v[3][1], v[3][2]
    _xr, _yr = (_Y, _X) if z else (_X, _Y)
    xy = [(xx + x, yy + y) for xx in range(_xr) for yy in range(_yr)]
    return xy

def xy2code(xy):
    x,y = xy[0],xy[1]
    return (y*_SXDOTS)+x   #numbering across, then down

def xyt(info_obj):
    return tuple(map(xy2code,v2xy(info_obj)))
    
    
def strikeout(x):    
    valid3 = [(i,v) for i,v in enumerate(valid2)]
    tile_i, xy_list = valid2[x][4], valid2[x][5] 

    out1 = filter(lambda v: v[1][4] == tile_i ,valid3)
    ind1 = map(lambda v: v[0] ,out1)

    out2 = filter(lambda v:any(map(lambda xyt: xyt in xy_list ,v[1][5]) ),valid3)
    ind2 = map(lambda v: v[0] ,out2)
    
    return list( set.union(set(ind1), set(ind2) ) )