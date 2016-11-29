import os, sys
import json

if False:
    f = open('data/output1.txt','r')
    ds = f.read()
    f.close()
    dd = eval(ds)
    jsonout = {'runs':dd}

loaded = json.load(open('data/output2.txt','r'))

#aster)
#$ python cf.py --analytics --readfile output1.txt --stat win_player --pct_analytics 1


def new_output(all_files):
    i = 1
    f_prefix = "output"
    while True:
        fn = f_prefix + str(i) + ".txt"
        if fn in all_files:
            i += 1
        else:
            return fn

datadir = os.path.join( os.getcwd(), 'data')
all_files = os.listdir(datadir)
fn = new_output(all_files)
fnpath = os.path.join( os.getcwd(), 'data', fn )

f = open(fnpath,'w')

data = ['1','2','3']
data = "\n".join(data)

d = {}
d['a'] = 1
d['b'] = {'aa':'str'}
d['c'] = 'string'

json.dump(jsonout,f)
#f.writelines(str(d))

f.close
print 'done'

'c:\\Users\\William\\Desktop\\files\\exercises\\exercises\\connectfour\\data'
'c:\\Users\\William\\Desktop\\files\\exercises\\exercises\\connectfour\\data\\file1.txt'