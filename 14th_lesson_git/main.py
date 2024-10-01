def demo_example():
    # TODO...
    # WIP.... work in progress

    pass


def demo_zip():
    values1 = list(range(2, 10))
    values2 = list(range(3, 19, 3))
    print(values1)
    print(values2)
    for v1, v2 in zip(values1, values2):
        print("v1 = ", v1, "v2 = ", v2, "sum = ", v1 + v2)

def main():
    # print("Hello_main")
    demo_zip()

if __name__ == '__main__':
    main()

