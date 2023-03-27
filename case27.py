

i = 1
list=[]
while i <= 5:

    list.append(input("Please input %d:  " %i))
    i+=1

def printer(y,list):

    if y > 0:
        print(list[y])
        printer((y-1),list)
    else:
        print(list[y])
    

printer(4,list)

    
    
    
    


        
        

    
 


    
