
#Ejercicio 1
def fun(precios,compras):
    pdiccionario=dict(precios)
    total=0
    for producto,cantidad in compras:
        if producto in pdiccionario:
            total+=pdiccionario[producto]*cantidad
        else:
            print(f"El producto'{producto}' no está en la lista de precios")
    return total
precios=[('manzana', 4), ('pan', 4)]
compras=[('manzana', 4), ('pan', 4)]
compra_total=fun(precios,compras)
print(f"El total de la compra es: {compra_total}")