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
    (([1, 2, 3, 4], ), [4, 3, 2, 1]),
    (([5], ), [5]),
    (([], ), []),
    (([-1, -1, -1], ), [-1, -1, -1]),
    (([40, 1, 26, 36, 77, 54, 76, 37, 3, 38, -7, 10, 32, 17, 28, 32, 12, 14],), [14, 12, 32, 28, 17, 32, 10, -7, 38, 3, 37, 76, 54, 77, 36, 26, 1, 40]),
    (([18],), [18]),
    (([13, 46, 69, 23],), [23, 69, 46, 13]),
    (([18, 53, 66, 45, 22, 62, 44, -8, 5, 32],), [32, 5, -8, 44, 62, 22, 45, 66, 53, 18]),
    (([72, 38, 46, 64, 63, 36, 80, 80, -8, -3, 32, 36, 18, 69],), [69, 18, 36, 32, -3, -8, 80, 80, 36, 63, 64, 46, 38, 72]),
    (([63, 68],), [68, 63]),
    (([6, -7, 38],), [38, -7, 6]),
    (([80, -7, 0, 48, -7, 18, 39, -5, 2],), [2, -5, 39, 18, -7, 48, 0, -7, 80]),
    (([4, 74],), [74, 4]),
    (([47, 66, 36, 59, 34, 32, 32, 55, 11, 42, 20, 73, 48, 25, 8, 25, 72],), [72, 25, 8, 25, 48, 73, 20, 42, 11, 55, 32, 32, 34, 59, 36, 66, 47]),
    (([66, 68, 34, 64, 20, -5, 74, 3, -4, 56, 12],), [12, 56, -4, 3, 74, -5, 20, 64, 34, 68, 66]),
    (([23, 37, 2, 60, 66, 56, 72, 13, 7, -9, 34, 72, 51, 49, 12, 40, 51],), [51, 40, 12, 49, 51, 72, 34, -9, 7, 13, 72, 56, 66, 60, 2, 37, 23]),
    (([16, 22, 41, 22, 40, 52, 61, 43, 40, 80, 65, 46, 48, 4, 25, 78, -3, 74],), [74, -3, 78, 25, 4, 48, 46, 65, 80, 40, 43, 61, 52, 40, 22, 41, 22, 16]),
]

tester = Test(challenge_method, tests, challenge_module)
