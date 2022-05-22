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
    ((1, ), 365),
    ((4, ), 1460),
    ((43.21, ), 15771),
    ((87.654321, ), 31993),
    ((51, ), 18615),
    ((56.687755, ), 20691),
    ((80, ), 29200),
    ((3.826643096, ), 1396),
    ((104, ), 37960),
    ((15.3769073, ), 5612),
    ((105, ), 38325),
    ((101.6, ), 37084),
    ((87, ), 31755),
    ((84.92, ), 30995),
    ((99, ), 36135),
    ((114.112, ), 41650),
    ((64, ), 23360),
    ((31.8108117, ), 11610),
    ((97, ), 35405),
    ((49.72920791, ), 18151),
    ((8, ), 2920),
    ((51.5, ), 18797),
    ((110, ), 40150),
    ((42.8351954545, ), 15634),
    ((110, ), 40150),
    ((83.4485936, ), 30458),
    ((91, ), 33215),
    ((114.8625679, ), 41924),
    ((8, ), 2920),
    ((67.614, ), 24679),
    ((86, ), 31390),
    ((52.0, ), 18980),
    ((23, ), 8395),
    ((63.0, ), 22995),
    ((78, ), 28470),
    ((81.412, ), 29715),
    ((24, ), 8760),
    ((27.0595, ), 9876),
    ((96, ), 35040),
    ((30.14694, ), 11003),
    ((118, ), 43070),
    ((116.8178, ), 42638),
    ((73, ), 26645),
    ((13.813844, ), 5042),
]

tester = Test(challenge_method, tests, challenge_module)
