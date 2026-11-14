lotes = [
    {
        "codigo": "LT-001" ,
        "urbanizacion": "Los Jardines",
        "area" : "120",
        "precio_por_m" : 450,
        "precio_total": 54000,
        "estado" : "Disponible"
},
{
        "codigo": "LT-002" ,
        "urbanizacion": "Las Palmeras",
        "area" : "90",
        "precio_por_m" : 500,
        "precio_total": 45000,
        "estado": "Disponible"
}

]

def registrarLote():
    registrado = False

    while(registrado == False):
        print("==========REGISTRO DE LOTE==================")
        codigo = f"LT-{len(lotes)+1:03d}"
        urbanizacion = input("Ingresar urbanización: ")
        area = int(input("Ingresar el área en metros cuadrados: "))
        precio_por_m = float(input("Ingresar precio por metro cuadrado: "))
        precio_total = area * precio_por_m
        estado = "Disponble"

        lote = {"codigo": codigo ,
                "urbanizacion": urbanizacion,
                "area" : str(area),
                "precio_por_m" : precio_por_m,
                "precio_total": precio_total,
                "estado" : estado
        }

        if(urbanizacion != '' and area > 0 and precio_por_m > 0.0 and precio_por_m):
            print("-" * 40)
            print(f"Código: {lote['codigo']}")
            print(f"Urbanización: {lote['urbanizacion']}")
            print(f"Área: {lote['area']} m²")  
            print(f"Precio por m²: s/ {lote['precio_por_m']:,.2f}")  
            print(f"Precio Total: s/ {lote['precio_total']:,.2f}")
            print(f"Estado: {lote['estado']}")
            print("---------------------Lote agregado exitosamente---------------------!!!")
            lotes.append(lote)
            registrado = True
            
        else:
            print("ERROR: todos los campos deben ser llenados y los precios y area deben ser mayor a 0.") 
            registrarLote()   

def listar_lotes():
        print("=" * 25)
        print("Lista total de lotes")
        print("=" * 25 )
        print()
        for lote in lotes:
           print(f"Código: {lote['codigo']}")
           print(f"Urbanización: {lote['urbanizacion']}")
           print(f"Área: {lote['area']} m²")  
           print(f"Precio por m²: s/ {lote['precio_por_m']:,.2f}")  
           print(f"Precio Total: s/ {lote['precio_total']:,.2f}")
           print(f"Estado: {lote['estado']}")
           print("=" * 25)
           print()
            
def listar_lotes_disponibles():
        print("=" * 25)
        print("LIsta de lotes disponibles")
        print("=" * 25)
        print()
        for lote in lotes:
            if(lote["estado"] == "Disponible"):
                print(f"Código: {lote['codigo']}")
                print(f"Urbanización: {lote['urbanizacion']}")
                print(f"Área: {lote['area']} m²")  
                print(f"Precio por m²: s/ {lote['precio_por_m']:,.2f}")  
                print(f"Precio Total: s/ {lote['precio_total']:,.2f}")
                print(f"Estado: {lote['estado']}")
                print("=" *25)
                print()
     
                  
                  
                     
    



