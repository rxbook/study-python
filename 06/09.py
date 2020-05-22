#encoding:utf-8
def test_a(**k):
	print k['name'],'----',k['age']

def test_b(k):
	print k['name'],'----',k['age']

args = {'name':'renxing','age':26}

test_a(**args)
test_b(args)
