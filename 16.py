import time

def test():
    a = str(2**1000)
    sum =0
    for i in range(len(a)): sum += int(a[i])
    print(sum)
if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
