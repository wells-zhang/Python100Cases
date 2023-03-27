

list = [1,11,22,33,44,55]

print(round(len(list)/2))
for i in range(round(len(list)/2)):

    list[i],list[len(list)-i-1]=list[len(list)-i-1],list[i]
    
print(list)
        


    

  

    
    
    
    
    
    
    