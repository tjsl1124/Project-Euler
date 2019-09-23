import time

def test():
    count =0
    a=""
    i=1

    while count<15:
        a=a+str(i)
        count+=len(str(i))
        i+=1
    count = count-15
    print(count)
    num =str(i)
    print(a, num[count])




if __name__ == "__main__":
    start = time.time()
    test()

    print("time :", time.time() - start)