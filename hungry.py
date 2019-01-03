#### Input:  [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 2, 1]
#### Output: 
# 1: 3개
# 2: 
# 3: 
# 4: 
# 5: 
#### 리스트에 나오는 숫자들 각 개수 세기

from collections import Counter
myList =  [1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 4, 2, 1]

print("---Counter( )---")
result = Counter(myList)
print(result)

for x in result:
    print(x, result[x])
