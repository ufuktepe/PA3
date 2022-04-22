from max_heap import MaxHeap
import random
import time

MAX_ITER = 100

def kk(a):
    H = MaxHeap(a)
    n = len(a)

    for i in range(n-1):
        x = H.extract_max()
        y = H.extract_max()
        d = x - y
        H.insert(d)

    u = H.extract_max()
    return u


def generate_solution(n):
    return [random.randrange(-1, 2, 2) for s in range(n)]


def generate_prepartition(n):
    return [random.randrange(n) for p in n]


def calc_residue(a, solution):
    return abs(sum([a_i * s_i for a_i, s_i in zip(a, solution)]))


def calc_residue_pp(a, solution, n):
    a_p = [0] * n
    for i in range(n):
        a_p[solution[i]] += a[i]

    a_p = [i for i in a_p if i != 0]
    return kk(a_p)


def repeated_random_std(a):
    n = len(a)
    solution = generate_solution(n)
    residue = calc_residue(a, solution)
    for i in range(MAX_ITER):
        new_solution = generate_solution(n)
        new_residue = calc_residue(a, new_solution)
        if new_residue < residue:
            residue = new_residue

    return residue


def repeated_random_pp(a):
    n = len(a)
    solution = generate_prepartition(n)
    residue = calc_residue_pp(a, solution, n)
    for i in range(MAX_ITER):
        new_solution = generate_prepartition(n)
        new_residue = calc_residue_pp(a, new_solution, n)
        if new_residue < residue:
            residue = new_residue

    return residue




if __name__ == '__main__':
    # a = []
    # for i in range(7):
    #     x = random.randint(1, 25)
    #     a.append(x)
    # print(a)
    # print(kk(a))

    a = []
    for i in range(100):
        a.append(random.randint(1, 10 ** 12))

    print(repeated_random_std(a))

