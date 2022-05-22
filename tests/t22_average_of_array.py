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
    (([1, 2, 3, 4],), 2.5),
    (([69, 69, 69, 420, 420, 420],), 244.5),
    (([0],), 0),
    (([66, 100, 317, 384, 438, 517, 583, 742, 763, 838, 867, 915, 975, 999, 999, 999],), 656.375),
    (([10, 20, 30, 40, 50, 60, 70, 80, 90],), 50),
    (([639, -988, 585, 900, 190, -127, 236, -599, 563, 194, 864, -804, -800, 731, -475, 824, -17, -100, 334, 582],), 136.6),
    (([-8577, -6368, -7570, -2217, -38, -647, -9502, -1656, -8910, -1472, -7399, -5308, -3248, -9382, -424, -1281, -4938, -9525, -1979, -9860],), -5015.05),
]

tester = Test(challenge_method, tests, challenge_module)
