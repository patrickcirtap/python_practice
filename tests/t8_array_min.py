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
    (([1, 2, 3, 4],), 1),
    (([-1, -2, -3, -4],), -4),
    (([0],), 0),
    (([354, 219],), 219),
    (([-138, -443, 321, 205, -456, -35, -80, -23, 267],), -456),
    (([559, 491, 506, 197, -310, -384, 548],), -384),
    (([-193, 303, -45],), -193),
    (([-6, 478, -111, -81, 250],), -111),
    (([-327, 520],), -327),
    (([32, -320, 383, 235, 397, 480, -26, -398, 175, -253, -395, -98, -248, 363, -50],), -398),
    (([35, -231, 129, -253, 45, 162, 423, -386, 299],), -386),
    (([173, 308, -242, 103, 380],), -242),
    (([-86, -232, -319, 232, 314, 452, 563, 305, -239, -262, 180, -137, -32, 315, 246],), -319),
]

tester = Test(challenge_method, tests, challenge_module)
