

def factorial(x):
    result=1
    for i in range(1,x+1):
        result*=i
        
    return result
    
sum = 0    

for i in range(1,21):
    sum += factorial(i)
    
    
print(sum)
    
