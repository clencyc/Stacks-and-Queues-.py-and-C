class Sum:
    @staticmethod
    def getsum(*args):
        add = 0
        for i in args:
            add += i
        return add


def main():
    print("Sum :", Sum.getsum(1, 2, 3, 4, 5))


main()
