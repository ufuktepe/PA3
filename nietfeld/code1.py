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

def karmarkar_karp(input):
    h = []
    for x in input:
        heapq.heappush(h, -x)
    while len(h) > 1:
        a = abs(heapq.heappop(h))
        b = abs(heapq.heappop(h))
        dist = abs(a - b)
        heapq.heappush(h, dist)
    return heapq.heappop(h)

def main():
    # check usage
    if len(sys.argv) is not 2:
        print("usage: python my_kk.py input.txt")
        sys.exit()

    input = readInput("input.txt")
    residue = karmarkar_karp(input)

    print(residue)



if __name__ == "__main__":
    main()