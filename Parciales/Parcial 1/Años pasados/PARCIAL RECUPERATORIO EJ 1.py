#La serie geométrica es una suma de la forma a + a *r + a*r2 + a*r3 + ... + a*r(n-1).
#Implementar en Python una función recursiva para calcular la suma de una serie geométrica
#, donde a es el primer término, r es la razón común, y n es el número de términos.
#Por ejemplo, para los siguentes valores
#a = 2, r = 3 y n = 4
#suma_geométrica(2,3,4) debe ser igual a 80.

def serie_geometrica(a,r,n):
    if n==0:
        return 0
    else:
        return a*r**(n-1)+serie_geometrica(a,r,n-1)

print("la suma de la serie geometrica es:",serie_geometrica(2,3,4))
    