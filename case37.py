

list=[]
for i in range(10):
    list.append(int(input("Pls enter the %i number: " %(i+1))))
    
for j in range(len(list),1,-1):
    #print(j)
    for k in range(0,j-1):
        if list[k] > list[k+1]:
            list[k],list[k+1] = list[k+1],list[k]
            
#print(list)

print(sorted(list))
    

  

    
    
    
    
    
    
    