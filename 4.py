import time

def test():
    # a=[]
    # pa = False
    # num =1
    # for i in range (999,99,-1):
    #     for j in range (999,99,-1):
    #         a=str(i*j)
    #         k = 0
    #         while(k  <= int(len(a)/2)):
    #             if(a[k] == a[len(a)-1-k]) :
    #                 pa = True
    #             else:
    #                 pa = False
    #                 break
    #             k+=1
    #         if (pa == True):
    #             if( num < int(a)):
    #                 num = int(a)
    #             break
    #
    # print(num)

    a = [] ; b =[]; num=1
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            a = str(i * j);  b = a[::-1]
            if a==b:
                if num < int(a): num = int(a) ;break
 
    print(num)



if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
