import random

def puzzle(valids,strikeouts,**kwargs):
    
    layout = []
    struckout = []
    log = []
    TOTAL_PLACES = 12
    #note: valids arent neccessary for this func, only strikeout
    allv = range(len(valids))  
    ivalids = [(i,v) for i,v in enumerate(valids)]
    Log = kwargs.get('Log',False)
    
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
            struckout.append(strikeouts[r])
            if Log: log.append([(try_i, "_APP:", len(layout), layout[:])])

    return log