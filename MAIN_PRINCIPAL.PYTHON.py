from granja import Granja
from corral import Corral
from empleado_sanidad import EmpleadoSanidad
from empleado_limpieza import EmpleadoLimpieza
from empleado_alimentacion import EmpleadoAlimentacion
from administrador import Administrador
from vaca import Vaca
from cerdo import Cerdo
from gallina import Gallina
from alimento import Alimento 

import datetime
asistencias = {}
registros_sanitarios = {}
def mostrar_menu():
    print("Menú de Gestión de la Granja")
    print("1. Crear un corral")
    print("2. Registrar y Gestionar animal")
    print("3. Registrar un empleado")
    print("4. Realizar tarea del empleado")
    print ("5. Registrar alimentacion")
    print("6. Supervisar corrales")
    print("7. Registrar asistencia")
    print("8. Registrar control sanitario")
    print("9. Salir")

gr = Granja("HACIENDA NÁPOLES")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_corral = input("ID del corral: ")
        capacidad = int(input("Capacidad: "))
        estado = input("Estado: ")
        nuevo_corral = Corral(id_corral, capacidad, estado)
        gr.corrales.append(nuevo_corral)
        print("Corral creado exitosamente.")

    elif opcion == "2":
        while True:
            print("Submenú de Animales")
            print("1. Registrar nuevo animal")
            print("2. Actualizar información de un animal")
            print("3. Ver reporte de población")
            print("4. Volver al menú principal")
            subop = input("Seleccione una opción: ")

            if subop == "1":
                tipo = input("Tipo de animal (vaca/cerdo/gallina): ").lower()
                id_animal = input("ID del animal: ")
                edad = int(input("Edad: "))
                peso = float(input("Peso: "))

                if tipo == "vaca":
                    leche = float(input("Producción de leche: "))
                    animal = Vaca(id_animal, edad, peso, leche)
                elif tipo == "cerdo":
                    grasa = float(input("Grasa corporal: "))
                    animal = Cerdo(id_animal, edad, peso, grasa)
                elif tipo == "gallina":
                    huevos = int(input("Producción de huevos: "))
                    animal = Gallina(id_animal, edad, peso, huevos)
                else:
                    print("Tipo de animal no válido.")
                    continue

                if gr.corrales:
                    print("Corrales disponibles:")
                    for i, c in enumerate(gr.corrales):
                        print(f"{i+1}. {c.idCorral}")
                    indice = int(input("Seleccione el corral (número): ")) - 1
                    gr.corrales[indice].asignarAnimal(animal)
                    print("Animal registrado exitosamente.")
                else:
                    print("No hay corrales disponibles.")

            elif subop == "2":
                id_buscar = input("ID del animal a actualizar: ")
                encontrado = False
                for corral in gr.corrales:
                    for animal in corral.animales:
                        if animal.idAnimal == id_buscar:
                            print(f"Actualizando {animal.idAnimal} ({type(animal).__name__})")
                            animal.edad = int(input("Nueva edad: "))
                            animal.peso = float(input("Nuevo peso: "))
                            # Actualiza atributos específicos
                            if isinstance(animal, Vaca):
                                animal.leche = float(input("Nueva producción de leche: "))
                            elif isinstance(animal, Cerdo):
                                animal.grasa = float(input("Nueva grasa corporal: "))
                            elif isinstance(animal, Gallina):
                                animal.huevos = int(input("Nueva producción de huevos: "))
                            print("Información actualizada.")
                            encontrado = True
                            break
                if not encontrado:
                    print("Animal no encontrado.")

            elif subop == "3":
                print("Reporte de población animal:")
                total = {"vaca": 0, "cerdo": 0, "gallina": 0}
                for corral in gr.corrales:
                    for animal in corral.animales:
                        if isinstance(animal, Vaca):
                            total["vaca"] += 1
                        elif isinstance(animal, Cerdo):
                            total["cerdo"] += 1
                        elif isinstance(animal, Gallina):
                            total["gallina"] += 1
                for tipo, cantidad in total.items():
                    print(f"{tipo.capitalize()}s: {cantidad}")
                if sum(total.values()) == 0:
                    print("No hay animales registrados.")

            elif subop == "4":
                break

            else:
                print("Opción inválida. Intente de nuevo.")

    elif opcion == "3":
        id_empleado = input("ID del empleado:")
        nombre = input("Nombre: ")
        print("Cargos: 1. Sanidad  2. Limpieza  3. Alimentacion  4. Administrador")
        cargo = input("Seleccione el número de cargo: ")

        if cargo == "1":
            esp = input("Especialidad: ")
            empleado = EmpleadoSanidad(id_empleado, nombre, esp)
        elif cargo == "2":
            area = input("Área asignada: ")
            empleado = EmpleadoLimpieza(id_empleado, nombre, area)
        elif cargo == "3":
            tipo = input("Tipo de alimento: ")
            empleado = EmpleadoAlimentacion(id_empleado, nombre, tipo)
        elif cargo == "4":
            empleado = Administrador(id_empleado, nombre)
        else:
            print("Cargo no válido.")
            continue

        gr.empleados.append(empleado)
        print("Empleado registrado exitosamente.")

    elif opcion == "4":
        if not gr.empleados:
            print("No hay empleados registrados.")
            continue

        for i, emp in enumerate(gr.empleados):
            print(f"{i+1}. {emp.nombre} - {emp.cargo}")
        indice = int(input("Seleccione un empleado: ")) - 1
        emp = gr.empleados[indice]
        emp.realizarTarea()

    elif opcion == "5":
        tipo= input("Tipo de animal (vaca-cerdo-gallina): ").lower()
        tipo_alimento = input("Tipo de alimento: ")
        cantidad = float(input( "Cantidad de alimento en kg: "))
        fecha = input ("Fecha de alimentacion dia-mes-año: ")
        alimento =Alimento(tipo_alimento,cantidad,fecha)
        print(f"Alimento registrado para {tipo}: {cantidad}Kg de {tipo_alimento} el {fecha}.")

    elif opcion == "6":
        for corral in gr.corrales:
            print(f"Corral {corral.idCorral} - Estado: {corral.estado} - Capacidad: {corral.capacidad}")
            if corral.estado.lower() in ["sucio", "mantenimiento"]:
                print(" Alerta: Este corral necesita limpieza o mantenimiento.")
        mover = input("¿Desea mover un animal de corral? : ").lower()
        if mover == "s":
            origen = int(input("Número del corral origen: ")) - 1
            destino = int(input("Número del corral destino: ")) - 1
            print("Animales en el corral origen:")
            for i, animal in enumerate(gr.corrales[origen].animales):
                print(f"{i+1}. {animal.idAnimal}")
            indice_animal = int(input("Seleccione el animal a mover: ")) - 1
            animal = gr.corrales[origen].animales.pop(indice_animal)
            gr.corrales[destino].asignarAnimal(animal)
            print("Animal movido correctamente.")


    elif opcion == "7":
        hoy = datetime.date.today()
        for emp in gr.empleados:
            presente = input(f"¿{emp.nombre} asistió hoy? : ").lower()
            if emp.idEmpleado not in asistencias:
                asistencias[emp.idEmpleado] = []
            if presente == "s":
                asistencias[emp.idEmpleado].append(hoy)
            else:
                print(f" Alerta: {emp.nombre} ausente hoy.")
        print("Asistencias registradas.")

    elif opcion == "8":
        id_animal = input("ID del animal: ")
        vacuna = input("Nombre de la vacuna: ")
        dosis = float(input("Dosis aplicada: "))
        fecha = datetime.date.today()
        if id_animal not in registros_sanitarios:
            registros_sanitarios[id_animal] = []
        registros_sanitarios[id_animal].append({"vacuna": vacuna, "dosis": dosis, "fecha": fecha})
        print("Registro sanitario guardado.")
        if len(registros_sanitarios[id_animal]) > 1:
            ultima_fecha = registros_sanitarios[id_animal][-2]["fecha"]
            dias = (fecha - ultima_fecha).days
            if dias > 30:
                print(f"Alerta: {id_animal} llevaba {dias} días sin vacunación.")

    elif opcion == "9":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
