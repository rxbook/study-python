#coding:utf-8
#反序列打印命令行参数
import sys
args = sys.argv[1:]
args.reverse()
print ' '.join(args)

#另一种做法：
#print ' '.join(reversed(sys.argv[1:]))


