import random

def puzzle(strikeouts,**kwargs):
    
    layout = []
    struckout = []
    log = []
    
    TOTAL_PLACES = 12
    allv = range(len(strikeouts))  
    Log = kwargs.get('Log',False)
    
    #note: valids arent neccessary for this func, only strikeout
    #ivalids = [(i,v) for i,v in enumerate(valids)]
    
    ini_layout = kwargs.get('ini_layout',[])
    if len(ini_layout) > 0:
        layout = ini_layout[:]
        struckout = map(lambda i: strikeouts[i], layout)
    
    MIN_UNDO_LAYOUT = 0
    if kwargs.get('dont_undo_ini_layout', True):
        MIN_UNDO_LAYOUT = len(ini_layout)
        
        
    
    for try_i in range(kwargs.get('tries',20)):

        if len(layout) == TOTAL_PLACES: 
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
        if len(available) < (TOTAL_PLACES - len(layout)):
            
            back_potential = len(layout) - MIN_UNDO_LAYOUT
            back = random.randint(1,back_potential)
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
            struckout.append(strikeouts[r])
            if Log: log.append([(try_i, "_APP:", len(layout), layout[:])])

    return log