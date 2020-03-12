import sys

if __name__ == "__main__":
    num = getattr(__builtins__,sys.argv[2])(int(sys.argv[1]))

    print(num)