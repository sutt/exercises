import subprocess
import os, sys

def pause(dispTxt, breaker):
    while(True):
        #print str(dispTxt)    #for mintty
        #sys.stdout.flush()
        inp = raw_input(dispTxt)
        if any(keywords in inp for keywords in breaker):
            return inp
def print_title_section(txt,**kwargs):
    
    top  = "     ##################################################"
    side = "     #                                                #"
    top_total, top_black = len(top), len(top) - 5

    title = (" " * 5)
    title += "# "
    title += str(txt)
    title += " " * ((len(top) - (5+2)) - len(txt) - 1)
    title += "#"

    s = "\n"
    s += top + "\n"
    s += side + "\n"
    s += title + "\n"
    s += side + "\n"
    s += top + "\n"
    
    return s

def askUser():

    print print_title_section('Welcome to ConnectFour Tutorial')
    print "     developed Will Sutton, 2017 \n     github.com/sutt/exercises/connectfour \n"
    pause('type yes to continue ...', ['yes'])

    print print_title_section('Basic Command: Run a Game')
    print "     Here, both player 1 adn 2 are computer controlled"
    print "     and playing random plays. \n"
    print "     The noisy flag outputs information when a player has won. \n"
    print "running:  $ python cf.py --noisy_gamewin"
    pause('\n[enter] to see run cmd ...', [''])
    print "\n"
    subprocess.call("python cf.py --noisy_gamewin --runs 1")
    pause('\n[enter] for next section ...', [''])

    print print_title_section('Assign Strategy: to the players')
    print "     Instead of playing randomly, computer can use a strategy."
    print "     These are set with strat flag with a tuple for which players"
    print "     can use the strategy, here only player-1 uses strat_me.\n"
    print "running:    $ python cf.py --noisy_gamewin --noisy_strat --strat_me (1,)"
    pause('\n[enter] to see run cmd ...', [''])
    subprocess.call("python cf.py --noisy_gamewin --noisy_strat --strat_me (1,)")
    pause('\n [enter] for more ...', [''])

    print "     There are three strategies, me, you and fork."
    print "     You can see a history of these plays being made. Here, each player"
    print "     has the use of all strategies.\n"
    print "running:    $ python cf.py --runs 2 --noisy_gamewin --noisy_strat --strat_me (1,2) --strat_you (1,2) --strat_fork (1,2)"
    pause('\n[enter] to see run cmd ...', [''])
    subprocess.call("python cf.py --runs 2 --noisy_gamewin --noisy_strat --strat_me (1,2) --strat_you (1,2) --strat_fork (1,2)")
    pause('\n[enter] for next section ...', [''])

    print print_title_section('Logging & Analytics: Batch runs, data schema')

    print print_title_section('Custom Rules: change board, rules')



askUser()



