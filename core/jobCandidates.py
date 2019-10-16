#!/usr/bin/env python
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : jobCandidates.py
#   Created Time  : 2019-10-16 20:45
#   Last Modified : 2019-10-16 20:45
#   Describe      :
#
# ====================================================
import sys
import walksearch 

class jobCandidates:
    def __init__(self):
        self._jobList = []
        self._opt = []
        self._arv = []
        self._diy = {}
        self._Uasge = ""
    def _prepare(self):
        if '-help' in sys.argv or "--help" in sys.argv or '-h' in sys.argv \
        or '--h' in sys.argv:
            print(self._Uasge)
            exit()
        # devide the input into option and var
        for i in range(1, len(sys.argv)):
            if '=' in sys.argv[i]:
                #print sys.argv[i]
                ss = sys.argv[i].split('=')
                #print ss
                self._diy[ss[0]] = ss[1]
                continue
            elif '-' == sys.argv[i][0]:
                self._opt.append(sys.argv[i])
            else:
                self._arv.append(sys.argv[i])
        if len(self._arv) == 0:
            self._arv.append(".")
        
        r = ""
        self._jobList = []
        if "-r" in self._opt:
            r = "-r"
        Type = []
        # get the default type: .txt, .c, .cxx, .cpp, .C, .py .sh
        if '-txt' in self._opt:
            Type.append('.txt')
        if '-c' in self._opt:
            Type += ['.C', '.cc', '.cxx', '.cpp']
        if '-sh' in self._opt:
            Type += ['.sh', '.csh']
        if '-py' in self._opt:
            Type.append('.py')
        #diy type
        #print self._diy.keys()
        if 'type' in self._diy.keys():
            #print self._diy["type"].split(',')
            Type += self._diy['type'].split(',')
            #if not 'sub' in self._diy.keys():
            #    self._diy['sub'] = 'hep_sub -g physics'
            #if not 'exe' in self._diy.keys():
            #    self._diy['exe'] = 'root -l -b -q '

        #print self._diy
        #print  "all Type", Type
        for p in self._arv:
            for t in Type:
                #print "path is:  ", p
                #print "type: ", t
                #print "r: ", r
                self._jobList += walksearch.findfiler(p, t, r)
                #print walksearch.findfiler(p, t, r)
