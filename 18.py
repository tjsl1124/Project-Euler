import time

def test():
    n = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    a = []
    b = []
    j=0

    for i in range(1,16): #피라미드 배열로 정리
        k = 0
        while(k<i):
            a.append(int(n[3*j:3*j+2]))
            k+=1
            j+=1
        b.append(a)
        a=[]


    sum_=0
    num =0
    for i in range(1,16):
        if i == 1:
            sum_ = b[i-1][num]
        elif i == 15:
            if b[i-1][num]>b[i-1][num+1] : sum_+=b[i-1][num+1]
            else :
                sum_+=b[i-1][num+1]
                num+=1
            print(sum_)

        # elif i == 15:
        #     print(sum_)
        #     break
        else : #한칸 아래와 두칸 아래의 합이 가장 큰 경로 추출
            c=[]
            c.append(b[i-1][num]+b[i][num])
            c.append(b[i-1][num] + b[i][num+1])
            c.append(b[i-1][num+1] + b[i][num+1])
            c.append(b[i-1][num+1] + b[i][num+2])
            max = c[0]
            for j in range(1,len(c)):
                if(c[j]>max) : max = c[j]

            if max == c[0] or max == c[1] :
                sum_+=b[i-1][num]
            else :
                num+=1
                sum_ += b[i - 1][num]








if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
