def permutationEquation(p):
    # Write your code here
    lenOfP = len(p)
    i = 1
    y = []
    while (i <= lenOfP):
        first_index = p.index(i) + 1
        secend_index = p.index(first_index) + 1
        y.append(secend_index)
        i += 1
    return y


if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))



