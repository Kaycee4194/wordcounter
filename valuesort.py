def sortValue(dic):
    s = sorted(dic.values(), reverse = True)
    d = {}
    for val in s:
        for v in dic:
            if dic[v] == val:
                d[v] = dic[v]
    return d

if __name__ == '__main__':
    d = {1: 4, 2: 4, 3: 7, 4: 3, 5: 4}
    print(sortValue(d))
