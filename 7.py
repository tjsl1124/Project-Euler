import time

def test():
    count =1
    num = 3
    while count<10001:
        prime = True
        for i in range(3,int(num**0.5)+1,2):
            if num % i ==0:
                prime =False
                break
        if prime == True: count+=1
        num+=2
    print(num-2)

if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)

