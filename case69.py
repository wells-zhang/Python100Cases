
n = int(input("Pls enter the total number of people: "))
queue=[]

for i in range(1,n+1):
    queue.append(i)

counter = 0    
while len(queue) > 1:
    
    for i in queue:
        
        counter+=1
        print(queue)
        print(counter,i)
        if counter == 3:
            if i == queue[-1]:
                queue.remove(i)
                counter=0
            else:
                queue.remove(i)
                counter=1
                
                   
print(queue)
        
        
    
    
    





            


    

    

    



    

  

    
    
    
    
    
    
    