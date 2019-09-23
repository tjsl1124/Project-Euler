import time

def test():
    p=[200,100,50,20,10,5,2,1]
    count=0
    num = 200
    sum_=num
    for i in range (0, len(p)):
        while(sum_<p[i]):
            sum_-=p[i]
            count+=1





if __name__ == "__main__":
    start = time.time()
    test()

    print("time :", time.time() - start)