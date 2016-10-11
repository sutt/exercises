from collections import namedtuple


# z: orientation => 0: stout, 6longx3high ; 1: tall: 3longx6high
#Z-enum:
#Flip-enum:


def tileHolder():
    TH_factory = namedtuple('TileHolder','tile-num full-tile-data flip-side flip-tile-data')
    return TH_factory
    
def playHolder():
    """PlayHolder holds all 6 pieces of information to place a tile on the board"""
    PH_factory = namedtuple('PlayHolder' ,'tilenum tileside x y z flip')
    return PH_factory
