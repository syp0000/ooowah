from math import pi

def main(ifff):
    result = [int(num * pi) for num in ifff]
    # lists = [int(result) for x in ifff]
    print(result)

if __name__== "__main__":
    happy = [1, 4, 3, 5, 6, 7, 5, 8, 3]
    main(happy)