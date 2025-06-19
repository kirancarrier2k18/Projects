from utils.ssh_executor import run_remote_command

def stress_cpu(ip, user, password, duration=30):
    command = f"stress-ng --cpu 0 --timeout {duration}s"
    out, err = run_remote_command(ip, user, password, command)
    return {"type": "CPU", "output": out.strip(), "error": err.strip(), "status": "PASS" if not err else "FAIL"}

def stress_memory(ip, user, password, duration=30):
    command = f"stress-ng --vm 1 --vm-bytes 256M --timeout {duration}s"
    out, err = run_remote_command(ip, user, password, command)
    return {"type": "Memory", "output": out.strip(), "error": err.strip(), "status": "PASS" if not err else "FAIL"}
