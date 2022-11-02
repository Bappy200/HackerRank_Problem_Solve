def viralAdvertising(n):
    # Write your code here
    cum = 2
    liked = 2
    i = 0
    while i < n:
        shared = liked * 3
        liked = shared // 2
        cum += liked
        i += 1
    return cum

    # if n <= 0:
    #     return 0;
    #
    # modulas = n // 2
    # liked = modulas
    # shared = (n - modulas) * 2
    # i = 1
    # print(liked, shared)
    #
    # while i < n:
    #     modulas = shared // 2
    #     print("modulas ", modulas, i)
    #     liked += modulas
    #     print("liked ", liked)
    #     print("1sheard ", shared)
    #     shared += modulas
    #     print("2sheard ", shared)
    #     i += 1
    #     print("")
    #
    #
    # return liked


if __name__ == '__main__':
    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)
