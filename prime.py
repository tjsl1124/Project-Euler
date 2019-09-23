import time

def test():
    num = 100
    a=[True] * num
    for i in range (2,int(num**0.5)+1):
        if (a[i] ==True):
            for j in range(i*i, num, i):
                a[j] =False

    for i in range (2,num):
        if(a[i] == True):
            print(i)


if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
