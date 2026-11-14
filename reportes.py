from ventas import *

def generar_reporte_general():
    if not ventas:
        print("No hay ventas registradas para realizar el reporte.")
        return

    total_ventas = len(ventas)
    ingresos_totales = sum(v["precio_total"] for v in ventas)
    area_total = sum(int(v["lote"]["area"]) for v in ventas)
    print("----------------------------------------------------------------------------------")
    print("                        REPORTE GENERAL DE VENTAS                                 ")
    print(f" Total Ventas Realizadas : {total_ventas}")
    print(f" Ingresos Totales        : S/{ingresos_totales:,.2f}")
    print(f" Área Total Comercializada: {area_total:,.2f} m²")

    print("----------------------------------------------------------------------------------")

    for v in ventas:
        print(f" ID: {v['id_venta']} \n Fecha: {v['fecha']} \n Cliente: {v['cliente']['nombre'][:20]} \n Urbanización: {v['lote']['urbanizacion'][:15]} \n Código Lote: {v['lote']['codigo']} \n Precio Total:  S/{v['precio_total']:,.2f}")

    print("==================================================================================")