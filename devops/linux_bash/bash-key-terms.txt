Shebang - The first line of a script that indicates the interpreter to use for executing the script. 
Example: #!/usr/bin/env python3

#!/bin/bash
echo "Hello World"

Chmod - A Linux command to change the permissions/access mode of files or directories. Used to make scripts executable.

chmod +x myscript.sh

Alias - A shortcut that can be defined in bash to replace a longer command or series of commands. Configured in .bashrc.

alias lm='ls -al | more'

Export - Makes a variable available across shell sessions and to child processes. Used to expose things like API keys.

export DB_PASSWORD='mysecurepass'

Find - A Linux command to search for files/folders in real-time based on various criteria. More exhaustive than locate.

find . -name "*.py"

# Shebang indicating Bash interpreter
#!/bin/bash
# Print hello world 
echo "Hello World"
# Set an environment variable
export MY_VAR="some value"
# Print the variable
echo $MY_VAR
# Define an alias
alias ll="ls -l"
# Use the alias 
ll

# bash command structure
[cmd] [-option] [target]
ls -al /tmp

/usr/bin is the location from root where one can access all the commands and explore them for learning