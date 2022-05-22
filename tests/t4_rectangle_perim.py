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
    ((4, 2), 12),
    ((5.5, 9.45), 29.9),
    ((0.5, 0.5), 2),
    ((40, 25), 130),
    ((63.0483, 56.41), 238.9166),
    ((46, 32), 156),
    ((64.186069, 71.245), 270.862138),
    ((44, 33), 154),
    ((127.899, 78.90194562), 413.60189124),
    ((105.086646546, 39.2748256881), 288.7229444682),
    ((6, 31), 74),
    ((29.7, 39.7666002), 138.9332004),
    ((49, 8), 114),
    ((116.2456894249, 84.7604470239), 402.0122728976),
    ((99.96183, 100.464609552), 400.852879104),
]

tester = Test(challenge_method, tests, challenge_module)
