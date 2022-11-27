def save(list, name):
    f = open(name, 'w')
    for i in list:
        for j in i:
            f.write(str(j))
            f.write(', ')
        f.write('\n')
    f.close()
