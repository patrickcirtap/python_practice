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
    (([1, 2, 3, 4],), 3),
    (([1, 3, 5, 7, 9, 0, 8, 6, 4, 2],), 9),
    (([0, 0],), 0),
    (([825, 101, 780, 446, 1179, 666, 1023, 1217, 31, 230, 733, 1020, 1181],), 1186),
    (([10, 277, 662, 1102, 651, 13, 427, 876, 278, 1071],), 1092),
    (([278, 380],), 102),
    (([172, 180, 16, 129, 208, 225, 800, 389, 278, 794, 982],), 966),
    (([160, 196, 562, 515, 1089, 539, 393, 775, 1170],), 1010),
    (([511, 143, 826, 481, 400, 8],), 818),
    (([0, 440, 972, 90, 663, 304, 292],), 972),
    (([516, 1212, 758, 502, 1141, 1229, 688],), 727),
]

tester = Test(challenge_method, tests, challenge_module)
