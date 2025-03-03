def gcd(x , y) :
    if x >= y :
        dividend = x
        divisor = y
    else :
        dividend = y
        divisor = x
    
    r = dividend % divisor
    if r == 0:
        gcd = divisor
    else :
        while r != 0 :
            dividend = divisor
            divisor = r
            r = dividend % divisor
            gcd = divisor
    
    return gcd

print(gcd(18 , 12))



    
    
