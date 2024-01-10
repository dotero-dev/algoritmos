def binary_search(lst,objetivo):
    lstIndices = range(0, len(lst))
    med = int(len(lst)/2)
    while len(lst)>2:
        if lst[med] == objetivo:
            return lstIndices[med]
        else:
            if lst[med] > objetivo:
                lstIndices = lstIndices[0:med+1]
                lst = lst[0:med+1]
                med = int(len(lst)/2)
            else:
                lstIndices = lstIndices[med:len(lst)+1]
                lst = lst[med:len(lst)+1]
                med = int(len(lst)/2)
    return False
