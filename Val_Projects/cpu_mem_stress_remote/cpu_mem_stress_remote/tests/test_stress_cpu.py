from stress.stress_runner import stress_cpu, stress_memory
import yaml

def load_config():
    with open("config/settings.yaml") as f:
        return yaml.safe_load()["ssh"]

def test_cpu_stress():
    cfg = load_config()
    result = stress_cpu(cfg["ip"], cfg["username"], cfg["password"], cfg["duration"])
    assert result["status"] == "PASS"

def test_memory_stress():
    cfg = load_config()
    result = stress_memory(cfg["ip"], cfg["username"], cfg["password"], cfg["duration"])
    assert result["status"] == "PASS"
