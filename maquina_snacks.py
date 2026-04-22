print('*** maquina de snacks***')

snacks =    [   
                {
                    'id':0,
                    'Nombre':'papas',
                    'precio':3000
                },
                
                {
                    'id':1,
                    'Nombre':'refresco',
                    'precio':5000
                },
                
                {
                    'id':2,
                    'Nombre':'sandwich',
                    'precio':12000
                }
            ]
#lista de productos 

productos = []

print('***maquina de snacks***')
print('snacks disponibles')

for snack in snacks:
    print(  
            f"\tID: {snack['id']}", 
            f"->{snack['Nombre']}",
            f"->{snack['precio']}"
        )
    
def maquina_snacks(snacks,productos):
    salir = False
    while not salir:
        print(f'''menu:
              1. comprar snack
              2. mostrar ticked
              3. salir''')
        opcion = int(input('escoje una opcion'))

        if opcion == 1:
            Comprar_producto(snacks,productos)
        elif opcion == 2:
            mostrar_ticked(productos)
        elif opcion == 3:
            print('reresa pronto')
            salir = True
        else:
            print('opcion invalida , selecciona otro')      

def Comprar_producto(snacks,productos):
    id_snack = int(input('pulsa el id del snack'))
    productos.append(snacks[id_snack])

def mostrar_ticked(productos):
    ticket = f'\t*** ticket de venta'
    total = 0
    for producto in productos:
        ticket += f"\n\t - {producto['Nombre']} - {producto['precio']}"
        total += producto['precio']
    ticket += f'\n\t TOTAL -> ${total}'    
    print(ticket)


#llamamoso invocamos la funcion 

maquina_snacks(snacks,productos)