import subprocess, yaml, time, json, platform
from pathlib import Path
from utils.logger import setup_logger
from stress.monitor import monitor_cpu

logger = setup_logger()

def load_config():
    with open('config/settings.yaml') as f:
        return yaml.safe_load(f)['cpu_stress']

def run_stress_test(duration=None, workers=None):
    config = load_config()
    duration = duration or config['duration']
    workers = workers or config['workers']

    logger.info(f"Running CPU stress for {duration} seconds with {workers} workers")

    if platform.system() == "Linux":
        cmd = ["stress-ng", "--cpu", str(workers), "--timeout", f"{duration}s"]
    else:
        logger.error("Stress test not yet supported on Windows.")
        return {"status": "SKIPPED"}

    start_time = time.time()
    monitor_thread = monitor_cpu(duration, config['monitor_interval'])
    subprocess.run(cmd)
    cpu_stats = monitor_thread()
    elapsed = time.time() - start_time

    result = {
        "status": "PASS" if cpu_stats['max'] > config['expected_usage'] else "FAIL",
        "max_cpu_usage": cpu_stats['max'],
        "avg_cpu_usage": cpu_stats['avg'],
        "duration": elapsed
    }

    Path("reports").mkdir(exist_ok=True)
    with open(f"reports/result_{int(time.time())}.json", "w") as f:
        json.dump(result, f, indent=2)

    return result
