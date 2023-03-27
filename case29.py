

x = int(input("Please enter no more than 5 bits number:  "))

x = str(x)

def printer(string):

    if len(string) > 1:
        printer(string[1:])
    
    print(string[0],end='')
        
printer(x)