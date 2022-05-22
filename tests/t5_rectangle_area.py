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
    ((4, 2), 8),
    ((0.5, 0.5), 0.25),
    ((19, 33), 627),
    ((99.6910475443, 41.061), 4093.4141032165026),
    ((11, 42), 462),
    ((112.99462059, 47.45911), 5362.624127989075),
    ((6, 39), 234),
    ((113.9243720216, 121.7088903), 13865.608896873304),
    ((49, 45), 2205),
    ((119.21, 69.0), 8225.49),
    ((4, 49), 196),
    ((70.3, 39.2383761623), 2758.45784420969),
    ((111.1238853, 4.7), 522.28226091),
    ((100.83624, 84.7155166572), 8542.394169369418),
]

tester = Test(challenge_method, tests, challenge_module)
