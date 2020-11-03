#Python collection
#there are four type
# list, touple, set and dictionary

# list -order,change duplicacy allowed
# set - unorder, unindex, no duplicate
# dictionary - key or value
# touples -oreder, duplicacy,unchangable

#List-

shopping=["milk","bread","jam"]
print(shopping)

number=[1,2,3,4,5,6]
print(number)

#accessing the list
print(number[0])
print(number[2])

#change the item value
shopping[1]="Toast"
print(shopping)

#loop through a list
for i in shopping:
    print(i)

#length of list
print(len(shopping))

#add item in a list
shopping.append("milk")
print(shopping)
shopping.insert(1,"water")
print(shopping)

#remove items

shopping.remove("milk")
print(shopping)
number.remove(1)
print(number)
number.remove(number[1])
print(number)

del(number[1])
print(number)

#pop method-remove the specified index
shopping.pop(0)
print(shopping)

#clear method
shopping.clear
print(shopping)

#list constructor
num=list((1,2,3,4,5))
print(num)

#check if any item exist
print("bread" in shopping)
