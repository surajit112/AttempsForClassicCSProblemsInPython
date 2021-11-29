def fibb(n: int) -> int:
    """Fibbonacci using Recurssion

    Args:
        n (int): [position for fibbonnacci series]

    Returns:
        int: [nth fibbonacci number]
    """
    if n < 2:
        return n
    return fibb(n - 1) + fibb(n - 2)


if __name__ == "__main__":
    print(fibb(8))
