# http://tinyurl.com/gvcdgxf

import csv

with open("stc.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
