import time

def test():
    sum_a=0
    for k in range (2,(9**5)*6):
        n=str(k)
        a = []
        for i in range(0, len(n)):
            a.append(int(n[i:i+1]))
        sum_ = 0
        for j in range(len(a)):
            sum_ += int(a[j])**5
        if sum_== k : sum_a = sum_a+sum_
    print(sum_a)



if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)

