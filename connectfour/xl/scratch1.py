import json
import yaml
import sys, os
import argparse


game = {}
game['game_i'] = None
game['t0'] = None
game['t1'] = None
game['t'] = None
game['count_turn'] = None
game['win_bool'] = None
game['win_turns'] = None
game['win_type'] = None
game['win_player'] = None


ap = argparse.ArgumentParser()
ap.add_argument("--excel", action="store_true", default=False)
ap.add_argument("--csv", action="store_true", default=False)
ap.add_argument("--dont_sum_strats", action="store_true", default=False)  #will leave a comma in your csv
ap.add_argument("--from_to", default = (1,1))   #which files from /data/outputN.json 
args = vars(ap.parse_args())


def load_file(path):
    
    f = open(path,'r')
    txt = f.read()
    f.close()
    #data_json = json.loads(txt)
    data_json = yaml.load(txt)
    return data_json

def find_replace_chars(input, find, replace):
    
    find_ind = [i for i,v in enumerate(input) if v == find]
    replaced = [replace if i in find_ind else v for i,v in enumerate(input) ]
    output = ''.join(replaced)
    return output

def all_files(low,high,**kwargs):
    
    game_col_names = game.keys()   # ['win_turns',  'game_i', 'win_player']
    games_list = []

    #Iter over all output files
    for n in range(low,high+1):
        print n        
        path_n = "../data/output" + str(n) + ".txt"
        data = load_file(path_n)
        
        #schema of log
        games = data["batch"]["games"]
        strat = data["batch"]["strategy"]

        
        #strat, same for whole batch
        strat_col_names = ['connect_three_me', 'connect_three_you', 'fork_me']
        strat_vals = [str(strat.get(k,"BAD")) for k in strat_col_names]
        if not(args["dont_sum_strats"]):
            # [1,2] -> <1|2>  ; [0,0] -> <|>  ; [2] -> <2>
            strat_vals = map(lambda x: find_replace_chars(x,",","|"), strat_vals)
            strat_vals = map(lambda x: find_replace_chars(x," ",""), strat_vals)
            strat_vals = map(lambda x: find_replace_chars(x,"0",""), strat_vals)
            strat_vals = map(lambda x: find_replace_chars(x,"[","<"), strat_vals)
            strat_vals = map(lambda x: find_replace_chars(x,"]",">"), strat_vals)
            

        #game, separate games within a batch
        for _game in games:
            game_list = []
            for k in game_col_names: 
                v = _game.get(k,"BAD")
                game_list.append(v)
            game_list.extend(strat_vals)
            games_list.append(game_list)

    #All output files together
    game_col_names.extend(strat_col_names)
    col_names = game_col_names
    table = [col_names]
    table.extend(games_list)
    
    return table
        

def xl():
    import xlwings as xw
    #wb = xw.Book()  # this will create a new workbook
    wb = xw.Book('scratch1.xlsx')  # connect to an existing file in the current working directory
    sht = wb.sheets['Sheet2']
    return sht


def new_output(all_files):
    
    i = 1
    f_prefix = "output"
    while True:
        fn = f_prefix + str(i) + ".csv"
        if fn in all_files:
            i += 1
        else:
            return fn


def output_name(**kwargs):
    
    datadir = os.path.join( os.getcwd(), 'data')
    all_files = os.listdir(datadir)
    fn = new_output(all_files)
    fnpath = os.path.join( os.getcwd(), 'data', fn )
    return fnpath


def make_csv(input_data):
    """ input_data: nested list 
        returns : list of stings, collapsed into csv """
    s_data = [map(str, row) for row in input_data]
    s2_data = [ reduce(lambda x,y: x + "," + str(y), row) for row in s_data]
    return "\n".join(s2_data)
    



def main():

    from_to_string = args["from_to"]
    from_to = eval(from_to_string)
    if len(from_to) != 2: print 'from_to is not correct'

    rows = all_files(from_to[0],from_to[1])

    down, across = len(rows), len(rows[0])   #note: previous steps should have assured all across are same length

    if args["csv"]:
        
        out_data = make_csv(rows)
        fnpath = output_name()
        print 'outputting to: ' , fnpath

        f = open(fnpath,'w')
        f.writelines(out_data)
        f.close()

    if args["excel"]:
        
        sht = xl()
        for i in range(down):
            for j in range(across):
                sht[i,j].value = rows[i][j] 

main()












