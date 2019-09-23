import time

def test():
    n = [True]*28123
    for i in range (2,10000):
        sum1=0 ; sum2=0
        if(n[i-1] == True):
            for k in range (1,int(i**0.5)+1):
                if i%k ==0 :
                    sum1+=k
            for k in range (1,sum1):
                if i%k ==0 :
                    sum2+=k
            if(sum2 == i) :
                n[sum1-1] =False
                n[i-1] = False
    for i in range(len(n)):
        if n[i-1] == False : print(i)
    print(sum2)





if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)

