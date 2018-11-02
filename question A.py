import matplotlib
from matplotlib import pyplot as plt 
a1 = float(input("please enter first x cordinate line 1: "))
b1 = float(input("please enter first y cordinate line 1: "))
a2 = float(input("please enter 2nd x cordinate line 1: "))
b2 = float(input("please enter 2nd y cordinate line 1: "))
c1 = float(input("please enter first x cordinate line 2: "))
d1 = float(input("please enter first y cordinate line 2: "))
c2 = float(input("please enter 2nd x cordinate line 2: "))
d2 = float(input("please enter 2nd y cordinate line 2: "))

#line x1
e = [a1,a2]
f = [b1,b2]
#line x2
g = [c1,c2]
h = [d1,d2]

plt.plot(e,f)
plt.plot(g,h)

plt.title("line interceptes")
#lable the axis
plt.xlabel("x1, x2")
plt.legend (["this is x1", "this is x2"]) # legend argument as a list
plt.show()

def buildEQ(self,a1,b1,a2,b2,c1,d1,c2,d2,s1,s2,i1,i2):
    #s1 is the slope
    #i1 is the x intercept
    s1 = ((a2-a1)/(b2-1))
    i1 = ((s1*a1)-b1)
    print ("your equation is: " + "y="+ s1 +"x" + i1)
