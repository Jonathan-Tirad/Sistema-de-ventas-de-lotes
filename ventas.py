from lotes import *
from clientes import *
ventas = []

def listarVentas():
    if not ventas:
        print("Aún no hay ventas registradas.")
    else:    
        for venta in ventas:
            print(venta) 

def venderLote():
    listarClientes()
    cli = input("Seleccionar cliente comprador ejm(CLI-058): ")
    comprador = None

    for cliente in clientes:
        if(cliente['codigo'] == cli):
            comprador = cliente 
            
    listar_lotes_disponibles()
    cod_lote = input("ingresar el codigo del lote a comprar ejm(LT-008): ")
    lotePorComprar = None

    for lote in lotes:
        if(lote['codigo'] == cod_lote):
            lotePorComprar = lote

    print("\n")
    if(lotePorComprar != None and comprador != None):        
        fecha = input("Ingresar fecha de la compra(DD/MM/AA): ")  
    
        venta = {
            "id_venta": f"V-{len(ventas)+1:03d}",
            "fecha": fecha,
            "precio_total": lotePorComprar['precio_total'],
            "cliente": {
                "nombre": comprador['nombre'],
                "dni": comprador['dni'],
                "telefono": comprador['telefono']
                },
            "lote": {
                "codigo": lotePorComprar['codigo'],
                "urbanizacion": lotePorComprar['urbanizacion'],
                "area": lotePorComprar['area']
                }
        } 

        ventas.append(venta)
        comprador['lotes_comprados'].append(lotePorComprar)
        lotePorComprar['estado'] = "vendido"
        print(f"Venta:{venta['id_venta']} realizada con éxito.")
        print()
    else:
        print("El número de cliente o el código de lote no existe.")  
        print("\n")
        venderLote()  


    

    

    