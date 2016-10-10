from collections import OrderedDict

N = int(raw_input())

od = OrderedDict()

s = ""
for n in range(N):
    s0 = str(raw_input())
    s1 = s0.split(" ")
    last = len(s1) - 1
    quant = int(s1[last])
    item = " ".join(s1[:last])
    if item in od.keys():
        od[item] += quant
    else:
        od[item] = quant

s = ""
for k in od.iterkeys():
    s += k
    s += " "
    s += str(od[k])
    s += "\n"    

print s




