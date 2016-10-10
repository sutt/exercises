#http://puzzles.bostonpython.com/hinomaru.html
import os, sys, random, time, math

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

SOLUTION = [
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0),
    (0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0),
    (0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0),
    (0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0),
    (0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0),
    (0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0),
    (0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0),
    (0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0),
    (0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0),
    (0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
]

TILES = [
    (
        ((1,1,1,1,1,1), (1,1,1,1,1,1), (1,1,1,1,1,1)),
        ((0,1,1,1,1,1), (0,1,1,1,1,1), (0,0,1,1,1,1)),
    ),
    (
        ((1,1,1,1,1,1), (1,1,1,1,1,1), (1,1,1,1,1,1)),
        ((1,1,0,0,0,0), (1,1,0,0,0,0), (1,0,0,0,0,0)),
    ),
    (
        ((1,1,1,1,1,1), (1,1,1,1,1,1), (1,1,1,1,1,1)),
        ((0,0,0,0,0,0), (1,1,0,0,0,0), (1,1,1,1,0,0)),
    ),
    (
        ((1,1,1,1,1,1), (0,1,1,1,1,0), (0,0,0,0,0,0)),
        ((1,1,1,1,0,0), (1,1,0,0,0,0), (0,0,0,0,0,0)),
    ),
    (
        ((1,1,1,1,1,1), (0,1,1,1,1,0), (0,0,0,0,0,0)),
        ((0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0)),
    ),
    (
        ((1,1,1,1,1,0), (1,1,1,1,1,0), (1,1,1,1,0,0)),
        ((0,0,0,0,0,0), (0,0,0,0,0,0), (1,0,0,0,0,0)),
    ),
    (
        ((1,1,1,1,0,0), (1,1,1,1,1,0), (1,1,1,1,1,0)),
        ((0,0,1,1,1,1), (0,0,0,0,1,1), (0,0,0,0,0,0)),
    ),
    (
        ((0,0,0,0,0,0), (0,0,0,0,1,1), (0,0,1,1,1,1)),
        ((0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0)),
    ),
    (
        ((0,0,1,1,1,1), (0,0,0,0,1,1), (0,0,0,0,0,0)),
        ((0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,1)),
    ),
    (
        ((0,0,0,0,1,1), (0,0,0,0,1,1), (0,0,0,0,0,1)),
        ((0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0)),
    ),
    (
        ((0,0,0,0,0,1), (0,0,0,0,1,1), (0,0,0,0,1,1)),
        ((0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,1)),
    ),
    (
        ((0,0,0,0,0,1), (0,0,0,0,0,0), (0,0,0,0,0,0)),
        ((0,0,0,0,0,0), (0,0,0,0,0,0), (0,0,0,0,0,0)),
    ),
]

t, s = TILES, SOLUTION

print recurse_dims(t), recurse_dims(s)
_TILES, _SIDES,_TYVECS, _TXDOTS = recurse_dims(t)
_SYVECS, _SXDOTS = recurse_dims(s)

#-------------------------------

def mod(dims,solution):
    return filter(lambda p: any( map(lambda dim: (p) % (dim) == 0,dims) ), \
                  range(0,solution) )




modx = mod((_TXDOTS,_TYVECS),_SXDOTS)
mody = mod((_TXDOTS,_TYVECS),_SYVECS)
print modx, mody



# z: orientation => 0: stout, 6longx3high ; 1: tall: 3longx6high
modxy = [(x,y) for x in modx for y in mody]
modxyz = [(a[0],a[1],b) for a in modxy for b in range(2)]
print modxyz[:4]
print len(modxyz)

combos = [(tile, flip,tileside,xyz,indt) for flip in range(2) for tileside in range(2) for xyz in modxyz for indt,tile in enumerate(t)]
print len(combos)


def tilemark(tx,xx,yy,zz,ff):
    #if flip = -1 -> y can be bigger than x
    flip = -1 if ff else 1
    tt = [x[::flip] for x in tx[::flip]]
    if not(zz):
        out = tt[yy][xx]
    else:    
        out = tt[2-xx][yy]
    return out

def matchtile(tile,flip,xyz):
    x,y,z = xyz[0], xyz[1], xyz[2]
    r0, r1 = range(3), range(6)
    xiter, yiter = (r0,r1) if z else (r1,r0)
    try:
        out = all( [s[y+ y0][x + x0] == tilemark(tile,x0,y0,z,flip) for x0 in xiter for y0 in yiter])
        return out
    except:
        return False #error occurs because some shapes are bigger than smallest mod
        
