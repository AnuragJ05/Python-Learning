list=[1,2,3,4,5,6,7,8,9,10]
pos=-1
item=int(input("Enter Item"))
for i in range (0,len(list)):
    if(list[i]==item):
        pos=i+1
        break

print(pos)
if(pos>0) :
    print("Item present at position ",pos)
else :
    print("Item is not present in list ")
