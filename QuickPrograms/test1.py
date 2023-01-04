import csv

file = "names.csv"

with open(file, 'r') as data:
	dict_reader = csv.DictReader(data)
	name_list = list(dict_reader)
	#print(dict_reader)

for i in range(len(name_list)):
    name_list[i]['n1'] = float(name_list[i]['n1'])
    name_list[i]['n2'] = float(name_list[i]['n2'])
    name_list[i]['n3'] = float(name_list[i]['n3'])
    name_list[i]['score'] = float(name_list[i]['score'])

"""name = input("Ingrese el nombre del nuevo estudiante: ")
n1 = float(input("Ingrese la nota 1 para {}: ".format(name)))
n2 = float(input("Ingrese la nota 2 para {}: ".format(name)))
n3 = float(input("Ingrese la nota 3 para {}: ".format(name)))
nuevo_est = {'': len(name_list)+1, 'name': name, 'n1': n1, 'n2': n2, 'n3': n3, 'score': 0.0}
name_list.append(nuevo_est)"""

for i in range(len(name_list)):
    print(name_list[i]) #****Editar para imprimir mejor
        
while True:
    sel2 = input("Seleccione uno de los estudiantes o presione 0 para salir a Menu principal: ")
    #print(type(sel2))
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
    
        

for i in range(len(name_list)):
        print(name_list[i]) #****Editar para imprimir mejor

#print(name_list)

