

numerator = [2,3,]
denominator = [1,2,]

sum = 0

for i in range(2,21):
    numerator.append(numerator[i-2]+numerator[i-1])
    denominator.append(denominator[i-2]+denominator[i-1])
    
for i in range(1,21):
    sum+=numerator[i]/denominator[i]
    
    
print(sum)
    
