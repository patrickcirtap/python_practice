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
    ((0.5,), "infant"),
    ((0.0,), "infant"),
    ((0,), "infant"),
    ((95,), "this is getting out of hand"),
    ((51,), "old, eww"),
    ((1.5,), "toddler"),
    ((1.49,), "infant"),
    ((2.9,), "toddler"),
    ((5.5,), "child"),
    ((5.4,), "young child"),
    ((5.6,), "child"),
    ((11,), "adolescent"),
    ((13.1,), "teenager"),
    ((19.5,), "young adult"),
    ((21,), "the prime of your life"),
    ((20.1,), "young adult"),
    ((96,), "this is getting out of hand"),
    ((81,), "how are you still alive?"),
    ((23,), "the prime of your life"),
    ((103,), "the wind could kill you"),
    ((30,), "old, eww"),
    ((39,), "old, eww"),
    ((47,), "old, eww"),
    ((92,), "how are you still alive?"),
    ((4,), "young child"),
    ((56,), "mid-life, lol"),
    ((6,), "child"),
    ((108,), "the wind could kill you"),
    ((102,), "this is getting out of hand"),
    ((62,), "damn still going..."),
    ((94,), "how are you still alive?"),
]

tester = Test(challenge_method, tests, challenge_module)
