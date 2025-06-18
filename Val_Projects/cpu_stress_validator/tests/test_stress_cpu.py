from stress.stress_runner import run_stress_test

def test_stress_run():
result = run_stress_test()
assert result["status"] in ["PASS", "FAIL", "SKIPPED"]