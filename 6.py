import time

def test():
    sum_s=0
    sum=0

    for i in range (1,101):
        sum_s += i*i
        sum += i
    s_sum = sum*sum

    sum =s_sum - sum_s
    print(sum)



if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
