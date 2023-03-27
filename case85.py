

x = input('Enter your odd_number: ')


def number_generator(k):

    sum = 0
    for i in range(1,k+1):
        sum += 9*(10**(i-1))
        
    return sum
        
        

    
for i in range(int(len(x)),1000):
    #print(number_generator(i))
    if number_generator(i) % int(x) == 0:
        print(number_generator(i))
        break
    
    
    
    


        

    

    
    
    





            


    

    

    



    

  

    
    
    
    
    
    
    