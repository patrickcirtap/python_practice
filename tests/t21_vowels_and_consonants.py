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
    (("hello world",), (3, 7)),
    (("t",), (0, 1)),
    (("variegated monstera",), (8, 10)),
    (("can you get this one correct",), (9, 14)),
    (("",), (0, 0)),
    (("vietnam and slovenia are the best countries in the world",), (19, 28)),
    ((" a a a a a e e e e i i i o o u",), (15, 0)),
    (("            more                       words",), (3, 6)),
    (("ennzqp oi wefuih jrwbchuoiwetnj    wbpiqehdk jhtihsd    fhstrhs djbr",), (13, 42)),
]

tester = Test(challenge_method, tests, challenge_module)
