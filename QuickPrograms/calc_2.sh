#!/bin/bash
# Calculadora Basica
# Victor Bernal Rueda - vbernalr@cisco.com
# 01/10/2023

menu(){
    # echo "Usage: $0 [OPTIONS]" 1>&2;
    echo "**********************"
    echo "* CALCULADORA BASICA *"
    echo "**********************"
    echo -e "\nSeleccione la operacion a realizar:"
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
    OPTIONS="Suma Resta Multiplicacion Division Salir"
    select opt in $OPTIONS; do
        if [ "$opt" = "Suma" ]; then
            echo "Suma"
            getNum
            echo -e $"El resultado es $[$NUM1+$NUM2]"
            echo done
            continue
        elif [ "$opt" = "Resta" ]; then
            echo "Resta"
            getNum
            echo -e $"El resultado es $[$NUM1-$NUM2]"
            echo done
            continue
        elif [ "$opt" = "Multiplicacion" ]; then
            echo "Multiplicacion"
            getNum
            echo -e $"El resultado es $[$NUM1*$NUM2]"
            echo done
            continue
        elif [ "$opt" = "Division" ]; then
            echo "Division"
            getNum
            echo -e $"El resultado es $[$NUM1/$NUM2]"
            continue
        elif [ "$opt" = "Salir" ]; then
            echo "Salir"
            exit 1;
        else
                echo bad option
                continue
        fi
    done
done