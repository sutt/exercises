import xlwings as xw
import json
import yaml
import sys, os

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
    wb = xw.Book()  # this will create a new workbook
    #wb = xw.Book('FileName.xlsx')  # connect to an existing file in the current working directory
    #wb = xw.Book(r'C:\users\william\desktop\')  # on Windows: use raw strings to escape backslashes
    sht = wb.sheets['Sheet1']
    return sht
    

rows = all_files(95,96)
sht = xl()
down,across = len(rows), len(rows[0])
for i in range(down):
    for j in range(across):
        sht[i,j].value = rows[i][j] 