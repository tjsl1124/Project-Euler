import time

def test():
    mul=1
    for i in range(1,101): mul =mul * i

    a = str(mul) ;  sum = 0

    for i in range(len(a)): sum += int(a[i])
    print(sum)
if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
