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
    (("hello world", 'o'), 2),
    (("expensive variegated monstera", 'e'), 6),
    (("", 'k'), 0),
    (("pink princess", 'p'), 2),
    (("banana is a fruit", 'c'), 0),
    (("qwertyuiop", 'f'), 0),
    (("gotta catch em all", 'a'), 3),
    (("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm", 'm'), 33),
    (("supercalifragilisticexpialidocious", 'i'), 7),
    (("abcdefghijklmnopqrstvwxyz", 'u'), 0),
    (("abcdefghijklmnopqrstuvwxyz", 'u'), 1),
    (("foobar", 'z'), 0),
]

tester = Test(challenge_method, tests, challenge_module)
