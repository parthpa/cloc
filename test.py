import sys

f = open(sys.argv[-1], "r")
count = 0
multi_comment_flag = False

for line in f:
    print line[0]

f.close()
