bevri_sityva = open('3.py', 'r')

listi = bevri_sityva.readlines()

sul = len(listi)
count = 0
persent = 0


for x in listi:
	count += 1
	if count == 5000 or count == 10000 or count == 50000 or count == 100000 or count == 200000 or count == 300000:
		print count
	if listi.count(x) > 1:
		print x