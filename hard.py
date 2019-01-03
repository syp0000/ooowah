#### input: list
#### [1,4,5,2,3,4,2,4,6,6,2,5]
#### output: 
#    Odd Number: 5
#    Even Numnber: 
####

def o(l):
    even = 0
    odd = 0
    for x in l:
        if x % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1    
    print("even: " + str(even))
    print("odd: " + str(odd))
    print("total: " + str(odd+even))
    print("lengh: " + str(len(l)))


if __name__== "__main__":
    lhhh = [1,4,5,2,3,4,2,4,6,6,2,5]
    o(lhhh)