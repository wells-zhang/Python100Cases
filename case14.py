z = int(input("Pls enter your number: "))

def Prime_number(y):

    for i in range(2,y):
        if y % i == 0:
            return False
            #break
    else:
        return True
        
        
def get_factor(num,list):
    
    x = num
    factors=list
    

    #print(x)
    for k in range(2,x+1):
                       
        if x == k:
                
            factors.append(x)
            #print(k,end='\n')
            #print(x,k,'Flag')
            break
                
        else:
            
            if x % k == 0 & Prime_number(k):
                
                #print(k,end=' ')
                factors.append(k)
                x = x // k
                #print(x)
                get_factor(x,factors)
                break
                
    print('test')
    return factors        

result = get_factor(z,list=[1,])
print(result)

       
       
            
            
            
    
    