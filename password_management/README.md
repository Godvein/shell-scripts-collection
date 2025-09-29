# passgen.sh

A simple yet Bash script to generate secure random passwords using `openssl`.  
It also provides an option to save generated passwords into a file for later use.

## Features
- Generate random passwords of any desired length.  
- Optionally save passwords to a file (`passgen_password.txt`) in a custom location or current directory.  
- Uses `openssl rand -base64` for strong, cryptographically secure passwords.  
- Built-in help for quick reference.  

## Installation

Clone the repository:
```bash
git clone https://github.com/<your-username>/shell-scripts-collection.git
cd shell-scripts-collection
```
Make the script executable:
```bash
`chmod +x passgen.sh` 
```
Move it to `/usr/local/bin` (so it can be used system-wide):
```bash
`sudo mv passgen.sh /usr/local/bin/passgen
```

Now you can run `passgen` command from anywhere
