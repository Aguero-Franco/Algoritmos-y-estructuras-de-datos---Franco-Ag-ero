#Escribe una programa en Python que calcule la suma de los números 
#enteros positivos de la serie n+(n-2)+(n-4) mientras n-x =< 0, usando recursión. (10)=30
def suma(n):
    if n==0:
        return 0 
    else:
        return n+suma(n-2)
    
print("la suma de es:",suma(6))
print("la suma de es:",suma(10))