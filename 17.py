import time

def test():
    a = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100:'hundred',1000:'thousand'}

    sum_=0
    for i in range (1,1001):
        if i/10 < 1 : sum_+=len(a[i]) #한자리수 구분
        elif i/100<1 and i/10 >=1 : #두자리수
            if i in a: sum_+=len(a[i]) #dic 안에 있는것들
            else :
                d=int(i%10) #1의자리
                t=i-d #10의자리
                sum_+=len(a[t])
                sum_+=len(a[d])
        else:#세자리수랑 1000
            if i == 1000 : sum_+=len(a[i]) + len(a[1])# 1000
            else :
                h=int(i/100) #100의자리
                sum_ += len(a[h])
                sum_ += len(a[100])
                if int(i%100)!=0 : sum_+= 3 #and
                n=int(i%100)
                if n in a: sum_ += len(a[n])  # dic 안에 있는것들
                else:
                    d = int(n% 10)  # 1의자리
                    t = n - d  # 10의자리
                    if t!=0 : sum_ += len(a[t])
                    if d!=0 :sum_ += len(a[d])

    print(sum_)
if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)
