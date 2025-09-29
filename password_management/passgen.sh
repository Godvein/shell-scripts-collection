#!/bin/bash
#initialize boolean save
save=0

#logic to generate password
generate_password(){
	PASSWORD=$(openssl rand -base64 "$1" 2> /dev/null)
	echo "$PASSWORD"
    if [ "$save" -eq 1 ]
    then
        save_password "$PASSWORD"
    fi
}

#logic to save password file
save_password(){
    local PASSWORD="$1"

    #prompt to ask save location
    read -p "Where do you want to save the password to?" PASSWORD_PATH

    #check if path is empty and save in working dir if empty
    if [ -z "$PASSWORD_PATH" ]
    then     
        echo "###########################################################" >> passgen_password.txt 2> /dev/null
        echo "new password created on $(date)" >> passgen_password.txt 2> /dev/null 
        echo "$PASSWORD" >> passgen_password.txt 2> /dev/null
        echo >> passgen_password.txt 2> /dev/null
           
    else          
    echo "###########################################################" >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null
    echo "new password at created on $(date)" >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null
    echo "$PASSWORD" >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null     
    echo >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null
    fi

    if [ $? -eq 1 ]
    then
        echo " Permission denied: Run with sudo "
    fi
}

#generate help function
generate_help(){
	echo "#################################"
	echo
    echo "Looks like you need help"
    echo
	echo "This is a custom script"
	echo "created by: Ankit Dware"
	echo
	echo "The script requires a number to be passed to determine the length of the password"
	echo 
	echo "passgen.sh <byte_count> --[options]"
	echo 
	echo "options:"
    echo "-s, --save:           save to a file (you will be promted for the save location)"
    echo
    echo "###############################"
}
#check if user has passed command line arguements 
#loop through the arguements
while [[ $# -gt 0 ]]
do
    #switch case to set variable according to the arguements
    case "$1" in 
        -s | --save)
            #set save to true
            save=1
            ;;
        -h | --help)
            #generate help
            generate_help
            exit 0
            ;;
        [0-9]*)
            #set length
            byte_count=$1
            ;;
        *)
            #unknown arguement error
            echo "Unknown option: $1"
            generate_help
            exit 1
            ;;
    esac
    shift
done

#if byte_count is given and greated than 0 generate password
if [[ "$byte_count" =~ ^[0-9]+$ ]] && [ "$byte_count" -gt 0 ]
then
    generate_password "$byte_count"
fi
