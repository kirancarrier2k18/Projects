import paramiko


IP = "10.118.246.160"
port = 22
username = "root"
password = "Fle6J%rsKn"

try:
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # auto-accept unknown host keys

    # Connect to the remote server
    ssh.connect(IP, port, username, password)

    # Run a command
    command = "ls -l"  # change this to whatever you want to run
    stdin, stdout, stderr = ssh.exec_command(command)

    # Get the output
    output = stdout.read().decode()
    error = stderr.read().decode()

    print("=== Output ===")
    print(output)

    if error:
        print("=== Error ===")
        print(error)

    ssh.close()

except Exception as e:
    print(f"Connection failed: {e}")