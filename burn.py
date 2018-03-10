count =1
x = 1

while count < 1000:
    x+=2
    for k in range(2,x):
        if x%k == 0:
            break

    else:
        count +=1
    

print(x)
            
