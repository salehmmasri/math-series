def fibonacci(num):
    if num==0:
        return 0
    else :    
        numtest=0
        numtest1=1
        list_fibonacci=[numtest,numtest1]
        for i in range(num-1):
           list_fibonacci.append( list_fibonacci[i]+list_fibonacci[i+1])
        return list_fibonacci[len(list_fibonacci)-1]
# print(fibonacci(10)) 


def lucas(num2):
    if num2==0:
        return 2
    elif num2 == 1:
        return 1  
    else:     
        numtestt=2
        numtest11=1
        list_fibonacci2=[numtestt,numtest11]
        
        for i in range(num2-1):
            list_fibonacci2.append( list_fibonacci2[i]+list_fibonacci2[i+1])
        return list_fibonacci2[len(list_fibonacci2)-1]

# print(lucas(10))

def sum_series(n1, n2=0,n3=1):
    if n2==0 and n3 == 1:
        return fibonacci(n1)
    elif     n2==2 and n3 == 1:
        return lucas(n1)
    else:
        return lucas(n1)+ fibonacci(n2)     

print(sum_series(9))