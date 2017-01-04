import xlwings as xw
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
args = vars(ap.parse_args())


def load_file(path):
    
    f = open(path,'r')
    txt = f.read()
    f.close()
    #data_json = json.loads(txt)
    data_json = yaml.load(txt)
    return data_json

def all_files(low,high,**kwargs):
    
    col_names = game.keys()   # ['win_turns',  'game_i', 'win_player']
    games_list = []

    for n in range(low,high+1):
        print n        
        path_n = "../data/output" + str(n) + ".txt"
        data = load_file(path_n)
        
        games = data["outcome"]
        for _game in games:
            game_list = []
            for k in col_names: 
                v = _game.get(k,"BAD")
                game_list.append(v)
            games_list.append(game_list)

        rows = [col_names]
        rows.extend(games_list)
    
    return rows
        

def xl():
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

    rows = all_files(9,9)

    down, across = len(rows), len(rows[0])

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












