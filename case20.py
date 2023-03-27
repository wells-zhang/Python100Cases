
x = 100 
for i in range(11):
    height =(x/(2**i))
    
    if i > 0:
        print("{}th time latitude of the sphere bounce: {}".format(i,height))