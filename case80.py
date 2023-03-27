

def Peach_division(x):

    if (x - 1) % 5 == 0:
        
        return True
        
    else:
    
        return False
        
    
if __name__ == '__main__':

    for n in range(5,5000):
    
        flag = 0
        
        x = n
        while Peach_division(x):
                            
            x = (x-1) // 5
            flag += 1
            
            if flag == 6:
                
                print(n)
                break
    
    
    
    


        

    

    
    
    





            


    

    

    



    

  

    
    
    
    
    
    
    