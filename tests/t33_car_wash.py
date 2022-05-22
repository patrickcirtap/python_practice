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
    (({"type": "sedan", "brand": "mitsubishi", "colour": "black"}, ), 118),
    (({"type": "sport", "brand": "audi",       "colour": "white"}, ), 502.5),
    (({"type": "suv",   "brand": "range rover","colour": "grey"}, ), 180),
    (({"type": "coupe", "brand": "toyota",     "colour": "pink"}, ), 29),
    (({"type": "van",   "brand": "pedo van",   "colour": "green"}, ), 217.56),
    (({"type": "truck", "brand": "ferrari",    "colour": "variegated"}, ), 224.25),
    (({"type": "sport", "brand": "nissan",     "colour": "black"}, ), 328),
    (({"type": "sedan", "brand": "subaru",     "colour": "white"}, ), 125),
    (({"type": "suv",   "brand": "porsche",    "colour": "pink"}, ), 166.5),
    (({"type": "coupe", "brand": "lamborghini","colour": "orange"}, ), 147),
    (({"type": "van",   "brand": "tesla",      "colour": "purple"}, ), 333),
    (({"type": "sport", "brand": "ford",       "colour": "variegated"}, ), 157.5),
    (({"type": "sedan", "brand": "audi",       "colour": "green"}, ), 154.35),
]

tester = Test(challenge_method, tests, challenge_module)
