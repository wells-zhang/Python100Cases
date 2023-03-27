import datetime

text = list(input("Please input......"))

dict = {}

while text != "\n":
    for i in text:
        for j in dict.keys():
            if i == j:
                dict[j]+=1
                print('ENGKAND')
                #break
        else:
            dict[i]=1
            print('USA')
            
    else:
        break
        
print(dict)
                
    