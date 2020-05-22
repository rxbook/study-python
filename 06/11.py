#encoding:utf-8
####先用传统的循环实现：
def jisuan(n):
	result = n
	for i in range(1,n):
		result *= i
	return result

print jisuan(5) # 5*4*3*2*1
print jisuan(4) # 4*3*2*1
print jisuan(1) # 1

#----------------------------------
###用递归实现阶乘：
def jiecheng(n):
	if n == 1:
		return 1
	else:
		return n * jiecheng(n-1)

print jiecheng(5)
print jiecheng(4)
print jiecheng(1)
