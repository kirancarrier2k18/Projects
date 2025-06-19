from stress.stress_runner import stress_cpu, stress_memory
from utils.logger import setup_logger
import yaml

logger = setup_logger()

def load_config():
    with open("config/settings.yaml") as f:
        return yaml.safe_load()["ssh"]

if __name__ == "__main__":
    cfg = load_config()
    logger.info("Running CPU Stress Test...")
    cpu_result = stress_cpu(cfg["ip"], cfg["username"], cfg["password"], cfg["duration"])
    logger.info(cpu_result)

    logger.info("Running Memory Stress Test...")
    mem_result = stress_memory(cfg["ip"], cfg["username"], cfg["password"], cfg["duration"])
    logger.info(mem_result)
