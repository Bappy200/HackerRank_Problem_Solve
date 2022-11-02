def arrayRotation(a, k):
    #first solve
    # lenOfa = len(a)
    # # a[0],a[1] = a[lenOfa - 1], a[0]
    # for i in range(k):
    #     temp = a[0]
    #     print("for in = ",a)
    #     for j in range(1, lenOfa):
    #         if j == lenOfa - 1:
    #             a[0] = a[lenOfa - 1]
    #         a[j], temp = temp, a[j]

    #secedn solve
    # rotadeList = a[:]
    # for i in range(k):
    #     rotadeList = rotadeList[-1:] + rotadeList[:-1]

    #3rd solve
    updateList = a[:]
    lenOfa = len(a)
    for i in range(0, lenOfa):
        index = (i+k) % lenOfa
        updateList[index] = a[i]

    return updateList


def circularArrayRotation(a, k, queries):
    # Write your code here
    finalList = arrayRotation(a, k)

    result = []
    for i in queries:
        result.append(finalList[i])

    return result


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print(result)
