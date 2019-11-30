import os
import shutil
import random
from geekgap_contest._1_contest_30_Nov_2019.fast_fibonacci.solution import fast_fibonacci

TEST_CASES_DIR = './test_cases'
INPUTS_DIR = f'{TEST_CASES_DIR}/input'
OUTPUTS_DIR = f'{TEST_CASES_DIR}/output'


def save_input_case(case_id, *inputs):
    with open(f'{INPUTS_DIR}/input{case_id}.txt', 'w') as fp:
        for el in inputs:
            fp.write(f'{el}\n')


def save_output_case(case_id, *outputs):
    with open(f'{OUTPUTS_DIR}/output{case_id}.txt', 'w') as fp:
        for el in outputs:
            fp.write(f'{el}\n')


def main():
    os.makedirs(INPUTS_DIR, exist_ok=True)
    os.makedirs(OUTPUTS_DIR, exist_ok=True)

    def handle_case(*_, **params):
        case_id = params['case_id']
        a = params['a']

        res = fast_fibonacci(a)

        save_input_case(case_id, a)
        save_output_case(case_id, res)

    # autogenerated test cases
    for i in range(40):
        case_id = "{:02d}".format(i)
        handle_case(case_id=case_id, a=i)

    # zip the test cases folder
    shutil.make_archive(TEST_CASES_DIR, 'zip', TEST_CASES_DIR)


if __name__ == '__main__':
    main()