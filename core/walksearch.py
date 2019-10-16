import os
import commands
import sys
import re
def walkDir(Dir, Type=""):
    """
    func:
        find a file recursionly in one directory with type "Type" 
    Args:
        Dir -> string, the aim directory
    return -> list 
        all matched files
    """
    File = []
    for tup in os.walk(Dir):
        path = tup[0]
        files = tup[2]
        for f in files:
            if f.endswith(Type):
                File.append(os.path.abspath(os.path.join(path, f)))
    File.sort()
    return File

def findfile(p, Type="") :
    File = []
    # if p is a file
    if os.path.isfile(p) and p.endswith(Type):
        File.append(os.path.abspath(p))
        File.sort()
        return File
    # p is a director
    if os.path.isdir(p):
        for i in os.listdir(p):
            if os.path.isfile(i) and i.endswith(Type):
                File.append(os.path.join(os.path.abspath(p), i))
    File.sort()
    return File


def match(k, aim):
    key = k.replace("*", "[a-zA-Z0-9_.]*")
    pattern = re.compile(key)
    if pattern.match(aim):
        return True
    else:
        return False

def findRegular(expre, Type = "", r = ""):
    matchList = []
    File = []
    for i in os.listdir("."):
        if match(expre, i):
            matchList.append(i)
    for i in matchList:
        if os.path.isfile(i) and i.endswith(Type):
            File.append(os.path.abspath(i))
        elif os.path.isdir(i):
            File += findfiler(i, Type, r)
    File.sort()
    return File

def findfiler(p, Type = "", r="-r"):
    File = []
    if os.path.isfile(p) and p.endswith(Type):
        File.append(os.path.abspath(p))
        return File

    #print "findfiler, p = ", p
    if os.path.isdir(p):
        #print "p isdir"
        if r == "-r":
            return walkDir(p, Type)
        else:
            #print "findfile", findfile(p, Type)
            return findfile(p, Type)
    
    #may be regular expression
    return findRegular(p, Type, r)






