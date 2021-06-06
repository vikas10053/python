class tatti:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def sum(self):
        s = self.a+self.b
        print(s)
    def sub(self):
        s = self.a-self.b
        print(s)
    def mul(self):
        s = self.a*self.b
        print(s)

z = tatti(10,15)

z.mul()
z.sum()
z.sub()

