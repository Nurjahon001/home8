def minimumPerimeter(neededApples):
    def numApples(k):
        return 2 * k * (k + 1) * (2 * k + 1)

    for k in range(1, 100_000):
        if numApples(k) >= neededApples:
            return k * 8
    return -1

print(minimumPerimeter(1))
