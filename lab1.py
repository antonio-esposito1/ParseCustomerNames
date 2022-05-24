class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print ('Current valus = "%s"' % self.data)

if __name__ == '__main__':
    x = FirstClass()
    y = FirstClass()
    z = SecondClass()
    z.setdata(42)
    z.display()


