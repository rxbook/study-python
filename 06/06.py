def test(x,y,z=3,*a,**b):
	print x,y,z
	print a
	print b

test(1,2,3,5,6,7,foo=1,bar=2)
print '------------------'
test(1,2)
