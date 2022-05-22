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
    (([5, 7, 7, 7, 8, 8, 11], 7), (1, 3)),
    (([5, 7, 7, 8, 8, 10], 6), (-1, -1)),
    (([], 69), (-1, -1)),
    (([1], 1), (0, 0)),
    (([1], 2), (-1, -1)),
    (([-100, -96, -64, -55, -47, -46, -43, -23, -10, -5, -4, 3, 18, 37, 37, 37, 37, 37], 37), (13, 17)),
    (([69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69], 69), (0, 29)),
    (([-95, -91, -87, -84, -73, -66, -54, -53, -25, -24, -10, -4], -95), (0, 0)),
    (([-95, -95, -95, -84, -73, -66, -54, -53, -25, -24, -10, -4], -95), (0, 2)),
    (([-95, -91, -87, -84, -73, -66, -54, -53, -25, -24, -10, -4], -24), (9, 9)),
    (([11, 13, 15, 16, 16, 16, 16, 16, 100000000], 16), (3, 7)),
]

tester = Test(challenge_method, tests, challenge_module)
