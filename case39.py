

list = [1,11,22,33,44,55,66,77,88,99]

x = int(input('pls enter the new num: '))

for i in range(len(list)):
    if x <= list[i]:
        list.insert(i,x)
        break
else:
        list.append(x)
        
print(list)
    


    

  

    
    
    
    
    
    
    