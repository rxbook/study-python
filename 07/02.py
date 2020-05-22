__metaclass__ = type #确定使用新式类
class Class:
    def method(self):
        print 'I have a self!'

    def function():
        print "I do not ..."

instance = Class()
instance.method()

#下面的运行报错，不知道为啥?
instance.method = function
instance.method()
