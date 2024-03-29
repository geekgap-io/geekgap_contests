import os
import shutil
import random
from solution import last_occurrence_search

TEST_CASES_DIR = './test_cases'
INPUTS_DIR = f'{TEST_CASES_DIR}/input'
OUTPUTS_DIR = f'{TEST_CASES_DIR}/output'


def get_input():
    population = [random.randint(0, 20) for i in range(20)]
    A = sorted(random.choices(population=population, k=20))

    k_index = random.randint(0, 19)
    if k_index % 2 == 0:
        k = A[k_index]
    else:
        k = random.randint(10, 30)

    return A, k


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
        A = params['A']
        k = params['k']

        res = last_occurrence_search(A, k)

        A_str = ' '.join(str(el) for el in A)
        save_input_case(case_id, A_str, k)
        save_output_case(case_id, res)

    # autogenerated test cases
    for i in range(37):
        case_id = "{:02d}".format(i)
        A, k = get_input()
        handle_case(case_id=case_id, A=A, k=k)


    # the rest are created manually for edge cases
    i += 1
    handle_case(case_id="{:02d}".format(i), A=[], k=2)

    i += 1
    handle_case(case_id="{:02d}".format(i), A=[2], k=2)

    i += 1
    handle_case(case_id="{:02d}".format(i), A=[2], k=1)


    # zip the test cases folder
    shutil.make_archive(TEST_CASES_DIR, 'zip', TEST_CASES_DIR)


if __name__ == '__main__':
    main()