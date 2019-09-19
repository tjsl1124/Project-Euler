import time
import openpyxl

def test():
    n = 600851475143
    # num = int(n ** 0.5)+1
    i =3
    while i<n :
        if n%i ==0 :  n=n/i
        else :i+=2
    print(i)

if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)

