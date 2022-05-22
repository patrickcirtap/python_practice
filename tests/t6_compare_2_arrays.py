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
    (([1, 2, 3, 4], [1, 2, 3, 4]), True),
    (([1, 2, 3], [1, 3, 2]), False),
    (([10, 20, 50], []), False),
    (([], []), True),
    (([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]), True),
    (([9, 7, 5, 3, 1], [1, 3, 5, 7, 9]), False),
    (([69, 69, 69, 69, 69], [69, 69, 69, 69, 69]), True),
    (([83, 13, 59, 80, 68, 46], [65, 75, 76, 25, 11, 22]), False),
    (([55, 45, 28], [82, 89, 53, 44, 92]), False),
    (([2, 5, 84, 49, 75, 84, 75, 87, 24, 42], [45, 33, 71, 48, 19, 72, 24, 16, 38, 31]), False),
    (([62, 98, 36, 57, 28, 81, 7, 4, 37, 71, 97, 53, 41], [93, 34, 24, 48, 35, 68, 54, 13, 96]), False),
    (([69, 10, 31, 61, 45, 14, 49, 68], [60, 76, 33]), False),
    (([58, 23, 39, 60, 38, 33, 2, 52, 82, 85, 56], [100, 82, 13, 100, 99, 83, 35, 52, 48, 33, 21, 54, 81, 34]), False),
    (([15, 23, 43, 79, 50, 16, 13, 87], [21, 30, 71, 74, 12, 54, 60, 13, 77, 48, 43, 6, 13, 96]), False),
    (([37, 3, 73, 49, 11, 27, 46], [55, 70, 98, 16, 100, 37, 35]), False),
    (([30, 28, 39, 78, 53, 61, 39, 34, 53, 10, 14, 39, 58, 43], [61, 69, 58, 40, 60, 68, 2]), False),
    (([54, 48, 25, 78, 67, 46], [41, 96, 42]), False),
]

tester = Test(challenge_method, tests, challenge_module)
