ids = []
asignaturas = []
codigos = []
docentes = []
grados = []
horas = []
salones = []
estados = []
observaciones = []
#----------------------------------------------#
#--|menu_principal_administrador_asignaturas|--#
#----------------------------------------------#
while True:
    print("menu principal administrador de asignaturas")
    print("1) crear asignatura")
    print("2) editar asignatura")
    print("3) eliminar asignatura")
    print("4) buscar asignatura")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #----------------------#
    #--|crear_asignatura|--#
    #----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_asignatura = 1
        else:
            id_asignatura = ids[-1] + 1
        asignatura = input("nombre de la asignatura: ")
        codigo = input("código de la asignatura: ")
        docente = input("docente responsable: ")
        grado = input("grado: ")
        hora = int(input("intensidad horaria (horas por semana): "))
        salon = input("salón: ")
        estado = input("estado de la asignatura: ")
        observacion = input("observación: ")
        ids.append(id_asignatura)
        asignaturas.append(asignatura)
        codigos.append(codigo)
        docentes.append(docente)
        grados.append(grado)
        horas.append(hora)
        salones.append(salon)
        estados.append(estado)
        observaciones.append(observacion)
        print("asignatura registrada correctamente.")
        print("id:", id_asignatura)
    #-----------------------#
    #--|editar_asignatura|--#
    #-----------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar asignatura")
            for i in range(len(ids)):
                print(f"{ids[i]} | {asignaturas[i]} | {codigos[i]} | {docentes[i]} | {grados[i]} | {horas[i]} | {salones[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {asignaturas[posicion]} | {codigos[posicion]} | {docentes[posicion]} | {grados[posicion]} | {horas[posicion]} | {salones[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                asignaturas[posicion] = input("nueva asignatura: ")
                codigos[posicion] = input("nuevo código: ")
                docentes[posicion] = input("nuevo docente: ")
                grados[posicion] = input("nuevo grado: ")
                horas[posicion] = int(input("nueva intensidad horaria: "))
                salones[posicion] = input("nuevo salón: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-------------------------#
    #--|eliminar_asignatura|--#
    #-------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar asignatura")
            for i in range(len(ids)):
                print(f"{ids[i]} | {asignaturas[i]} | {codigos[i]} | {docentes[i]} | {grados[i]} | {horas[i]} | {salones[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {asignaturas[posicion]} | {codigos[posicion]} | {docentes[posicion]} | {grados[posicion]} | {horas[posicion]} | {salones[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    asignaturas.pop(posicion)
                    codigos.pop(posicion)
                    docentes.pop(posicion)
                    grados.pop(posicion)
                    horas.pop(posicion)
                    salones.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|buscar_asignatura|--#
    #-----------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar asignatura")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {asignaturas[posicion]} | {codigos[posicion]} | {docentes[posicion]} | {grados[posicion]} | {horas[posicion]} | {salones[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = horas[0]
            menor = horas[0]
            activas = 0
            inactivas = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {asignaturas[i]} | {codigos[i]} | {docentes[i]} | {grados[i]} | {horas[i]} | {salones[i]} | {estados[i]} | {observaciones[i]}")
                suma += horas[i]
                if horas[i] > mayor:
                    mayor = horas[i]
                if horas[i] < menor:
                    menor = horas[i]
                if estados[i].lower() == "activa":
                    activas += 1
                elif estados[i].lower() == "inactiva":
                    inactivas += 1
            promedio = suma / len(ids)
            print("estadísticas administrador de asignaturas")
            print("cantidad de registros:", len(ids))
            print("horas semanales acumuladas:", suma)
            print("promedio de horas:", round(promedio, 2))
            print("mayor intensidad horaria:", mayor)
            print("menor intensidad horaria:", menor)
            print("asignaturas activas:", activas)
            print("asignaturas inactivas:", inactivas)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")