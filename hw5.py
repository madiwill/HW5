import re
filename = ("regex_sum_38503.txt")
x = open(filename, 'r')
numbers = []
for a in x.readlines():
	num = re.findall('[0-9]+', a)
	numbers.append(num)
z=0
for y in numbers:
	if len(y)>=1:
		for c in y:
			z += int(c)
print (z)



