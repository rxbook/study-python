#ʹ��list���췽��������ʽ�ؽ�������ת��Ϊ�б�
class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


