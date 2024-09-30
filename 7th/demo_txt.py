# FILE_PATH = "file.txt"

def main():
    # f = open(FILE_PATH, "w")
    # f.write("HI\n")
    # f.close()

    # with open("file.txt", "w") as f:
    #     f.write("I LOVE PYTHON1\n")

    f = open("file.txt", "r")
    print(f.readlines())
    f.close()

    with open("file.txt", "r") as f:
        print(f.readlines())

    with open("file.txt", "a") as f:
        f.write("Hi friend\n")
        f.writelines(["cat\n", "dog\n"])

    with open("file.txt", "r") as f:
        for line in f:
            print(line, end="")
    print()


if __name__ == "__main__":
    main()
