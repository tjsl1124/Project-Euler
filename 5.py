import time
import openpyxl

def test():
    num =20 ; a=[0]*num ;mul=1
    for i in range (2,num):
        n=i
        for k in range (2,i) :
            count =0
            while n%k==0 :
               n=int(n/k)
               count+=1

            if a[k-1] < count : a[k-1] += (count-a[k-1])

        a[n-1]+=1



    for i in range(1,len(a)):
        if a[i]!=0:
            mul *= ((i+1)**a[i])



    print( mul)


if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)

