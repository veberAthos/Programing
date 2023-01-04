import csv

file = "names.csv" # Nombre del archivo contenedor de las notas

with open(file, 'r') as data: # creamos la lista de directorios
	reader = csv.DictReader(data)
	name_list = list(reader)

for i in range(len(name_list)): # convertimos las notas a float para operar en el programa
    name_list[i][''] = int(name_list[i][''])
    name_list[i]['n1'] = float(name_list[i]['n1'])
    name_list[i]['n2'] = float(name_list[i]['n2'])
    name_list[i]['n3'] = float(name_list[i]['n3'])
    name_list[i]['score'] = float(name_list[i]['score'])

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
    0. Regresar"""

def nuevoEst():
    return "nuevoEst"

def editEst():
    while True:
        for i in range(len(name_list)):
            print(name_list[i]) #****Editar para imprimir mejor
        
        sel2 = int(input("Seleccione uno de los estudiantes o presione 0 para salir a Menu principal: "))
        if sel2 == 0:
            break
        print("Estudiante seleccionado {}".format(name_list[sel2-1]['name']))
        while True:
            print(menuEditEst)
            sel3 = int(input("\nSeleccion: "))
            if sel3 == 0:
                break
            elif sel3 == 1:
                name = raw_input("Ingrese nuevo nombre: ")
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
            else:
                print("Intente denuevo")
    return

def notaFinalEst():
    return "\nnotaFinalEst\n"

def notaFinal():
    for i in range(len(name_list)):
        print(name_list[i]['name'])
    name = raw_input("De cual estudiante quiere saber la nota final?")
    if name in name_list:
        return
    return "\nnotaFinal\n"

def saveChg(name_list):
    return "saveChg"

while True:
    print (menuPrinc)

    sel1 = int(input("\nSeleccion: "))

    if sel1 == 1:
        print(nuevoEst())
    elif sel1 == 2:
        editEst()
    elif sel1 == 3:
        print(notaFinalEst())
    elif sel1 == 4:
        print(notaFinal())
    elif sel1 == 5:
        print(saveChg())
    elif sel1 == 0:
        print('\nBye!')
        break
    else:
        print('\nSeleccion incorrecta, intente denuevo\n')
        continue
    
    
    

