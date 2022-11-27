def mean(list):
    x = 0
    for i in list:
        x += i
    return x/len(list)

def median(list):
    if len(list)%2 == 1:
        return list[len(list)//2]
    else:
        return (list[len(list)//2-1]+list[len(list)//2])/2

def std(list):
    x = 0
    M = mean(list)
    for i in list:
        x += (i-M)**2
    return x**0.5