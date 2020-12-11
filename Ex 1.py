#1.a
#Calcul du pgcd selon l'algorithme d'Euclide :
#Pour chaque itération, on effectue "a mod b"
#Si le résultat est différent de 0, "a" prend la valeur "b" et "b" la valeur "a mod b"
#Si le résultat est égal à 0, on retourne la valeur de "b" correspondant au pgcd(a,b)

def my_gcd(a,b): 
        
    while(a%b != 0) : 
        a, b = b, a%b 
        
    return b

#1.b
#Calcul de l’inverse du modulo N de a selon l'algorithme d’Euclide étendu:
#Utilisation de l'identité de Bézout avec ab + Nc = PGCD(a, N)
#Initialisation avec une matrice identité pour les valeurs de b,b1,c,c1
#Retourne un entier b tel que a*b ≡ 1 mod N ssi pgcd(a,N) = 1

def my_inverse(a,N):
    
    b,b1 = 1,0
    c,c1 = 0,1

    while N!=0:
        
        temp_quotient, temp_reste = a//N, a%N 
        
        a, N = N, temp_reste
        b, b1 = b1, (b - temp_quotient*b1)
        c, c1 = c1, (c - temp_quotient*c1)
        
    #a => pgcd(a,N)
    #b => a*b ≡ pgcd(a,N) mod N
    #c => N*c ≡ pgcd(a,N) mod a
    
    if a!=1:
        raise ValueError("a n’est pas inversible modulo N!")
    else:
        return b

#1.c
#Détermination expérimentalement de la complexité des fonctions
#Utilisation de la fonction time() pour le calcul et de matplotlib pour l'affichage du graphe
#les valeurs testées sont les puissances de 89 et 97 (2 nombres premiers) pour s'assurer que le pgcd soit égale à 1

import time
import matplotlib.pyplot as plt

complexity1 = []
complexity2 = []

for i in range (1,3000):
    start1=time.time()
    temp1 = my_gcd(89**i,97**i)
    complexity1.append(time.time()-start1)
    
    start2=time.time()
    temp2 = my_inverse(89**i,97**i)
    complexity2.append(time.time()-start2)
    
plt.plot(complexity1,label="my_gcd()")
plt.plot(complexity2,label="my_inverse()")
plt.legend()
plt.show()

#1.d
#Utilisation du pseudocode donné dans l'exercice avec "a_i" correspondant à "n & (2**i)"

def my_expo_mod(g,n,N):
    
    l = n.bit_length()
    h = 1
    
    for i in range(l,-1,-1):
        h = (h*h)%N

        if((n & (2**i)) == 2**i):
            h = (h*g)%N
            
    return h
