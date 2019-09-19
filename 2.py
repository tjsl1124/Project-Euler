import time

def test():
    num =[1,2]; sum=2;  i=0
    while num[i]<= 4000000:
        num.append(num[i]+num[i+1])
        if num[i+2] %2 ==0: sum+=num[i+2]
        i+=1
    print('%d' %(sum))



if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
