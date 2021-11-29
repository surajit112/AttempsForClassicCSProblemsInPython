def fibb(n: int) -> int:
    """Fibbonacci Number

    Args:
        n ([int]): [position fibbonacci number]

    Returns:
        [int]: [nth fibbonacci number]
    """
    num = [0, 1]
    if n >= 2:
        for i in range(2, n):
            number = num[i - 1] + num[i - 2]
            num.append(number)
        return num[-1]
    else:
        if n == 1:
            return 1
        else:
            return 0


if __name__ == "__main__":
    print(fibb(9))
