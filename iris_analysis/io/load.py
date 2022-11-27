def load(path):
    f = open(path, 'r')
    data = f.readlines()
    names = data[:1]
    names = names[0]
    names = names.replace("\"","").split(",")

    rows = data[1:]
    cols = [[],[],[],[]]
    for i in range(len(rows)):
        w = rows[i]
        w = w.split(',')
        for j in range(4):
            w[j] = float(w[j])
            cols[j].append(w[j])
        rows[i] = w
    return cols