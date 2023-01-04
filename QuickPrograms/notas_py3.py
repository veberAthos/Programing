import csv

file = "names.csv" # Nombre del archivo contenedor de las notas

with open(file, 'r') as data: # creamos la lista de directorios
	reader = csv.DictReader(data)
	name_list = list(reader)

for i in range(len(name_list)): # convertimos las notas a float para operar en el programa
    name_list[i]['n1'] = float(name_list[i]['n1'])
    name_list[i]['n2'] = float(name_list[i]['n2'])
    name_list[i]['n3'] = float(name_list[i]['n3'])
    name_list[i]['score'] = float(name_list[i]['score'])

headers = ['ID','name','n1','n2','n3','score']

menuPrinc ="""
    #######################
    # CALCULAR NOTA FINAL #
    #######################
    
    Que accion desea hacer?
    1. Nuevo estudiante
    2. Editar estudiante
    3. Nota final por estudiante
    4. Nota final todos registrados
    5. Guardar cambios
    0. Salir"""

menuEditEst ="""
    Editar:
    1. Nombre
    2. Nota 1
    3. Nota 2
    4. Nota 3
    5. Eliminar
    0. Regresar"""

def nuevoEst():
    name = input("Ingrese el nombre del nuevo estudiante: ")
    n1 = float(input("Ingrese la nota 1 para {}: ".format(name)))
    n2 = float(input("Ingrese la nota 2 para {}: ".format(name)))
    n3 = float(input("Ingrese la nota 3 para {}: ".format(name)))
    nuevo_est = {'ID': str(len(name_list)+1), 'name': name, 'n1': n1, 'n2': n2, 'n3': n3, 'score': 0.0}
    name_list.append(nuevo_est)
    for i in range(len(name_list)):
            print(name_list[i]) #****Editar para imprimir mejor
    return

def editEst():
    while True:
        for i in range(len(name_list)):
            print(name_list[i]) #****Editar para imprimir mejor
        
        while True:
            sel2 = input("Seleccione uno de los estudiantes o presione 0 para salir a Menu principal: ")
            if sel2 == "0": 
                return
            exist = bool()

            for i in range(len(name_list)):
                #print(name_list[i])
                if sel2 == name_list[i]['ID']:
                    exist = True
                    sel2 = int(sel2)
                    break
                else:
                    exist = False
            if exist == True:
                break
            else:
                print("No esta en la lista, intente denuevo")
        
        print("Estudiante seleccionado {}".format(name_list[sel2-1]['name']))
        while True:
            print(menuEditEst)
            while True:
                sel3 = input("\nSeleccion: ")
                if sel3 == '0' or sel3 == '1' or sel3 == '2' or sel3 == '3' or sel3 == '4' or sel3 == '5':
                    sel3 = int(sel3)
                    break
                else:
                    print("No esta en la lista, intente denuevo")
            if sel3 == 0:
                break
            elif sel3 == 1:
                name = input("Ingrese nuevo nombre: ")
                name_list[sel2-1]['name'] = name
                print(name_list[sel2-1])
            elif sel3 == 2:
                note = float(input("Ingrese nueva nota 1: "))
                name_list[sel2-1]['n1'] = note
                print(name_list[sel2-1])
            elif sel3 == 3:
                note = float(input("Ingrese nueva nota 2: "))
                name_list[sel2-1]['n2'] = note
                print(name_list[sel2-1])
            elif sel3 == 4:
                note = float(input("Ingrese nueva nota 3: "))
                name_list[sel2-1]['n3'] = note
                print(name_list[sel2-1])
            elif sel3 == 5:
                removed = name_list.pop(sel2-1)
                print("Eliminado: {}".format(removed))
                break
            else:
                print("Intente denuevo")
    return

def notaFinalEst():
    for i in range(len(name_list)):
        print(name_list[i]['name'])
    name = input("De cual estudiante quiere saber la nota final?: ")
    for i in range(len(name_list)):
        if name in name_list[i]['name']:
            name_list[i]['score'] = (name_list[i]['n1'] + name_list[i]['n2'] + name_list[i]['n3'])/3
            print("La nota para el estudiante {0} es: {1:.1f}".format(name, name_list[i]['score']))
            return
    return

def notaFinal():
    for i in range(len(name_list)):
        name_list[i]['score'] = (name_list[i]['n1'] + name_list[i]['n2'] + name_list[i]['n3'])/3
        print(name_list[i]['name'],end="\t--->\t")
        print("{:.1f}".format(name_list[i]['score']))
    return

def saveChg(name_list):
    try:
        with open(file, 'w') as data:
            d_writer = csv.DictWriter(data,fieldnames=headers)
            d_writer.writeheader()
            d_writer.writerows(name_list)
    except:
        print("Error when saving, please try again")
    else:
        print("File saved as: {}".format(file))
    return

while True:
    print (menuPrinc)

    sel1 = input("\nSeleccion: ")

    if sel1 == "0" or sel1 == "1" or sel1 == "2" or sel1 == "3" or sel1 == "4" or sel1 == "5":
        sel1 = int(sel1)
    else:
        print('\nSeleccion incorrecta, intente denuevo\n')
        continue
    
    if sel1 == 1:
        nuevoEst()
    elif sel1 == 2:
        editEst()
    elif sel1 == 3:
        notaFinalEst()
    elif sel1 == 4:
        notaFinal()
    elif sel1 == 5:
        saveChg(name_list)
    elif sel1 == 0:
        confirm = input("Seguro que desea salir? Y/N: ")
        if confirm == "Y" or confirm == "y":
            print('\nBye!')
            break
    else:
        print('\nSeleccion incorrecta, intente denuevo\n')
        continue
    
    
    

