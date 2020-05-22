class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): #SPAMFilter��Filter������
    def init(self): #��дFilter�����е�init����
        self.blocked = ['SPAM']

#-----------------(��ʼ����)---------------------#
#Filter�Ǹ����ڹ������е�ͨ���࣬��ʵ�������ܹ����κζ���
f = Filter()
f.init()
print f.filter([1,2,3]) #�����[1,2,3]

#Filter����ô���������������������Ļ��ࣨ���ࣩ��
#����SPAMFilter�࣬���Խ������е�"SPAM"���˳�ȥ
s = SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','eggs','bacon','SPAM'])


