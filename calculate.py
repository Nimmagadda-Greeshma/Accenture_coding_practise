def Calculate( m, n):
    sum_of_divisible=0
    for i in range(m,n+1):
        if(i%3==0 and i%5==0):
            sum_of_divisible = sum_of_divisible+i
    print(sum_of_divisible)
        
solve=Calculate(12,50)
solve
    
