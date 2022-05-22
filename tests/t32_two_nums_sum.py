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
    (([2, 7, 11, 15], 9), (0, 1)),
    (([3, 2, 4], 6), (1, 2)),
    (([69, 420], 489), (0, 1)),
    (([3, 3], 6), ((0, 1))),
    (([19, 7, 4, 5, 1, 11, 2, 20, 12, 3, 17, 15, 9], 3), ((4, 6))),
    (([19, 7, 4, 5, 0, 11, 2, 20, 12, 3, 17, 15, 9], 3), ((4, 9))),
    (([92, 48, 16, 55, 99, 84, 71, 15], 191), ((0, 4))),
    (([53, 72, 34, 11, 96, 100, 28, 24, 87, 71, 35, 97, 2, 22, 95, 86, 18, 38, 47, 33], 80), ((18, 19))),
    (([32, 45, 3, 10, 22, 55, 26, 66, 2], 76), ((3, 7))),
    (([893, 103, 749, 628, 589, 677, 541, 732, 703, 756, 141, 869, 663, 445, 252, 799, 259, 903, 31, 536, 791, 776, 68, 761, 240, 42, 414, 864, 641, 121, 313, 601], 224), ((1, 29))),
]

tester = Test(challenge_method, tests, challenge_module)
