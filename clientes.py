clientes = [
    {
        "codigo" : "CL-001",
        "nombre": "Carlos Alberto Pérez Gómez",
        "dni": "72345678",
        "telefono": "987654321",
        "lotes_comprados": []
    },
    {
        "codigo" : "CLI-002",
        "nombre": "Ana María Rodríguez Silva",
        "dni": "48123456",
        "telefono": " 912345678",
        "lotes_comprados": []
    },
    {
        "codigo" : "CLI-003",
        "nombre": "Luis Fernando Quispe Mendoza",
        "dni": "10456789",
        "telefono": "998877665",
        "lotes_comprados": []
    }
]

def registrarCliente():
    registrado = False

    while(registrado == False):
        print("==========REGISTRO DE CLIENTE==================")
        nombre = input("Ingresar Nombre del Cliente: ").strip().title()
        dni = input("Ingresar Número de DNI: ")
        telefono = input("Ingresar Número Télefonico: ")
        print("-" * 50)

        cliente = {
                "codigo" : f"CLI-{len(clientes)+1:03d}",
                "nombre": nombre,
                "dni": dni,
                "telefono" : telefono,
                "lotes_comprados":[] 
        }

        if(nombre != '' and dni != ''  and telefono != ''):
           print(f"Código: {cliente['codigo']}")
           print(f"Nombre: {cliente['nombre']}")
           print(f"DNI: {cliente['dni']}")
           print(f"Télefono: {cliente['telefono']}")
           print("--------------Cliente agregado con éxito--------------!!!")
           clientes.append(cliente)
           registrado = True
          
        else:
            print("ERROR: todos los campos deben ser llenados correctamente.") 
            registrarCliente() 

def listarClientes():
    print("=====LISTA DE CLIENTES=====")
    print()
    for cliente in clientes:
        print(f"Código: {cliente['codigo']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"DNI: {cliente['dni']}")
        print(f"Télefono: {cliente['telefono']}")
        
        if(len(cliente["lotes_comprados"]) > 0):
            print(f"Lotes Comprados: ")   
            for lote in cliente["lotes_comprados"]:
                print()
                print(" " * 18 + f"Código: {lote['codigo']}")
                print(" " * 18 + f"Urbanización: {lote['urbanizacion']}")
                print(" " * 18 + f"Área: {lote['area']} m²")  
                print(" " * 18 + f"Precio por m²: s/ {lote['precio_por_m']:,.2f}")  
                print(" " * 18 + f"Precio Total: s/ {lote['precio_total']:,.2f}")
                print("=" * 25)
                print()
        else:
            print(f"Lotes Comprados: Ninguno")

        print("-" *30)   
