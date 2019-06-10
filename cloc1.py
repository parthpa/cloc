import sys

f = open(sys.argv[-1], "r")
count = 0
multi_comment_flag = False

for line in f:
    stripped = line.strip()
    if stripped:
        if multi_comment_flag == True and stripped[0:3] != "'''":
            continue
        elif multi_comment_flag == True and stripped[0:3] == "'''":
            multi_comment_flag = False
            continue
        else:    
            if stripped[0] != "#" and stripped[0:3] != "'''":
                count += 1
                #print "%s %s" % (count, stripped)
            elif stripped[0:3] == "'''":
                multi_comment_flag = True

print "Significant Lines: %d" % (count)

f.close()
