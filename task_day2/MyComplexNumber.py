class MyComplexNumber:
    def __init__(self,real=0,imag=0):
        print("My complex number are executing...")
        self.real_part=real
        self.imag_part=imag
    def displayComplex(self):
        print("{0}+{1}j".format(self.real_part,self.imag_part))
cmpx1=MyComplexNumber(40,80)
cmpx1.displayComplex()
cmpx2=MyComplexNumber(60,70)
cmpx2.new_attribute=80
cmpx2.displayComplex()