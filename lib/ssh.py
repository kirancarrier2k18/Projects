import paramiko



#Server_ip=(input("Enter the Server IP: "))
#Username=input("Enter the Username: ")
#Password=input("Enter the Password: ")

# Create an SSH client
ssh = paramiko.SSHClient()

# Automatically add the server's host key (not recommended for production)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server using an SSH key
ssh.connect(hostname="100.98.116.51", username="root", password="dell@123")

# Execute a command
stdin, stdout, stderr = ssh.exec_command('uname -r')

# Print the output
print(stdout)

# Close the connection
ssh.close()



