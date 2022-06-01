for j in range(0,15):
	s = "             "
	for i in range(0,17):
		if j == 6:
			s += " *  *  *  *  I  L  O  V  E  Y  O  U  <3 *  *  *  * "
			break
		if (i+j<2) or (i-j>14 and j<2) or (i-j>5 and j<3 and i+j<11 and i<11) or (j>6 and(j-i>6 or i+j>22)):
			s = s +("   ")
		else:
			s = s +(" * ")
	print(s)
