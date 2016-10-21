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

def printerHolder():
    """not used right now"""
    type_factory = namedtuple('PrinterHolder' ,'tilenum tdata x y z flip')
    return type_factory
    
def playplusHolder():
    """playplus holds play as the basic info with augmented info about that play. <data> is both sides so it must be indexed by play.tileside to give tdata"""
    type_factory = namedtuple('PlayplusHolder' ,'play xyt data')
    return type_factory