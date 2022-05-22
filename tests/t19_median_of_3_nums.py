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
    ((901, 326, 712), 712),
    ((85, 252, 856), 252),
    ((381, 469, 416), 416),
    ((919, 239, 860), 860),
    ((794, 195, 296), 296),
    ((-522.059128872146, 430.7833406673965, -606.4668897850052), -522.059128872146),
    ((-33.399654167336735, -544.3655456408475, -666.1463996894588), -544.3655456408475),
    ((869.6302630766288, -523.3852684351137, 397.3295399338158), 397.3295399338158),
    ((429.1601595735808, 346.2452291717382, -55.92839197182468), 346.2452291717382),
    ((-607.1891078645908, 13.6705464421143, -517.1270019693918), -517.1270019693918),
]

tester = Test(challenge_method, tests, challenge_module)
