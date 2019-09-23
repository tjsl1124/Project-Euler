import time

def test():
    a=1
    b=1
    c = 1000-a-b

    for a in range (1, 998):
        for b in range (1,500):
            c = 1000 - a - b
            if (a*a + b*b) == (c*c): abc = a*b*c ; print(abc); return 0


if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
