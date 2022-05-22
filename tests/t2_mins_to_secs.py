import glob
import importlib
import re
import sys
sys.path.append("..")

if __name__ == "__main__":
    if("run_test.py" not in sys.argv):
        print("Test file can not be run directly - use run_test.py")
        sys.exit(1)

try:
    from run_test import Test
except RuntimeError:
    print(f"Error importing tester: {RuntimeError}")
    sys.exit(1)
try:
    challenge_module = glob.glob(f"c{sys.argv[1]}_*.py")[0]
    # Remove ".py" from file name
    challenge_module = challenge_module[:-3]
    # Remove "cN_" from file name
    challenge_function = re.sub(r'^.*?_', '', challenge_module)

    module = importlib.import_module(challenge_module)
    challenge_method = getattr(module, challenge_function)
except RuntimeError:
    print(f"Error importing challenge function: {RuntimeError}")
    sys.exit(1)

# List of all tests. Each test has form:
# ( (params_tuple), exp_result )
# Params must be tuple so they can be un-packed when called
##### CHANGE HERE: #####
tests = [
    ((1, ), 60),
    ((2, ), 120),
    ((3.5, ), 210),
    ((0.5, ), 30),
    ((0.002, ), 0.12),
    ((3.1415926, ), 188.495556),
    ((5, ), 300),
    ((15, ), 900),
    ((10, ), 600),
    ((11, ), 660),
    ((0, ), 0),
    ((6, ), 360),
    ((19, ), 1140),
    ((12, ), 720),
]

tester = Test(challenge_method, tests, challenge_module)
