import time


def test():
    """https://projecteuler.net/problem=15"""

    num=20
    a = [[1] * (num+1)] * (num+1)

    for i in range(1, num+1):
        for j in range(1, num+1):
            a[i][j] = a[i - 1][j] + a[i][j - 1]

    print(a)


if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
