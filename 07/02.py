__metaclass__ = type #ȷ��ʹ����ʽ��
class Class:
    def method(self):
        print 'I have a self!'

    def function():
        print "I do not ..."

instance = Class()
instance.method()

#��������б�����֪��Ϊɶ?
instance.method = function
instance.method()
