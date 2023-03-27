
perfect_nums=[]


def judge(x,list):
    #sum = 0
    #for i in list:
        #sum+=i
    #if sum == x:
        #return True
    #else:
        #return False
    if sum(list)==x:
        return True
    else:
        return False
        
        

for i in range(2,10001):
    list=[1,]
    for j in range(2,i):
        if i % j == 0:
            list.append(j)
    if judge(i,list):
        perfect_nums.append(i)
        
print(perfect_nums)