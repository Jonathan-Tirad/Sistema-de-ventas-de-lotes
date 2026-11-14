from lotes import *
from clientes import *
from ventas import *
from reportes import *

def main():
    while True:
        print("================ S. G. DE INMOBILIARIA ================")
        print("1. Registrar nuevo lote")
        print("2. Listar todos los lotes")
        print("3. Listar lotes disponibles")
        print("4. Registrar nuevo cliente")
        print("5. Listar clientes")
        print("6. Vender lote")
        print("7. Listar ventas")
        print("8. Generar reporte general de ventas")
        print("9. Salir")
        print("=======================================================")
        
        opcion = input("Seleccione una opción (1-9): ").strip()
        
        if opcion == "1":
            registrarLote()
        elif opcion == "2":
            listar_lotes()
        elif opcion == "3":
            listar_lotes_disponibles()
        elif opcion == "4":
            registrarCliente()
        elif opcion == "5":
            listarClientes()
        elif opcion == "6":
            venderLote()
        elif opcion == "7":
            listarVentas()
        elif opcion == "8":
            generar_reporte_general()
        elif opcion == "9":
            print("\n Saliendo del sistema de ventas. ¡Hasta pronto!\n")
            break
        else:
            print("\n Opción inválida. Por favor, ingrese un número del 1 al 9.\n")


if __name__ == "__main__":
    main()