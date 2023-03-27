
x_data=[]
n = 1
while n <= 4:

    number = int(input('enter your number: '))
    x_data.append(number)    
    n+=1


x_data[0],x_data[3]=x_data[3],x_data[0]
x_data[1],x_data[2]=x_data[2],x_data[1]


for i in range(0,4):

    if x_data[i] >= 5:
        x_data[i]=x_data[i]-5
    elif x_data[i] < 5:
        x_data[i]=x_data[i]+5
        
        
print(x_data)




 


        

    

    
    
    





            


    

    

    



    

  

    
    
    
    
    
    
    