### input: [[1,3,4,3], [234,42,45], [34, 1, 4, 5, 7], [1,2,46]]
## output:  add up all the odd numbers onlys

def sum_of_odd_numbers_in_list_of_lists(apple):
    sum = 0
    odd = 0
    for x in apple:
        for y in x:
            if y % 2 == 1:
                odd = odd + y
    print("odd: " + str(odd))

if __name__== "__main__":
     list_of_list = [[1,3,4,3], [234,42,45], [34, 1, 4, 5, 7], [1,2,46]]
     sum_of_odd_numbers_in_list_of_lists(list_of_list)



