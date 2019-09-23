import time

def test():
    '''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

    num = 2000000
    sum=0
    a=[True] * num
    for i in range (2,int(num**0.5)+1):
        if (a[i] ==True):
            for j in range(i*i, num, i):
                a[j] =False

    for i in range (2,num):
        if(a[i] == True):
            sum+=i


    print(sum)


if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
