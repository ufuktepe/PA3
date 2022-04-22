
from utils import *
import sys
import math
import heapq
import operator
import time
max_iter = 25000


def generate_solution(input):
    # get a random solution and calculate its residual
    solution = [x * random.randrange(-1, 2, 2) for x in input]
    residual = sum(solution)
    return solution, residual


def generate_prepartition(input):
    k = len(input)
    partition = [random.randint(1, k) for x in range(k)]
    solution = [0 for x in range(k)]
    # combine elements with same value in partition
    for i in range(k):
        solution[partition[i] - 1] += input[i]
    solution = filter(lambda x : x != 0,  solution)
    return solution


def karmarkar_karp(input, prepartition):
    t0 = time.clock()
    # check if should prepartition
    if prepartition:
        input = generate_prepartition(input)
    h = []
    for x in input:
        heapq.heappush(h, -x)
    while len(h) > 1:
        a = abs(heapq.heappop(h))
        b = abs(heapq.heappop(h))
        dist = abs(a - b)
        heapq.heappush(h, dist)
    return heapq.heappop(h), time.clock() - t0


def repeated_random(input, prepartition):
    t0 = time.clock()
    # check if should prepartition
    if prepartition:
        input = generate_prepartition(input)

    # get a random solution and calculate its residual
    solution, residual = generate_solution(input)
    residual = abs(residual)

    # try to find better solutions
    iterations = max_iter
    while iterations > 0 and residual > 0:
        # find new solution
        new_solution = [x * random.randrange(-1, 2, 2) for x in input]
        new_residual = abs(sum(new_solution))
        # check if solution is better
        if new_residual < residual:
            residual = new_residual
        iterations -= 1
    return residual, time.clock() - t0


def hill_climbing(input, prepartition):
    t0 = time.clock()
    # check if should prepartition
    if prepartition:
        input = generate_prepartition(input)

    # get a random solution and calculate its residual
    solution, residual = generate_solution(input)

    # length of the input and number of iterations
    length = len(input)
    iterations = max_iter

    # try to find better solutions
    while iterations > 0 and abs(residual) > 0:
        # pick two different indices
        [i, j] = random.sample(range(length), 2)
        # flip sign of first index
        new_residual = residual - 2 * solution[i]
        # flip sign of second with 0.5 probability
        sign = random.randrange(-1, 2, 2)
        new_residual = new_residual - 2 * solution[j] if sign == -1 else new_residual
        # if the new residual is better, update solution
        if abs(new_residual) < abs(residual):
            solution[i] *= -1
            solution[j] *= sign
            residual = new_residual
        iterations -= 1
    return abs(residual), time.clock() - t0

def T(iter):
    return (10 ** 10) * (0.8 ** math.floor(iter / 300.))

def annealing(input, prepartition):
    t0 = time.clock()
    # check if should prepartition
    if prepartition:
        input = generate_prepartition(input)

    # get a random solution and calculate its residual
    solution, residual = generate_solution(input)

    # length of the input, number of iterations and S''
    length = len(input)
    iterations = max_iter
    best_solution = list(solution)

    # try to find better solutions
    while iterations > 0 and abs(residual) > 0:
        # pick two different indices
        [i, j] = random.sample(range(length), 2)
        # flip sign of first index
        new_residual = residual - 2 * solution[i]
        # flip sign of second with 0.5 probability
        sign = random.randrange(-1, 2, 2)
        new_residual = new_residual - 2 * solution[j] if sign == -1 else new_residual
        # if the new residual is better, update solution
        if abs(new_residual) < abs(residual):
            solution[i] *= -1
            solution[j] *= sign
            residual = new_residual
        else:
            # probability of moving
            distance = abs(new_residual) - abs(residual)
            t_iter = T(max_iter - iterations + 1)
            probability = math.exp(-distance/t_iter)
            if random.random() <= probability:
                solution[i] *= -1
                solution[j] *= sign
        if abs(residual) < abs(sum(best_solution)):
            best_solution = list(solution)

        iterations -= 1
    return abs(residual), time.clock() - t0

def main():
    # check usage
    if len(sys.argv) is not 3:
        print("usage: python my_kk.py array_size prepartition (e.g., python my_kk.py 100 0)")
        sys.exit()
    # convert command line arguments
    k = int(sys.argv[1])
    prepartition = int(sys.argv[2])

    kk = []
    rr = []
    hc = []
    sa = []
    kk_t = 0
    rr_t = 0
    hc_t = 0
    sa_t = 0

    tests = 50
    print("Minimum Residue Problem by Elk Inc.\n\nTesting...")
    for i in range(tests):
        print("Test number " + str(i + 1))
        generate_nums(k)
        input = readInput("input.txt")
        residue, t1 = karmarkar_karp(input, prepartition)
        kk.append(residue)
        kk_t += t1
        residue, t1 = repeated_random(input, prepartition)
        rr.append(residue)
        rr_t += t1
        residue, t1 = hill_climbing(input, prepartition)
        hc.append(residue)
        hc_t += t1
        residue, t1 = annealing(input, prepartition)
        sa.append(residue)
        sa_t += t1

    # print results in ranking order
    ranking = {"Karmarkar-Karp": sum(kk)/tests, "Repeated random": sum(rr)/tests, "Hill climbing": sum(hc)/tests, "Simulated annealing": sum(sa)/tests}
    ranking = sorted(ranking.iteritems(), key=operator.itemgetter(1))

    print("Results in decreasing performance order")
    for method in ranking:
        print(method[0] + ": " + str(method[1]))

    print("\nKarmarkar-Karp (average of " + str(kk_t/tests) + " seconds):\n")
    print(kk)
    print("\nRepeated random (average of " + str(rr_t/tests) + " seconds):\n")
    print(rr)
    print("\nHill climbing (average of " + str(hc_t/tests) + " seconds):\n")
    print(hc)
    print("\nSimulated annealing (average of " + str(sa_t/tests) + " seconds):\n")
    print(sa)



if __name__ == "__main__":
    main()