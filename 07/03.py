class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): #SPAMFilter是Filter的子类
    def init(self): #重写Filter超类中的init方法
        self.blocked = ['SPAM']

#-----------------(开始调用)---------------------#
#Filter是个用于过滤序列的通用类，事实上它不能过滤任何东西
f = Filter()
f.init()
print f.filter([1,2,3]) #输出：[1,2,3]

#Filter类的用处在于它可以用作其他类的基类（超类），
#比如SPAMFilter类，可以将序列中的"SPAM"过滤出去
s = SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','eggs','bacon','SPAM'])


