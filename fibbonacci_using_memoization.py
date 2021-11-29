# Cache
memo: dict[int, int] = {0: 0, 1: 1}


def fibb(n: int) -> int:
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibb(n - 1) + fibb(n - 2)
        return memo[n]


if __name__ == "__main__":
    for i in range(101):
        print(i, " : ", fibb(i))
