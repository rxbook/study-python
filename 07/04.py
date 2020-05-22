class Calc:
    def calc(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print 'Hello,',self.value

class TalkingCalc(Calc,Talker):
    pass

#--------µ÷ÓÃ-------------
tc = TalkingCalc()
tc.calc('1+2*3')
tc.talk()
