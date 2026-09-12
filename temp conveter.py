# count down in a list
lst=[ ]
n=int(input("Enter the begin countdown number: "))
def count_down(n):
    for i in range(n,0,-1):
        
            lst.append(i)
    return lst

print(count_down(n))
        
        
    


    
    

