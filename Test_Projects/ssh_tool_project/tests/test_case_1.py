# tests/test_case_1.py
import sys
import os

# Add project root to sys.path so utils can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import ssh_run_command_and_save

def test_ssh_connection():
    ip = '100.98.116.57'               # Replace with your target IP
    username = 'root'                 # Replace with your username
    password = 'dell@123'        # Replace with your password
    command = 'lspci | grep -i nvidia'              # Simple OS command

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_file = os.path.join(project_root, 'logs', 'remote_output.txt')

    try:
        ssh_run_command_and_save(ip, username, password, command, output_file)
        print("✅ SSH function called successfully from utils.")
    except Exception as e:
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    test_ssh_connection()
