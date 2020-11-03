import math
a=int(input("Enter the 1st Side of Triangle : "))
b=int(input("Enter the 2nd Side of Triangle : "))
c=int(input("Enter the 3rd Side of Triangle : "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of Triangle is :",area)
