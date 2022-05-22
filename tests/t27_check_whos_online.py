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
    (([{"name": "Steve","status": "online"},
       {"name": "Alice","status": "offline"},
       {"name": "Bob","status": "online"}],), ["Bob", "Steve"]),

    (([{"name": "Steve","status": "online"},
       {"name": "Alice","status": "offline"},
       {"name": "Bob","status": "online"},
       {"name": "Sarah","status": "online"},
       {"name": "Erin","status": "online"},
       {"name": "Andy","status": "offline"}],), ["Bob", "Erin", "Sarah", "Steve"]),

    (([],), -1),

    (([{"name": "Betty","status": "offline"},],), -1),

    (([{"name": "Luke","status": "online"},
       {"name": "Vince","status": "offline"},
       {"name": "Gary","status": "offline"},
       {"name": "Jessica","status": "offline"},
       {"name": "Alex","status": "offline"},
       {"name": "Taylor","status": "offline"}],), ["Luke"]),

    (([{"name": "Jake","status": "offline"},
       {"name": "Amy","status": "offline"},
       {"name": "Boyle","status": "offline"},
       {"name": "Holt","status": "offline"},
       {"name": "Diaz","status": "offline"}],), -1),

    (([{"name": "Stan","status": "online"},
       {"name": "Kenny","status": "online"},
       {"name": "Kyle","status": "online"},
       {"name": "Cartman","status": "online"},
       {"name": "Mr. Garrison","status": "online"},
       {"name": "Randy","status": "online"},
       {"name": "Ike","status": "online"},
       {"name": "Wendy","status": "online"},
       {"name": "Butters","status": "online"}],), ["Butters", "Cartman", "Ike", "Kenny", "Kyle", "Mr. Garrison", "Randy", "Stan", "Wendy"]),
]

tester = Test(challenge_method, tests, challenge_module)
