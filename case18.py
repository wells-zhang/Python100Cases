
a = int(input("Please input the a value: "))

sum = 0

num = int(input("input the num: "))

for i in range(1,num+1):
    x = 0
 
    for j in range(1,i+1):
        s=a*(10**(j-1))
        x += s        
        
    sum+=x
    
print(sum)
    