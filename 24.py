import time


def test():
    dic_=[]
    n = 1000000
    mul_=1
    for a in range (10,1,-1):
        # for i in range (2,a+1):
        #     mul_=mul_*i
        while(mul_<n):
        if(mul_<n):
            dic_.append(int(n/mul_)-1)
        else :
            for i in range(2, a):
                mul_ = mul_ * i
    print(mul_)



if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)

