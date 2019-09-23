import time

def test():
    a={i**j for i in range (2,101) for j in range (2, 101)}
    print(len(a))
if __name__ == "__main__":
    start = time.time()
    test()

    print("time :", time.time() - start)
        # a= {}
        # for i in range (0,10):
        #     a.append(i)
        # print(a)
        #
        # a = [i if i % 2 == 0 else 'a' for i in range(1,11) for j in range()]
        # print(a)
        # b = {str(i+1):i for i in range(1,11)}
        # print(a)
        # print(b)


