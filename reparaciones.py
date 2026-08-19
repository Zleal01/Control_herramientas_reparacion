from datetime import datetime
from archivos import leer_json, guardar_json
from inventario import obtener_inventario, guardar_inventario, buscar_herramienta, mostrar_inventario

ARCHIVO_REPARACIONES = "reports/reparaciones.json"


def registrar_reparacion():
    inventario = obtener_inventario()
    reparaciones = leer_json(ARCHIVO_REPARACIONES)
    mostrar_inventario(inventario)
    try:
        id_herramienta = int(input("\nIngrese el ID de la herramienta: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        return
    herramienta = buscar_herramienta(inventario, id_herramienta)
    if herramienta is None:
        print("La herramienta no existe en el inventario.")
        return
    if not {"id_herramienta", "nombre", "estado"}.issubset(herramienta):
        print("La herramienta no tiene todos los datos necesarios.")
        return
    if herramienta["estado"] == "En reparación":
        print("La herramienta ya está en reparación.")
        return
    inicio = input("Fecha de inicio (AAAA-MM-DD): ")
    final = input("Fecha estimada de finalización (AAAA-MM-DD): ")
    observaciones = input("Observaciones: ")
    try:
        fecha_inicio = datetime.strptime(inicio, "%Y-%m-%d").date()
        fecha_final = datetime.strptime(final, "%Y-%m-%d").date()
    except ValueError:
        print("La fecha debe tener formato AAAA-MM-DD.")
        return
    if fecha_final < fecha_inicio:
        print("La fecha final no puede ser anterior a la fecha de inicio.")
        return
    reparaciones.append({
        "id_herramienta": herramienta["id_herramienta"],
        "nombre": herramienta["nombre"],
        "fecha_inicio_reparacion": inicio,
        "fecha_estimada_finalizacion": final,
        "observaciones": observaciones,
        "estado": "En reparación"
    })
    herramienta["estado"] = "En reparación"
    guardar_json(ARCHIVO_REPARACIONES, reparaciones)
    guardar_inventario(inventario)
    print("Reparación registrada correctamente.")


def listar_reparaciones():
    reparaciones = leer_json(ARCHIVO_REPARACIONES)
    activas = [r for r in reparaciones if r.get("estado") == "En reparación"]
    print("\n--- HERRAMIENTAS EN REPARACIÓN ---")
    if not activas:
        print("No hay herramientas en reparación.")
        return
    for reparacion in activas:
        print(f'\nID: {reparacion["id_herramienta"]}')
        print(f'Nombre: {reparacion["nombre"]}')
        print(f'Inicio: {reparacion["fecha_inicio_reparacion"]}')
        print(f'Finalización estimada: {reparacion["fecha_estimada_finalizacion"]}')
        print(f'Observaciones: {reparacion["observaciones"]}')


def actualizar_reparaciones_finalizadas():
    inventario = obtener_inventario()
    reparaciones = leer_json(ARCHIVO_REPARACIONES)
    hoy = datetime.now().date()
    cambios = False
    for reparacion in reparaciones:
        if reparacion.get("estado") != "En reparación":
            continue
        try:
            final = datetime.strptime(reparacion["fecha_estimada_finalizacion"], "%Y-%m-%d").date()
        except (ValueError, KeyError):
            continue
        if hoy >= final:
            herramienta = buscar_herramienta(inventario, reparacion["id_herramienta"])
            if herramienta is not None:
                herramienta["estado"] = "Activa"
                reparacion["estado"] = "Finalizada"
                cambios = True
    if cambios:
        guardar_inventario(inventario)
        guardar_json(ARCHIVO_REPARACIONES, reparaciones)
