
ini = [3,7]
maxchanges = 15
bad = [61,60]
maxnodes = 40000
iprune = 11

def p2c(pos):
	''' x,y -> across then down ordering '''
	return (pos[1]-1)*8 + pos[0]

def c2p(code):
	#print code
	return [  8 if ((code % 8)==0) else code % 8 ,((code-1) / 8) + 1]
	
start = [0,0,ini,[p2c(ini)]]
ss = [start] 
	
def travel(d,guy):
	dlast, changes, pos1,hist = guy[0],guy[1], guy[2], guy[3]
	dir = [[1,0],[-1,0],[0,1],[0,-1]][d-1]
	changes = changes + 1 if d <> dlast else changes
	if changes > maxchanges: return False
	pos2 = [dir[0] + pos1[0], dir[1] + pos1[1]]
	if (max(pos2) > 8) or (min(pos2) < 1): return False
	if sum(map(lambda p: p2c(p) in bad,[pos1, pos2]))== 2:return False
	if p2c(pos2) in hist:  return False
	lst = hist[:]
	lst.extend([p2c(pos2)])
	return [d,changes,pos2, lst]

def maze(hist):
		'''input: hist (list): code of path points taken, in order '''
		vec = "  00  " * 8
		vecb = "      " * 8
		vecc = vec+"\n"+vecb+"\n"
		mat = vecc*8
		
		h0 = hist[0]
		for h in hist:
			x,y = c2p(h)[0], c2p(h)[1]
			spot = (x-1)*6 + (y-1)*(((6*8)+1)*2)
			repl = "0" + str(h) if h < 10 else str(h)
			mat = mat[:spot+2] + repl +  mat[spot + 4:]
			
			if h != h0:
			
				x0,y0 = c2p(h0)[0], c2p(h0)[1]
				repl2 = "--" if y == y0 else "||"
				
				if y == y0:
					spot2 = spot - ((x-x0)*3)
				else:
					spot2 = spot -  (y-y0)*((6*8)+1)
				
				mat = mat[:spot2+2] + repl2 +  mat[spot2 + 4:]
				
				h0 = h
				
		return mat

if __name__ == "__main__":		

	for i in range(63):
		
		ss = [travel(x,y) for x in range(1,5) for y in ss]
		orig = len(ss)
		
		ss = filter(lambda x: x != False, ss)
		orig2 = len(ss)
		
		sf = " "
		if i > iprune:
			
			#prune by desired progress
			#mmax = float(15) / float(64)
			#mmax = (i + 10) * mmax
			#ss = filter(lambda x: x[1] <  mmax, ss)
			
			#prune by top X, least dirchanges made
			if orig2 > maxnodes:
				ss.sort(key=lambda k: k[1])
				ss = ss[:maxnodes]
				sf += "-> "
				sf += str(len(ss))
		
		print i, ": ", orig, " -> ", orig2, sf

	#Print out an example solution
	solution = ss[0]
	print solution 
	solution = solution[3]
	eachtown = map(lambda q: 1 if q in solution else 0, range(1,65))
	print "unique towns visited: ", sum(eachtown)
	print "\n PATH: \n"
	print maze(solution)




