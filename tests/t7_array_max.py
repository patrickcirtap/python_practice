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
    (([1, 2, 3, 4],), 4),
    (([-1, -2, -3, -4],), -1),
    (([0],), 0),
    (([234, 479],), 479),
    (([353, -115, 264, -148, 55, -238, -444, 135, 112, -137, -182, 504, -312, 503],), 504),
    (([-225, 257, -258, -215, -380, -27, 465, -368],), 465),
    (([40, 417, 509, 62],), 509),
    (([102, 134, 404, -400, -394, -327, 299, -251, 498, 417, -448, -329, 121, -395],), 498),
    (([488, 207, 134, -269, -101, 120, -381, -46, 170, -128, 513, -295, -303],), 513),
    (([-81, -111, 12, 481, -252, 462, 71, 339, -292, -289],), 481),
    (([-173, -350, 36, -70, 418],), 418),
    (([530, 48, -192, 190, -58, -297, 374, -219, 17, 384, 188],), 530),
    (([315, -213, 501, -11, 55, -453, -251, -33, -118, 454, 309],), 501),
]

tester = Test(challenge_method, tests, challenge_module)
