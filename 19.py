import time

def test():
    count_s =0
    l=7
    for y in range (1900,2001):
        if y%400==0: #윤달
            count, l = day(29,l)
            count_s += count
        elif y%100==0 and y%400!=0: #윤달 아님
            count, l = day(28, l)
            if y!= 1900 :count_s += count
        elif y%4==0 : #윤달
            count, l = day(29,l)
            count_s += count
        else : #윤달아님
            count, l = day(28, l)
            count_s += count
        print(count_s)

def day(n,l):
    count =0
    for m in range(1,13):
        if m == 4 or m == 6 or m == 9 or m == 11 : d=30
        elif m == 2:d =n
        else: d=31
        if l == 1 : count+=1
        # print(m,count, l)
        if (d-(l+21))>7 :l=7-(d-(l+28))
        else:l=7-(d-(l+21))
    return count,l



if __name__ == "__main__":
    start = time.time()
    test()
    print("time :", time.time() - start)

