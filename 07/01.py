__metaclass__ = type #ȷ��ʹ����ʽ��

class Person:

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, %s" % self.name

#����
foo = Person()
foo.setName('renxing')
foo.greet()

bar = Person()
bar.setName('zhangsan')
bar.greet()


