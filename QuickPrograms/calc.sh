#!/bin/bash
# Calcularoda Basica
# Victor Bernal Rueda - vbernalr@cisco.com
# 01/10/2023

menu(){
    # echo "Usage: $0 [OPTIONS]" 1>&2;
    echo "**********************"
    echo "* CALCULADORA BASICA *"
    echo "**********************"
    echo -e "\nSeleccione la operacion a realizar:\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division"
}

getNum(){
    echo -e "Ingrese el primer numero a operar: \c"
    read NUM1
    echo -e "Ingrese el segundo numero a operar: \c"
    read NUM2
}

while true ; do
    echo ""
    menu
    echo -e "Seleccion: \c"
    read SEL
    case $SEL in
        1)  echo "Suma"
            getNum
            echo -e $"El resultado es $[$NUM1+$NUM2]";;
        2)  echo "Resta"
            getNum
            echo -e $"El resultado es $[$NUM1-$NUM2]";;
        3)  echo "Multiplicacion"
            getNum
            echo -e $"El resultado es $[$NUM1*$NUM2]";;
        4)  echo "Division"
            getNum
            echo -e $"El resultado es $[$NUM1/$NUM2]";;
        *)  echo "Seleccione entre opcion 1 a 4";;
    esac
    echo -e "Desea realizar otra operacion? presione n para salir: \c"
    read REPETIR
    if [ $REPETIR = "N" ] || [ $REPETIR = "n" ] ; then
        exit 1
    fi
done