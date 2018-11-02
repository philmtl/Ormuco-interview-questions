#Question B
#The goal of this question is to write a software 
#library that accepts 2 version string as input and 
#returns whether one is greater than, equal, or less than the other. 
#As an example: “1.2” is greater than “1.1”. Please provide all 
#test cases you could think of.


a = float(input("please enter a decimal number: "))
b = float(input("please enter a 2nd decimal number: "))
                
if a > b:
    print ('a is greater than b')
elif a == b:
    print ('a is equal to b')
elif a < b: 
    print ('a is less than b')
else:
    print('invalid oporator')
          
