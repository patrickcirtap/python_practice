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
    ((2, 3), 5),
    ((0, 8), 8),
    ((-10, -20), -30),
    ((926, 424), 1350),
    ((-754, -303), -1057),
    ((-123, 123), 0),
    ((751, -664), 87),
    ((-501, -225), -726),
    ((307, -473), -166),
    ((0, 0), 0),
    ((665, -446), 219),
    ((733, -356), 377),
    ((626, -988), -362),
    ((-999, -999), -1998),
    ((999, 999), 1998),
    ((999, 998), 1997)
]

tester = Test(challenge_method, tests, challenge_module)
