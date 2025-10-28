#!/bin/bash

createProject(){
    #read project and package name
    read -p "enter project name: " PROJECT
    read -p "enter package name (example: com.company): " PACKAGE

    #convert package name to directory path
    PACKAGE_PATH=${PACKAGE//./\/}

    #make the project
    mkdir -p $PROJECT/src/main/java/$PACKAGE_PATH
    mkdir -p $PROJECT/src/test/java/$PACKAGE_PATH
    mkdir $PROJECT/lib
    mkdir $PROJECT/build
    touch $PROJECT/README.md
    touch $PROJECT/.gitignore

    #create Main.java file
    MAIN_FILE="$PROJECT/src/main/java/$PACKAGE_PATH/Main.java"
    touch $MAIN_FILE
    cat > "$MAIN_FILE" <<EOL
    package $PACKAGE;

    public class Main {
        public static void main(String[] args) {
            System.out.println("Hello from $PROJECT!");
        }
    }
EOL
}

run(){
    #read project and package name
    read -p "enter project name to run: " PROJECT
    read -p "enter package name to run (example: com.company): " PACKAGE

    #convert package name to directory path
    PACKAGE_PATH=${PACKAGE//./\/}

    # compile and interpret
    javac -d $PROJECT/build $PROJECT/src/main/java/$PACKAGE_PATH/Main.java
    java -cp $PROJECT/build $PACKAGE.Main

}

if [ "$1" == "run" ]
then
    run 
else
    createProject
fi
