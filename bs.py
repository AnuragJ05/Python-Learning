list=[1,2,3,4,5,6,7,8,9,10]
pos=-1
item=int(input("Enter Item"))
f=0
l=len(list)

while f<=l :
    m=int((f+l)/2)
    if(list[m]==item):
        pos=m+1
        break
    elif (list[m]<item):
        f=m+1
    else :
        l=m

print(pos)
if(pos>0) :
    print("Item present at position ",pos)
else :
    print("Item is not present in list ")
