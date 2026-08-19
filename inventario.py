from archivos import leer_json, guardar_json

ARCHIVO_INVENTARIO = "inventario.json"


def obtener_inventario():
    return leer_json(ARCHIVO_INVENTARIO)


def guardar_inventario(inventario):
    guardar_json(ARCHIVO_INVENTARIO, inventario)


def buscar_herramienta(inventario, id_herramienta):
    for herramienta in inventario:
        if herramienta["id_herramienta"] == id_herramienta:
            return herramienta
    return None


def mostrar_inventario(inventario):
    print("\n--- INVENTARIO DE HERRAMIENTAS ---")
    if not inventario:
        print("No hay herramientas registradas.")
        return
    for herramienta in inventario:
        print(
            f'ID: {herramienta["id_herramienta"]} | '
            f'Nombre: {herramienta["nombre"]} | '
            f'Estado: {herramienta["estado"]}'
        )
