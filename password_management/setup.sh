#!/bin/bash

#this is a setup file


#clone in the script file
git clone https://github.com/Godvein/shell-scripts-collection.git

#change working dir to the password dir
cd shell-scripts-collection/password_management

#file permission
chmod +x passgen.sh 

#move to the bin
sudo mv passgen.sh /usr/local/bin/passgen

