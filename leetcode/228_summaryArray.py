list1 = [0,1,2,3,5,8,9,11]

def summary_array(list1):
    list1.append("a")
    print(list1)
    range_str = []
    start, end = list1[0], list1[0]
    for i in range(1,len(list1)):
        if list1[i] == list1[i-1]+1:
            end +=1
        else:
            if start == end:
                range_str.append(str(start))
            else:
                range_str.append(str(start) + "->" + str(end))
            start = end =list1[i]
    return range_str

print(summary_array(list1))
