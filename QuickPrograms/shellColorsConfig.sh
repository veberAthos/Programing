#!/bin/bash
# Shell colors config
# Victor Bernal Rueda - vbernalr@cisco.com
# 01/10/2023

declare -A colors=(
[RED]="\\\033[1;31m"
[GREEN]="\\\033[1;32m"
[BLUE]="\\\033[1;34m"
[YELLOW]="\\\033[1;33m"
[PURPLE]="\\\033[1;35m"
[CYAN]="\\\033[1;36m"
[GREY]="\\\033[0;37m"
[RESET]="\\\033[m"
)

if grep -q "PS1=" $HOME/.bashrc ; then
    echo "Runnig .bashrc file has been modified, if you want to restore from backup enter option -d"
else
    cp $HOME/.bashrc $HOME/ORIGINAL_.bashrc
    echo ".bashrc file has been saved as ORIGINAL_.bashrc for backup"
fi

usage(){
    echo "Usage: $0 [OPTIONS] {arg1} {arg2} {arg3}" 1>&2;
    echo "This utility used to change profile shell colors"
    echo -e "\t -h, --help \t   Displays this help"
    echo -e "\t -d, --default \t Reset all colors to the default ones"
    echo -e "\t -c, --color \t show color selection"
    echo -e "\t -e, --edit \t  edit shell colors, arguments order:  {USER COLOR} {HOST COLOR} {PATH COLOR}"
    exit 1;
}

color(){
    echo -e "\033[1;31mRED \t\t\t \033[1;32mGREEN \t\t\t \033[1;34mBLUE"
    echo -e "\033[1;33mYELLOW \t\t\t \033[1;35mPURPLE \t\t \033[1;36mCYAN"
    echo -e "\033[0;37mGREY \t\t\t \033[mRESET"
    exit 1;
}

default(){
    # if [[ $EUID -ne 0 ]]; then
    #     echo "Make sure you're using root!"
    #     exit 1
    # fi
    
    sed -e '/PS1=/c\' -e "PS1=\"[\\\u@\\\h \\\W]$ \"" $HOME/.bashrc > $HOME/MODIFIED_.bashrc
    mv $HOME/MODIFIED_.bashrc $HOME/.bashrc
    source $HOME/.bashrc
    # cp $HOME/ORIGINAL_.bashrc $HOME/.bashrc
    echo "Backup restored"
    exit 1;
}

edit(){
    # if [[ $EUID -ne 0 ]]; then
    #     echo "Make sure you're using root!"
    #     exit 1
    # fi
    # echo $1
    # echo $2
    # echo $3
    if [ -z $1 ] || [ -z $2 ] || [ -z $3 ] ; then
        echo "Not enough arguments"
        exit 85
    else
        USER=$1
        HOST=$2
        xPATH=$3
        for key in ${!colors[@]} ; do
            if [ "$USER" = "$key" ] ; then
                # echo ${colors[$key]}
                USER=${colors[$key]}
            fi
            if [ "$HOST" = "$key" ] ; then
                HOST=${colors[$key]}
            fi
            if [ "$xPATH" = "$key" ] ; then
                xPATH=${colors[$key]}
            fi
        done
        # echo Colors will be changed to: ${!colors[$USER]} USER ${!colors[$HOST]} HOST ${!colors[$PATH]} PATH
        read -p "Do you confirm change? Y/N: " CONFIRM
        echo $USER $HOST $xPATH
        if [ $CONFIRM = "Y" -o $CONFIRM = "y" ] ; then
            if grep -q "PS1=" $HOME/.bashrc ; then
                sed -e '/PS1=/c\' -e "PS1=\"${USER}[\\\u${HOST}@\\\h ${xPATH}\\\w]${HOST}$ ${colors[RESET]}\"" $HOME/.bashrc > $HOME/MODIFIED_.bashrc     # add PS1 line with desired colors inside the profile bash
            else
                sed -e '/# User specific aliases and functions/a\' -e "PS1=\"${USER}[\\\u${HOST}@\\\h ${xPATH}\\\w]${HOST}$ ${colors[RESET]}\"" $HOME/.bashrc > $HOME/MODIFIED_.bashrc     # add PS1 line with desired colors inside the profile bash
                # export PS1="${2}[\u${3}@\h ${4}\W]${3}$ ${RESET}"
            fi
            # chmod 666 $HOME/*.bashrc
            mv $HOME/MODIFIED_.bashrc $HOME/.bashrc   # rename MOFIFIED_.bashrc to .bashrc
            source $HOME/.bashrc
            exit 1
        else
            echo "No changes made"
        fi
    # read -p COLORSET
    # if [ -z $COLORSET ] ; then
    #     echo "Entry error"
    #     exit 85
    # elif [ $COLORSET = ]
    fi
    exit 1
}

if [ $# -eq 0 ]
then
	usage
fi

while true ; do
    case "$1" in
        -h|--help) usage;;
        -d|--default) default;;
        -c|--color) color;;
        -e|--edit) edit $2 $3 $4;;
        *) echo "[ERROR] : Internal error!" ; exit 1 ;;
    esac
done

# # .bashrc

# # Source global definitions
# if [ -f /etc/bashrc ]; then
#         . /etc/bashrc
# fi

# # Uncomment the following line if you don't like systemctl's auto-paging feature:
# # export SYSTEMD_PAGER=

# # User specific aliases and functions