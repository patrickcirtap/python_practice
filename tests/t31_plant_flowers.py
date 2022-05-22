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
tests = [
    (([1, 0, 0, 0, 1], 1), True),
    (([1, 0, 0, 0, 1], 2), False),
    (([1, 0, 0, 1], 1), False),
    # length 1
    (([1], 1), False),
    (([1], 0), True),
    (([1], 2), False),
    # length 3
    (([1, 0, 1], 0), True),
    (([1, 0, 1], 1), False),
    (([1, 0, 1], 2), False),
    # length 4
    (([1, 0, 0, 1], 0), True),
    (([1, 0, 0, 1], 1), False),
    (([1, 0, 0, 1], 8), False),
    # length 5
    (([1, 0, 1, 0, 1], 0), True),
    (([1, 0, 1, 0, 1], 1), False),
    (([1, 0, 1, 0, 1], 4), False),
    # length 6 - none
    (([1, 0, 0, 0, 0, 1], 0), True),
    (([1, 0, 0, 0, 0, 1], 1), True),
    (([1, 0, 0, 0, 0, 1], 2), False),
    (([1, 0, 0, 0, 0, 1], 3), False),
    # length 6 - 1 first
    (([1, 0, 1, 0, 0, 1], 0), True),
    (([1, 0, 1, 0, 0, 1], 1), False),
    (([1, 0, 1, 0, 0, 1], 5), False),
    # length 6 - 1 second
    (([1, 0, 0, 1, 0, 1], 0), True),
    (([1, 0, 0, 1, 0, 1], 1), False),
    (([1, 0, 0, 1, 0, 1], 4), False),
    # length 7 - none
    (([1, 0, 0, 0, 0, 0, 1], 0), True),
    (([1, 0, 0, 0, 0, 0, 1], 1), True),
    (([1, 0, 0, 0, 0, 0, 1], 2), True),
    (([1, 0, 0, 0, 0, 0, 1], 3), False),
    # length 7 - first
    (([1, 0, 1, 0, 0, 0, 1], 0), True),
    (([1, 0, 1, 0, 0, 0, 1], 1), True),
    (([1, 0, 1, 0, 0, 0, 1], 2), False),
    (([1, 0, 1, 0, 0, 0, 1], 3), False),
    # length 7 - second
    (([1, 0, 0, 1, 0, 0, 1], 0), True),
    (([1, 0, 0, 1, 0, 0, 1], 1), False),
    (([1, 0, 0, 1, 0, 0, 1], 2), False),
    (([1, 0, 0, 1, 0, 0, 1], 3), False),
    # length 7 - third
    (([1, 0, 0, 0, 1, 0, 1], 0), True),
    (([1, 0, 0, 0, 1, 0, 1], 1), True),
    (([1, 0, 0, 0, 1, 0, 1], 2), False),
    (([1, 0, 0, 0, 1, 0, 1], 6), False),
    # length 7 - fourth
    (([1, 0, 1, 0, 1, 0, 1], 0), True),
    (([1, 0, 1, 0, 1, 0, 1], 1), False),
    (([1, 0, 1, 0, 1, 0, 1], 3), False),
    (([1, 0, 1, 0, 1, 0, 1], 5), False),
    # length 8 - first
    (([1, 0, 0, 0, 0, 0, 0, 1], 0), True),
    (([1, 0, 0, 0, 0, 0, 0, 1], 1), True),
    (([1, 0, 0, 0, 0, 0, 0, 1], 2), True),
    (([1, 0, 0, 0, 0, 0, 0, 1], 3), False),
    # length 8 - second
    (([1, 0, 1, 0, 0, 0, 0, 1], 0), True),
    (([1, 0, 1, 0, 0, 0, 0, 1], 1), True),
    (([1, 0, 1, 0, 0, 0, 0, 1], 2), False),
    (([1, 0, 1, 0, 0, 0, 0, 1], 3), False),
    # length 8 - second
    (([1, 0, 0, 1, 0, 0, 0, 1], 0), True),
    (([1, 0, 0, 1, 0, 0, 0, 1], 1), True),
    (([1, 0, 0, 1, 0, 0, 0, 1], 2), False),
    (([1, 0, 0, 1, 0, 0, 0, 1], 3), False),
    # length 8 - third
    (([1, 0, 0, 0, 1, 0, 0, 1], 0), True),
    (([1, 0, 0, 0, 1, 0, 0, 1], 1), True),
    (([1, 0, 0, 0, 1, 0, 0, 1], 2), False),
    (([1, 0, 0, 0, 1, 0, 0, 1], 3), False),
    # length 8 - fourth
    (([1, 0, 0, 0, 0, 1, 0, 1], 0), True),
    (([1, 0, 0, 0, 0, 1, 0, 1], 1), True),
    (([1, 0, 0, 0, 0, 1, 0, 1], 2), False),
    (([1, 0, 0, 0, 0, 1, 0, 1], 3), False),
    # length 8 - fifth
    (([1, 0, 1, 0, 1, 0, 0, 1], 0), True),
    (([1, 0, 1, 0, 1, 0, 0, 1], 1), False),
    (([1, 0, 1, 0, 1, 0, 0, 1], 2), False),
    (([1, 0, 1, 0, 1, 0, 0, 1], 3), False),
    # length 8 - sixth
    (([1, 0, 1, 0, 0, 1, 0, 1], 0), True),
    (([1, 0, 1, 0, 0, 1, 0, 1], 1), False),
    (([1, 0, 1, 0, 0, 1, 0, 1], 2), False),
    (([1, 0, 1, 0, 0, 1, 0, 1], 3), False),
    # length 8 - seven
    (([1, 0, 0, 1, 0, 1, 0, 1], 0), True),
    (([1, 0, 0, 1, 0, 1, 0, 1], 1), False),
    (([1, 0, 0, 1, 0, 1, 0, 1], 2), False),
    (([1, 0, 0, 1, 0, 1, 0, 1], 3), False),
    # larger lengths
    (([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1], 1), True),
    (([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1], 2), False),
    (([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1], 1), True),
    (([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1], 2), False),
]

tester = Test(challenge_method, tests, challenge_module)
