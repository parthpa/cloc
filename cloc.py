'''
CLOC: Create a program that will count the number of significant (non comment/blank) lines in a python file.

The program should contain usages of at least:

Variables
Text
Functions
Branching
Looping
Arrays
File I/O
Error Handling
Classes
Debugging (comment out any useful debug print statements)
Testing
'''
import sys

class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.comments = 0
        self.classes = 0
        self.functions = 0
        self.prints = 0
        self.significant_lines = 0
    
    def open_file(self):
        self.file = open(self.filename, "r")

    def is_comment(self):
        self.comments += 1
    
    def is_class(self):
        self.classes += 1
    
    def is_function(self):
        self.functions += 1
    
    def is_print(self):
        self.prints += 1
    
    def is_significant_line(self):
        self.significant_lines += 1

    def file_object(self):
        return self.file

    def close_file(self):
        self.file.close()

    def is_file_closed(self):
        return self.file.closed
    
#f = open("car.py", "r")
f = File(sys.argv[-1])
f.open_file()
multi_comment_flag = False

for line in f.file_object():
    stripped = line.strip()  
    if stripped:
        if multi_comment_flag == True and stripped[0:3] != "'''":
            continue
        elif multi_comment_flag == True and stripped[0:3] == "'''":
            multi_comment_flag = False
            continue
        else:    
            if stripped[0] != "#" and stripped[0:3] != "'''":
                f.is_significant_line()
                #print "%s %s" % (f.significant_lines, stripped)
                if stripped[0:4] == "def ":
                    f.is_function()
                elif stripped[0:6] == "class ":
                    f.is_class()
                elif stripped[0:6] == "print ":
                    f.is_print()
            elif stripped[0:3] == "'''":
                multi_comment_flag = True
                f.is_comment()
            else:
                f.is_comment()

f.close_file()
print "Comments: %d" % (f.comments)
print "Functions: %d" % (f.functions)
print "Classes: %d" % (f.classes)
print "Prints: %d" % (f.prints)
print "Significant Lines: %d" % (f.significant_lines)

'''
print f.file_object()
print f.is_file_closed()
f.close_file()
print f.is_file_closed()
'''

'''
f = open("car.py", "r")
count = 0
for line in f:
    if line.strip():
        stripped = line.strip()
        if stripped[0] != "#":
            count += 1
        print "%s %s" % (count, stripped)

f.close()
'''