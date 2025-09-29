#!/bin/bash

#logic to generate password
generate_password(){
	local PASSWORD=$(openssl rand -base64 "$1" 2> /dev/null)
	echo "$PASSWORD"

    #check if the second command line arguement is to save the password file
    if [ "$2" = "--save" ] || [ "$2" = "-s" ]
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
	echo "create by: Ankit Dware"
	echo
	echo "The script requires a number to be passed to determine the length of the password"
	echo 
	echo "passgen.sh <password_length> --options"
	echo 
	echo "options:"
	echo "-s, --save:           save to a file"
    echo
    echo "###############################"
}
#check if command line arguement is an integer
if [[ "$1" =~ ^[0-9]+$ ]]
then #generate password if the first line arguement is an integer
	generate_password "$1" "$2"

else    #generate help if no options match 
	generate_help
fi
