print("Hello User")
def add(num1, num2):
     return num1+num2
def subtract(num1,num2):        
     return num1-num2
def multiply(num1,num2):
    return num1*num2  
def divide(num1,num2):
    return num1/num2
print("select operation-\n"
"1.Add\n"
 "2.Subtract\n"
"3.Multiply\n"
"4.Divide")
chose =int(input("select operation from 1,2,3,4:"))
a=float(input("enter first number: "))
b=float(input("enter second number:"))
if chose==1:
   print(a,'+',b,'=',add(a,b))
elif chose ==2:
 print(a,'-',b,'=',subtract(a,b))
elif chose==3:
  print(a,'*',b,'=', multiply(a,b))
elif chose==4:
      if b!=0:
          print(a,"/",b,'=', divide(a,b))
      else:
        print("Denominator can't be zero")
else:
  print("select correct input from 1,2,3,4")
