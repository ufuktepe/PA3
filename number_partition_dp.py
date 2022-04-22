
def number_partition_dp(A, b):
    n = len(A)
    b_half = b // 2

    D = [[False for j in range(b_half + 1)] for i in range(n + 1)]
    C = [[None for j in range(b_half + 1)] for i in range(n + 1)]
    K = [None for j in range(b_half + 1)]

    for i in range(n + 1):
        D[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, b_half + 1):
            a_i = A[i - 1]
            if a_i > j:
                D[i][j] = D[i - 1][j]
                C[i][j] = C[i - 1][j]
            else:
                D[i][j] = D[i - 1][j] or D[i - 1][j - a_i]
                if D[i - 1][j - a_i]:
                    C[i][j] = a_i
                    K[j] = a_i
                else:
                    C[i][j] = C[i - 1][j]



    for j in range(b_half, -1, -1):
        if D[n][j]:
            return D, C, K, b - 2*j

def reconstruct(C, A, j, i, K):
    A1 = []
    A_test = []
    while j > 0:
        x = C[i][j]
        y = K[j]
        A1.append(x)
        A_test.append(y)
        j = j - x
        i = i - 1
    return A1


def sum_up(A):
    total = 0
    for x in A:
        total += x
    return total


if __name__ == '__main__':
    A = [2, 12, 2, 6, 8, 15, 9]
    print(f'Sum: {sum_up(A)}')
    b = sum_up(A)
    D, C, K, u = number_partition_dp(A, b)

    print(f'Residue: {u}')

    j = (b - u) // 2

    A1 = reconstruct(C, A, j, len(A), K)
    A2 = []
    for x in A1:
        for k in range(len(A)):
            if x == A[k]:
                del A[k]
                break

    A1_sum = sum_up(A1)
    A2_sum = sum_up(A)

    print(f'{A1_sum} {A1}')
    print(f'{A2_sum} {A}')