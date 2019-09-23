import time

def digit(a):
    arr=[]
    arr=str(a)
    n = len(arr)+1
    return n


def test():
    a=1 ; b=1 ; c=a+b ;  n=3 ; term = 1001 ; f=c
    while(digit(f)!=term):
        n += 1 ;  a=b+c ;  f=a
        if(digit(a)==term) : print(n) ; break

        n += 1 ; b=c+a ; f = b
        if (digit(b) == term): print(n) ; break

        n+=1 ; c=a+b ;  f = c
        if (digit(c) == term):print(n) ;  break



if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
