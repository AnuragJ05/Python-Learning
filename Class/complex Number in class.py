class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real=r
        self.img=i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.img))
c1=ComplexNumber(2,3)
c1.getData()
c2=ComplexNumber(5)
c2.attr=10
print((c2.real,c2.img,c2.attr))
c1.attr=20

