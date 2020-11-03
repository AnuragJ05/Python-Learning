# While Loop

i=1
while i<=5:
    print(i)
    i+=1
    
# while loop with break condition
i=1
while i<=5:
    print(i)
    i+=1
    if i==3:
        break
    
# while loop with Continue condition
i=1
while True:
    print(i)
    i+=2
    if i%5!=0:
        continue
    else:
        break