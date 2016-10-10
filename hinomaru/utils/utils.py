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