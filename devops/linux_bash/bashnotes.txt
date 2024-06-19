###### Piping ######
Piping - Connecting the stdout of one command to the stdin of another command using the pipe | symbol.

# List files and pipe to wc command
ls -l | wc -l

Redirection - Redirecting command output to a file instead of stdout using >.

# Redirect output to file
ls -l > output.txt

Conditional Execution - Chain commands using && to execute next command only if first succeeds.

ls file && echo "File exists"

Append - Append output to a file instead of overwriting using >>.

Control Characters - Modify command line with Ctrl+letter shortcuts like Ctrl+A start of line.

Python Example

Here is an example piping in Python using subprocess module:

import subprocess
# Call Bash pipeline and store result
result = subprocess.run("ls -l | wc -l", shell=True, text=True, capture_output=True)  
print(result.stdout)

###### Shell Piping ######

Shell piping - series of steps when you process data coming from an input, then sending the processed data to the output
input -> process -> output
For example: ls -h | wc -l > out.txt
list directory, then count the items in the directory and write the value to a file out.txt

The reading (https://github.com/noahgift/shell-pipes) covers core shell piping concepts like connecting commands for data processing, redirecting output to files, chaining execution, 
appending to files, and using control characters for command editing. It provides a comprehensive set of examples demonstrating piping, conditional execution, text processing and file handling, 
error suppression,  and leveraging command history.

# Basic pipe usage
ls -l /usr/bin | wc -l
# Redirect output to file 
ls -l > output.txt
# Conditional execution
[ -f file.txt ] && echo "File exists" 
# Append output
echo "Data" >> logfile.txt
# Edit command  
# Ctrl+A - Start of line
# Ctrl+E - End of line

Key Points

Pipes connect stdout to stdin to combine commands

Redirectors capture command output in files

Conditional execution chains dependent commands

Append mode adds to existing files

Control characters enable command editing

SSH (Secure Shell) - A protocol that allows secure communication between two systems over an unsecured network. It enables encrypted tunneling, remote command execution, and forwarding network ports.

SSH Keys - A public/private key pair used to authenticate and securely communicate with remote systems using SSH without needing passwords.

Git - A distributed version control system for tracking changes in source code and coordinating work on projects across multiple developers.

GitHub - A cloud-based platform built around Git for hosting and collaborating on software development projects.

Port Forwarding - A technique that allows redirecting incoming network connections from one port/IP on a machine to another port/IP. Useful for accessing services running on remote internal systems.

Bash Code Examples

The ssh-keygen command generates a public/private key pair that can be used for SSH authentication.

The cat command prints out the public key file needed to add to GitHub for access.

The git clone command clones a GitHub repo via SSH using the public/private keys.

The ssh -L command forwards port 8080 on the remote host to local port 8080 for access.

# Verbosely demonstrate piping, redirection, conditional execution
# Print files in directory
echo "Listing files..."
ls -l 
# Pipe files into line count
echo "Piping to wc..." 
ls -l | wc -l

# Redirect output to file
echo "Redirecting output..."
ls > directory_listing.txt

# Conditional file creation
if [ -f key_file.txt ]; then
    echo "File exists, creating new file..." 
    touch new_file.txt
fi

# Generate public/private SSH key pair
ssh-keygen -t rsa -b 4096 -C "myemail@example.com"  
# Print the generated public key 
cat ~/.ssh/id_rsa.pub
# Clone a GitHub repo via SSH 
git clone git@github.com:user/repo.git
# Port forward remote port 8080 to local port 8080
ssh -L 8080:localhost:8080 user@remotehost