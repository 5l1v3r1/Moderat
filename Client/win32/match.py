bevri_sityva = open('3.py', 'r')

listi = bevri_sityva.readlines()

for x in listi:
	if listi.count(x) > 1:
		print x