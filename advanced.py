

def sum_of_list_of_lists(l):
    sum = 0
    for x in l:
        for y in x:
            sum = sum + y
    print(sum)


if __name__== "__main__":
    list_of_list = [[1, 4, 54], [23, 45], [64, 11, 23], [53, 2, 6, 45]]
    
    sum_of_list_of_lists(list_of_list)