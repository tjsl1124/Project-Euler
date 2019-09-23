import time

def test():
    a=[5,4,7,4,8]
    sum2 =0
    for i in range (10000,100000):
            sum1 = 0

            a[0] = int(i/10000)
            a[1] = int(i % 10000/1000)
            a[2] = int (i %10000%1000/100)
            a[3] = int (i % 10000%1000%100/10)
            a[4] = int (i % 10000%1000%100%10)

            for j in range (0,5):
                sum1 += a[j]**4
            if( i == sum1) :
                print (sum1)
                sum2+=sum1
                print(sum2)


    print(a)
if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
