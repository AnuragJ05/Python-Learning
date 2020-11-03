#For Loop with list
number =[1,2,3]
for i in number:
    print(i)

#For Loop with string
for i in "ACROPOLIAN":
    print(i)
    
#For loop with break statement
items=["Table","Chair","Duster","Pen","Pencil"]
for i in items:
    print(i)
    if i=="Duster":
        break
    
#For loop with Continue statement
items=["Table","Chair","Duster","Pen","Pencil"]
for i in items:
    if i!="Duster":
        print(i)
        continue
    
#For Loop in range
for i in range(4):
    print(i)
for i in range(1,3):
    print(i)
for i in range(1,10,3):
    print(i)    
    
