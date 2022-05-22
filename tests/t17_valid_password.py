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
    (("p@s$W0rd>>", ), True),
    (("p@s$W0rd>", ), False),
    (("", ), False),
    (("zX<%5kL{}12#", ), True),
    (("abc", ), False),
    (("^KZ]UB.P@n3)65", ), True),
    (("Q%kqMSB59rhvTX", ), False),
    (("Kuv:r9+)PZ(F(<", ), False),
    (("hbE?+W$#H", ), False),
    (("WSvSF@[Y8CQ+ML", ), True),
    (("@j@:`kqV!@/2[y=", ), True),
    (("$pP{4$pP{", ), False),
    (("6zGUAwcRwRx3%_=7?5", ), False),
    (("jY~Lnn9}{}{&AQqhj", ), True),
    (("-y39kr*sdJ+Z5D$u^3", ), False),
    (("l!<^>1I", ), False),
    (("ES$$8nr3d,QGb(", ), True),
    (("6s6=S", ), False),
    (("aaaaaaaaaaaaaaa><<><>><aadKZspL3TuD!=F:", ), True),
    (("KjYKG*enr&vCn6*sxc", ), False),
    (("123456", ), False),
    (("JBpbfH)aHC7_AaT<^>", ), True),
    (("dU6$y*W-5L6dvtq!D6", ), False),
]

tester = Test(challenge_method, tests, challenge_module)
