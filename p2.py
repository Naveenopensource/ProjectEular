c=[]
d=[]
a, b = 0, 1
#fibonacii series
while b < 4000000:
	c.append(b)
	a, b = b, a+b
#even series
for i in range(0,len(c)):
	if c[i]%2==0:
		d.append(c[i])
#sum
print(sum(d))
