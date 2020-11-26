def my_gcd(a,b): 
    
    temp1, temp2 = a,b
    
    while(temp1%temp2 != 0) : 
        temp1, temp2 = temp2, temp1%temp2 
    
    return temp2

def my_inverse(a,N):
    
    u,u1 = 1,0
    v,v1 = 0,1

    while N!=0:
        
        temp_quotient, temp_reste = a//N, a%N 
        
        a, N = N, temp_reste
        u, u1 = u1, (u - temp_quotient*u1)
        v, v1 = v1, (v - temp_quotient*v1)
        
    return (a,u,v) # a = pgcd(a,N)

def my_expo_mod(g,n,N):
    l = len(n)
    h = 1
    
    for j in range(l):
        i = l - 1 - j
        h = (h**2)%N
        if(a[i] == 1):
            h = h*(g%N)
    
    return h