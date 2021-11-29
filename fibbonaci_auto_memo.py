from functools import lru_cache


@lru_cache(maxsize=None)
def fibb(n: int) -> int:
    if n < 2:
        return n
    else:
        return fibb(n - 1) + fibb(n - 2)


if __name__ == "__main__":
    for n in range(101):
        print(n, " : ", fibb(n))
