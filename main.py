from inventario import obtener_inventario, mostrar_inventario
from reparaciones import registrar_reparacion, listar_reparaciones, actualizar_reparaciones_finalizadas


def ejecutar_programa():
    actualizar_reparaciones_finalizadas()
    while True:
        print("\n===== CONTROL DE HERRAMIENTAS =====")
        print("1. Registrar reparación")
        print("2. Listar reparaciones")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_reparacion()
        elif opcion == "2":
            actualizar_reparaciones_finalizadas()
            listar_reparaciones()
        elif opcion == "3":
            mostrar_inventario(obtener_inventario())
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    ejecutar_programa()
