import argparse
parser = argparse.ArgumentParser()
parser.add_argument("FileName", help  = "Name of the read file.")
parser.add_argument("Size_of_truss", help = "What kind of truss we are searching for.")
args = parser.parse_args()
graphDict = {}
with open(args.FileName) as f:
    line = f.readline()
    while line:
        a,b = line.split(' ')
        if int(a) not in graphDict:
            graphDict[int(a)] = list()
            graphDict[int(a)].append(int(b))
        else:
            graphDict[int(a)].append(int(b))
        if int(b) not in graphDict:
            graphDict[int(b)] = list()
            graphDict[int(b)].append(int(a))
        else:
            graphDict[int(b)].append(int(a))
        line = f.readline()
f.close()
a = []
b = []
def intersection(a,b):
    commonlist = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and b[j] != None:
                commonlist.append(a[i])
    return commonlist
flag = 0
while flag == 0:
    flag = 1
    for i in range(len(graphDict) + 1):
        if i in graphDict:
            for j in range(len(graphDict[i])):
                if graphDict[i][j] != None:
                    if(len(intersection(graphDict[i],graphDict[graphDict[i][j]]))) < int(args.Size_of_truss) - 2:
                        flag = 0
                        graphDict[i][j] = None
trusslist = []
for i in range(len(graphDict) + 1):
    if i in graphDict:
        finder = 1
        shortlist = []
        for j in range(len(graphDict[i])):
            if graphDict[i][j] != None and finder == 1:
                shortlist.append(i)
                finder = 2
            if graphDict[i][j] != None:
                shortlist.append(graphDict[i][j])
        if finder == 2:
            trusslist.append(shortlist)
k = len(trusslist)
lastlist = []
for i in range(k):
    for p in range(k):
        if trusslist[p] != None and trusslist[i] != None:
            if len(intersection(trusslist[i],trusslist[p])) == len(trusslist[i]) and p != i:
                trusslist[p] = None
for i in range(len(trusslist)):
    if trusslist[i] != None:
        lastlist.append(trusslist[i])
for i in range(len(lastlist)):
    lastlist[i].sort()
    prefix = '('
    for j in range(len(lastlist[i])):
        prefix += str(lastlist[i][j])
        if j != len(lastlist[i]) - 1:
            prefix += ', '
    prefix += ')'
    print(prefix)
