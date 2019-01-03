#### Input:  [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 2, 1]
#### Output: [1, 2, 3, 4, 5, 6]
#### 리스트에서 반복되는거 뺴


def remove_duplicates(master) :
    result = (list(set(master)))
    print(result)

if __name__== "__main__":
    happy = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 2, 1]
    remove_duplicates(happy)