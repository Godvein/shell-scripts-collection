#!/bin/bash
#initialize boolean save
save=0
copy=0

#logic to generate password
generate_password(){
	PASSWORD=$(openssl rand -base64 "$1" 2> /dev/null)
	echo "$PASSWORD"

    #save function call condition
    if [ "$save" -eq 1 ]
    then
        save_password "$PASSWORD"
    fi

    #copy function call condition
    if [ "$copy" -eq 1 ]
    then
        copy_password "$PASSWORD"
    fi

}

#logic to save password file
save_password(){
    local PASSWORD="$1"

    #prompt to ask save location
    read -p "Where do you want to save the password to?" PASSWORD_PATH

    #prompt to save email/username
    read -p "Enter an email/username to save?" email

    #check if path is empty and save in working dir if empty
    if [ -z "$PASSWORD_PATH" ]
    then     
        echo "###########################################################" >> passgen_password.txt 2> /dev/null
        echo "new password created on $(date)" >> passgen_password.txt 2> /dev/null
        echo "email/username: $email" >> passgen_password.txt 2> /dev/null
        echo "password: $PASSWORD" >> passgen_password.txt 2> /dev/null
        echo >> passgen_password.txt 2> /dev/null
           
    else          
    #condition if save path is given
    echo "###########################################################" >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null
    echo "new password at created on $(date)" >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null
    echo "email/username: $email" >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null
    echo "password: $PASSWORD" >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null     
    echo >> $PASSWORD_PATH/passgen_password.txt 2> /dev/null
    fi

    if [ $? -eq 1 ]
    then
        echo " Permission denied: Run with sudo "
    fi
}

#detect_utility to copy to clipboard
detect_utility_copy(){
    if command -v wl-copy &> /dev/null
    then
        wl-copy

    elif command -v xclip &> /dev/null
    then
        xclip -selection clipboard

    elif command -v xsel &> /dev/null
    then
        xsel --clipboard

    else
        echo "######################################"
        echo "Error"
        echo "No copy utilities found"
        echo "Please install one of the following"
        echo "wl-clipboard"
        echo "xclip"
        echo "xsel"
        echo "####################################"
    fi

}

#copy password function
copy_password(){
    echo -n "$1" | detect_utility_copy

    if [ "$?" -eq 0 ]
    then
        echo "Password copied to clipboard"
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
    echo "-c, --copy:           copy to clipboard "
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
        -c | --copy)
            #copy to clipboard
            copy=1
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
else
#if no byte_count is give generate help
    generate_help
fi

