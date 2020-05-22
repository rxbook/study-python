def test(hobby='222',name='111'):
	print '%s,%s' % (hobby,name)


zidian = {'name':'renxing','hobby':'PHP'}
test(**zidian)
