#!/usr/bin/python
def math_func(count):
	current_val = 1
	N = 0
	
	for x in range(max(count,0)):
		
		
		spaces = ((8 - len(current_val))/2)
		for y in range (0, spaces):
			print " ",
		for z in range (0, (x + 1) ):
			print(current_val[z]),
		current_val = [l+r for l,r in zip(current_val + N, N + current_val)]
		#spaces = ((80-len(current_val))/2)

math_func(17)
