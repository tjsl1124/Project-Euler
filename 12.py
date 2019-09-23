import time

def test():
    number =1
    sum_=0
    num =500
    c=0
    while c< num:
        sum_= sum_+number
        c=1
        for i in range (2,int(sum_**0.5)+1):
            if sum_%i ==0:
                if sum_**0.5 == sum_/i : c+=1
                else: c+=2
        number+=1

    print(sum_)



if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)

