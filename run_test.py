import copy
import glob
import os
import sys
import time
import traceback

# Text styles for printing test results to terminal
TEXT_RED    = "\033[91m"
TEXT_GREEN  = "\033[92m"
TEXT_YELLOW = "\033[93m"
TEXT_BOLD   = "\033[1m"
TEXT_END    = "\033[0m"

class Test:
    def __init__(self, method, tests, module_name):
        self.num_passed = 0
        self.num_failed = 0
        self.tests_run = 0
        self.sleep_time = 0

        self.module_name = module_name
        self.run_all_tests(method, tests)
    
    def run_all_tests(self, method, tests):
        # Tests take between [1.5, 5] seconds to run
        self.sleep_time = min(1.5, 5/len(tests))

        for test in tests:
            self.run_test(method = method,
                          params = test[0],
                          expected_result = test[1])
        
        self.tests_done()

    def run_test(self, method, params, expected_result):
        self.tests_run += 1
        orig_params = copy.deepcopy(params)
        # Params must be un-packed as different methods have different parameters
        try:
            result = method(*params)

            if(result == expected_result):
                self.test_pass()
            else:
                self.test_fail(params = orig_params, result = result, expected_result = expected_result)
        except Exception:
            self.test_fail(params = orig_params, result = "Error", expected_result = expected_result)
            print()
            print(traceback.format_exc())
        
        time.sleep(self.sleep_time)

    def test_pass(self):
        print(f"{TEXT_GREEN}Test {self.tests_run} passed{TEXT_END}")

    def test_fail(self, params, result, expected_result):
        print(f"{TEXT_RED}{TEXT_BOLD}Test {self.tests_run} failed{TEXT_END}")
        # Print params tuple elements
        print(f"    Test input:      ", end="")
        for i in range(len(params)):
            if(i < len(params)-1):
                print(f"{params[i]}, ", end="")
            else:
                print(params[i])
        print(f"    Expected result: {expected_result}")
        print(f"    Your result:     {result}")
        
        print(f"\n{TEXT_YELLOW}See test output above{TEXT_END}")

        sys.exit(1)

    def tests_done(self):
        print(f"\n{TEXT_GREEN}{TEXT_BOLD}Success - You passed all the tests{TEXT_END}")
        print(f"{TEXT_YELLOW}{TEXT_BOLD}Challenge: {self.module_name}{TEXT_END}")

        # Rename challenge file to DONE
        # Split up to first '_' and add DONE inbetween
        test_file_DONE_name = self.module_name.split("_", 1)[0] + "_DONE_" + self.module_name.split("_", 1)[1] + ".py"
        os.rename(f"{self.module_name}.py", test_file_DONE_name)


if __name__ == "__main__":
    # Get challenge number to test
    if(len(sys.argv) != 2):
        print("One (1) argument required")
        sys.exit(1)
    try:
        challenge_num = int(sys.argv[1])
    except Exception as e:
        print(f"Argument must be an integer: {e}")
        sys.exit(1)

    # Look for corresponding test file in directory
    # Format for test N will be tN_xyz.py
    matching_tests = glob.glob(f"tests/t{challenge_num}_*.py")
    if(len(matching_tests) != 1):
        print(f"Error locating challenge test: {challenge_num}")
        sys.exit(1)
    # Now have the test file for this challenge
    test_file = matching_tests[0]

    # Execute the test file
    # Try-catch not needed here - run_test() does check
    exec(open(test_file).read())
