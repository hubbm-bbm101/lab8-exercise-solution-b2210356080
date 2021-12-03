import sys

f = open(sys.argv[1],"r") #student.py

name = []
uni = []

for line in f:
    name.append(line.split(":")[0])
    uni.append(line.split(":")[1].strip("\n"))
f.close()

dict1 = dict(zip(name,uni))

for i in sys.argv[2].split(","):
    try:
        print("Name: %s, University: %s" %(i, dict1[i]))
        assert i in name
    except:
        print("No record of '%s' was found!" %i)
