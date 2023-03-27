list=[82,9,35,47,66,28,53]

max = 0
min = 0
tempt1=list[0]
tempt2=list[0]

for i in range(len(list)):
    
    for j in range(i,len(list)):
        if tempt1 < list[j]:
            tempt1 = list[j]
            max = j
        elif tempt2 > list[j]:
            tempt2 = list[j]
            min = j

list[0],list[max]=list[max],list[0]
list[-1],list[min]=list[min],list[-1]

print(list)



            


    

    

    



    

  

    
    
    
    
    
    
    