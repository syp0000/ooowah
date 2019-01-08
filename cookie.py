

def split_list(_list, n):
    arrs = []
    while len(_list) > n:
        pice = _list[:n]
        arrs.append(pice)
        _list = _list[n:]
        arrs.append(_list)
        return arrs
    print(split_(_list, 5))
    # print(split(_list,n))

if __name__== "__main__":
    cookie = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    split_list(cookie, 5)
