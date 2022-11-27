from iris_analysis.io.load import load
from iris_analysis.io.save import save
from iris_analysis.calculate import mean
from iris_analysis.calculate import median
from iris_analysis.calculate import std

import sys
path = sys.argv[1]

path = 'C:\\Users\\1aaa2\\PycharmProjects\\Pd4\\Data\\iris.csv'
dane = load(path)
col = [['mean','median','std']]
for i in range(len(dane)):
    col.append([mean(dane[i]),median(dane[i]),std(dane[i])])

save(col, sys.argv[2])

