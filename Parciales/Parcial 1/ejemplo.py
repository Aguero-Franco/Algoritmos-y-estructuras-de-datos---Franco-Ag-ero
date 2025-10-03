tipos_entradas = [("general", 8000), ("estudiante", 5000), ("vip", 2000),("jubilado", 3500)]
entradas_vendidas = [("general", 3), ("vip", 2), ("jubilado", 1), ("estudiante", 4)]
def entradas(tipo):
    precio=[]
    cantidad=[]
    total=[]
    recaudo=0
    typo=str(tipo)
    """for prec in range(len(tipos_entradas)):
        precio.append(tipos_entradas[prec][1])
    print(precio)

    for cant in range(len(entradas_vendidas)):
        cantidad.append(entradas_vendidas[cant][1])
    print(cantidad)"""

    for can in range(len(entradas_vendidas)):
        if entradas_vendidas[can][0] == typo:
            for tip in range(len(tipos_entradas)):
                multi=tipos_entradas[tip][1]*entradas_vendidas[can][1]
                if tipos_entradas[tip][0] == typo:
                    total.append(multi)    
                    recaudo+=multi       
    print(total)
    return recaudo


#for index in range(4):
    #entradas(input("Ingrese el tipo de entrada: "))

print(entradas("general"))