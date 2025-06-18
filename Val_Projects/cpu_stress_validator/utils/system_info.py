import platform
import psutil

def get_cpu_cores():
return psutil.cpu_count(logical=True)

def is_windows():
return platform.system() == "Windows"

def is_linux():
return platform.system() == "Linux"