#valid: if matchtile returns true, tile t, with params p matches to solution mat
valid = filter(lambda i: matchtile(i[0][i[2]],i[1],i[3]), combos)   #THE BUG! this flips
print len(valid)

#valid2: (tile, flip,tileside,xyz,indt, (xyt's))
def v2xy(v):
    x,y,z = v[3][0], v[3][1], v[3][2]
    _xr, _yr = (_TYVECS, _TXDOTS) if z else (_TXDOTS, _TYVECS)
    xy = [(xx + x, yy + y) for xx in range(_xr) for yy in range(_yr)]
    return xy

def xy2code(xy):
    x,y = xy[0],xy[1]
    return (y*_SXDOTS)+x   #numbering across, then down

def xyt(info_obj):
    return tuple(map(xy2code,v2xy(info_obj)))

print valid[0][3]   
print xyt(valid[0])    

valid2 = map(lambda v: ( v[0], v[1], v[2], v[3],v[4], xyt(v) ) ,valid)
print valid2[0]


# each v in valid will strike out a portion of other v's
# -> so we can update strikeout vec as union of preproc's stikeouts

def strikeout(x):    
    valid3 = [(i,v) for i,v in enumerate(valid2)]
    tile_i, xy_list = valid2[x][4], valid2[x][5] 

    out1 = filter(lambda v: v[1][4] == tile_i ,valid3)
    ind1 = map(lambda v: v[0] ,out1)

    out2 = filter(lambda v:any(map(lambda xyt: xyt in xy_list ,v[1][5]) ),valid3)
    ind2 = map(lambda v: v[0] ,out2)
    
    return list( set.union(set(ind1), set(ind2) ) )

so = [[] for i in range(len(valid2))]
for i in range(len(valid2)) :
    so[i].extend(strikeout(i))
    
print so[:5]
outs = map(len,so)
print '----'
print outs
print '----'
print max(outs),min(outs)

def puzzle(**kwargs):
    layout = []
    struckout = []
    allv = range(len(valid2))
    log = []
    valid3 = [(i,v) for i,v in enumerate(valid2)]
    Log = kwargs.get('Log',False)
    
    for try_i in range(kwargs.get('tries',20)):

        if len(layout) == 12: 
            print 'SUCCESS:', layout
            print 'IN TRIES:', try_i
            if Log:
                return (layout,log)
            else:
                return (layout,try_i)

        if len(struckout) > 0:
            notavail = reduce(lambda x,y: x+y, struckout)
        else:
            notavail = ()
        available = [x for x in allv if x not in notavail]

        #Prune Condition: Not enough valid plays to complete puzzle.
        if len(available) < (12 - len(layout)):
            
            back = random.randint(1,len(layout))
            if kwargs.get('allback',False): back = len(layout)
            if Log: log.append([(try_i, "_BACK:", back)])
                           
            for b in range(back):
                lp = layout.pop()
                sp = struckout.pop()
                if Log: log.append([(try_i, "POP:", lp)])
                
        else:
            
            #Extend layout list with a play from available list
            r = random.sample(available,1)[0]
            layout.append(r)
            struckout.append(so[r])
            if Log: log.append([(try_i, "_APP:", len(layout), layout[:])])

    return log

ret = puzzle(tries = 20, Log=True)

ret2 = reduce( lambda x,y: str(x) + "\n" + str(y), ret)
print ret2


#ret = puzzle(tries = 100000, Log=False)

wins = []
for trial in range(2):
    wins.append(puzzle(tries=100000,Log = False))   
print wins    

win1 = wins[0][0]
win_v = [valid2[w] for w in win1]

letters = 'abcdefghijkl'
letters = list(letters)
dletters = {}
for i,v in enumerate(letters):
    dletters[i]=v.capitalize() 
print dletters


def build_puzzle_letter(inp_rows):
    s = ""
    for row in inp_rows:
        s += "".join(row)
        s += "\n"
    return s

def build_puzzle_mark(inp_rows):
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
    
def code2xy(xyt):
    y = int(xyt / 18)
    x =  xyt % 18
    return (x,y)

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
        #return str(x)
        #return str(1)
        return str(tilemark(tdata,x,y,z,f))
    except:
        return "?"

rows,rows2 = [], []
for y in range(12):
    row,row2 = "",""
    for x in range(18):
        xyt = x + (y*18)
        row += lookup_letter(xyt)
        row2 += lookup_mark(xyt)
    rows.append(row)
    rows2.append(row2)
    
out = build_puzzle_letter(rows)
print out

out = build_puzzle_mark(rows2)
print out

