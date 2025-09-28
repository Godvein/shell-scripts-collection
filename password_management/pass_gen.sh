#!/bin/bash

#logic to generate password
generate_password(){
	PASSWORD=$(openssl rand -base64 "$1" 2> /dev/null)
	echo "$PASSWORD"
}

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
	echo "passgen.sh <n> --options"
	echo 
	echo "options:"
	echo "--save: save to a file"
    echo
    echo "###############################"
}
#check if first line arguement is an integer
if [[ "$1" =~ ^[0-9]+$ ]]
then 
	generate_password "$1"
else 
	generate_help
fi


