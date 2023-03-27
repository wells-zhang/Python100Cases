
def generate(numRows):
    r=[[1]]
    for i in range(1,numRows):
        
        print(r[-1])
        r.append(list(map(lambda x,y:x+y,[0]+r[-1],r[-1]+[0])))
        
    return r[:numRows]
        
a = generate(10)


#for i in a:
#    print(i)

###############################################
#def triangles():

#    L=[1]
#    S=[]
    
#    while True:
        
#        print(L)
#        yield L
#        L=[1] + S + [1]
#        S=[]
#        for i in range(len(L)-1):
#            S.append(L[i] + L[i+1])
                    

###############################################
#def triangles():
#    L=[1]
#    while True:
#        print(L)
#        yield L
#        L=[sum(i) for i in zip([0]+L,L+[0])]
        
        
#g=triangles()
#for i in range(10):
#    next(g)
    
##############################################

        

        


    

    



    

  

    
    
    
    
    
    
    