### input: [1,2,4,5,3,2,1,4,6,7,7554,5,43,52]
### output:  리스트안에 두번째로 큰수 

def main(list1):

    # for item in list1:
    #     item = int(item)
    # length = len(list1)
    list1.sort()
    print("Second Smallest element is: ", list1[len(list1)-2])

if __name__== "__main__":
    cookie = [1,2,4,5,3,2,1,4,6,7,7554,5,43,52]
    main(cookie)

