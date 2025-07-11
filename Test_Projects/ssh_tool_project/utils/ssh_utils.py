import paramiko


def ssh_run_command_and_save(ip, username, password, command, output_file):
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote machine
        ssh.connect(ip, username=username, password=password)
        print(f"Connected to {ip}")

        # Run the command
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        # Save output to file
        with open(output_file, 'w') as f:
            f.write("Command Output:\n")
            f.write(output)
            if error:
                f.write("\nError Output:\n")
                f.write(error)

        print(f"Command output saved to {output_file}")

        # Close connection
        ssh.close()

    except Exception as e:
        print(f"Error: {e}")
