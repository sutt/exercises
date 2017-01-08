import subprocess

def pause(dispTxt, breaker):
    while(True):
        inp = raw_input(dispTxt)
        if any(keywords in inp for keywords in breaker):
            return inp
    
def askUser():
    """ this sets up motor from class """
    pause('Y to continue ...', ['yes'])
    subprocess.call("python cf.py --runs 2 --noisy_gamewin --noisy_strat --strat_me (1,2) --strat_you (1,2) --strat_fork (1,2)", shell = True)

askUser()



