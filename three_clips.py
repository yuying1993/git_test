# coding:utf-8
# @Time : 2018/5/7 15:58
# @Author : yuy
class Program(object):
    def __init__(self):
        pass

    def do(self):
        for i in range(1000):
            print(i)
            if i % 3 == 0:
                print("3 booms")
            if i % 5 == 0:
                print("5 booms")
            if i % 7 == 0:
                print("7 booms")

if __name__ == "__main__":
    sol = Program()
    sol.do()