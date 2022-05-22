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
    ((1, 2, '+'), 3),
    ((100, 4, '/'), 25),
    ((4, 100, '/'), 0.04),
    ((69, 420, '+'), 489),
    ((8, 83, '*'), 664),
    ((10, 8, '*'), 80),
    ((-98, 68, '-'), -166),
    ((51, 23, '-'), 28),
    ((-51, 11, '/'), -4.636363636363637),
    ((30, -9, '*'), -270),
    ((16, 84, '*'), 1344),
    ((-44, 78, '*'), -3432),
    ((0, 0, '/'), "undefined"),
    ((-70, 36, '+'), -34),
    ((-26, -38, '-'), 12),
    ((57, 68, '-'), -11),
    ((-48, -59, '+'), -107),
    ((-56, -71, '+'), -127),
    ((-2, -3, '/'), 0.6666666666666666),
    ((-85, 5, '/'), -17.0),
    ((-82, 28, '/'), -2.9285714285714284),
    ((64, 30, '-'), 34),
    ((-72, 54, '/'), -1.3333333333333333),
    ((39, 14, '*'), 546),
    ((-80, 59, '-'), -139),
    ((69, 0, '/'), "undefined"),
    ((-9, 92, '-'), -101),
    ((78, 75, '*'), 5850),
    ((0, 420, '/'), 0),
    ((-17, -45, '-'), 28),
    ((-68, -61, '+'), -129),
    ((60, 38, '*'), 2280),
]

tester = Test(challenge_method, tests, challenge_module)
