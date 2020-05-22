#encoding:utf-8

def story(**kwds):
	return 'This is a story:' \
		'%(job)s --- %(name)s' % kwds

def power(x,y,*others):
	if others:
		print 'Good student:',others
	return pow(x,y)

def interval(start,stop=None,step=1):
	'Imitates range() for step > 0'
	if stop is None: #如果没有为stop提供值
		start,stop = 0,start #指定参数
	result = []
	i = start #计算start索引
	while i < stop: #直到计算到stop索引
		result.append(i) #将索引添加到result内
		i+=step #用step(>0)增加索引i
	return result

#---------------------------------------------
print story(job='king',name='renxing')

print story(name='Green',job='teacher')

params = {'job':'language','name':'Python'}
print story(**params)

del params['job']
print story(job='hahahaha',**params)

power(2,3)

power(3,2)

power(y=3,x=2)

params = (5,)*2
power(*params)

power(3,3,'Hello_world')

interval(10)

interval(1,5)

interval(3,12,4)

power(*interval(3,7))
