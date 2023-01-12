#!/bin/bash
# Retrieve Value from dictionary
# Victor Bernal Rueda - vbernalr@cisco.com
# 01/12/2023

declare -A colors=(
[RED]="\033[1;31m"
[GREEN]="\033[1;32m"
[YELLOW]="\033[1;33m"
[BLUE]="\033[1;34m"
[PURPLE]="\033[1;35m"
[CYAN]="\033[1;36m"
[GREY]="\033[0;37m"
[RESET]="\033[m"
)

read -p "USER COLOR: " USER
read -p "HOST COLOR: " HOST
read -p "PATH COLOR: " PATH

for key in "${!colors[@]}" ; do
    if [ "$USER" = "$key" ] ; then
        # echo ${colors[$key]}
        USER=${colors[$key]}
    fi
    if [ "$HOST" = "$key" ] ; then
        HOST=${colors[$key]}
    fi
    if [ "$PATH" = "$key" ] ; then
        PATH=${colors[$key]}
    fi
done

# echo Colors will be changed to: "${!colors[$USER]}" USER "${!colors[$HOST]}" HOST "${!colors[$PATH]}" PATH

# echo colors has ${#colors[@]} element

# echo ${colors[$USER]}
# echo ${colors[$HOST]}
# echo ${colors[$PATH]}