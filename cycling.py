import os
import time
import subprocess
import paramiko


def ping_ip(ip):
    response = os.system(f"ping -c 1 {ip}")
    return response == 0


def reboot_system(ip, username, password, timeout=300):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        ssh.connect(ip, username=username, password=password)

        # Reboot the remote server
        ssh.exec_command("sudo reboot")
        ssh.close()

        # Wait until the system is up
        start_time = time.time()
        while time.time() - start_time < timeout:
            if ping_ip(ip):
                return True
            time.sleep(5)
        return False
    except Exception as e:
        print(f"Failed to reboot the server: {e}")
        return False


def check_nvidia_smi():
    result = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
    return result.stdout


def main():
    ip = "100.98.116.51"
    username = "your_username"
    password = "your_password"

    # Check if IP is up
    if ping_ip(ip):
        print(f"{ip} is up.")
    else:
        print(f"{ip} is down. Rebooting the system...")

        # Reboot the system and wait until it's up
        if reboot_system(ip, username, password):
            print(f"{ip} is back up.")

            # Check nvidia-smi and save the output
            nvidia_smi_output = check_nvidia_smi()
            with open("cycle1_OSlog.txt", "w") as file:
                file.write(nvidia_smi_output)
            print("nvidia-smi output saved to cycle1_OSlog.txt.")
        else:
            print(f"Failed to bring {ip} back up within the timeout period.")


if __name__ == "__main__":
    main()
