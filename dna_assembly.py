import argparse
parser = argparse.ArgumentParser()
parser.add_argument("FileName", help = "Name of the read file")
args = parser.parse_args()
graphDict = {}
dnalist = []
counter = 1
k = 0
length = 0
with open(args.FileName) as f:
    line = f.readline()
    k = len(line)
    length = k - 1
    while line:
        if line[0:k - 2] not in graphDict:
            graphDict[line[0:k - 2]] = list()
            graphDict[line[0:k - 2]].append(line[1:k - 1])
            if counter == 1:
                dnalist.append(line[0:k - 2])
        elif line[1:k - 1] not in graphDict[line[0:k - 2]]:
            graphDict[line[0:k - 2]].append(line[1:k - 1])
        line = f.readline()
        counter = 0
checkfrag = dnalist[0]
temp = None
p = 0
i = 0
flag = 0
while  flag == 0 and counter == 0:
    counter = 0
    check = 0
    flag = 1
    while graphDict[checkfrag][0] != dnalist[p]:
        if graphDict[checkfrag][0] not in dnalist:
            temp = graphDict[checkfrag][0]
            dnalist.append(temp)
            del graphDict[checkfrag][0]
            checkfrag = temp
        else:
            temp = graphDict[checkfrag][0]
            dnalist.append(temp)
            del graphDict[checkfrag][0]
            checkfrag = temp
    dnalist.append(graphDict[checkfrag][0])
    del graphDict[checkfrag][0]
    while i < len(dnalist) and check == 0:
        if len(graphDict[dnalist[i]]) > 0:
            p = i
            check = 1
            flag = 0
            temp = graphDict[dnalist[i]][0]
            dnalist.append(temp)
            del graphDict[dnalist[i]][0]
            checkfrag = temp
        i += 1
    for i in range(len(dnalist)):
        if len(graphDict[dnalist[i]]) > 0:
            counter == 1
dnalist.pop()
result = ''
for i in range(len(dnalist)):
    if i == 0:
        result += dnalist[i]
    else:
        result += dnalist[i][len(dnalist[i]) - 1]
print(result[0:-(length - 2)])
