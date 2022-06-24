# -*- coding: UTF-8 -*-
import os
import sys
import re

class WR:
    def w_List2list(self, strs, **kwards):
        pass

    def w_Solve(self, strs, **kwards):
        if(strs == "{}"):
            return []
        res = []
        patt = "(.*) -> (.*)"
        ree = re.compile(patt)
        r = ree.findall(strs)
        if r:
            print(len(r))
            return r
        else:
            print("No match.")


    def wolfram(self, s: str, output: bool = False):
        s = s.replace("\"", "\\\"")
        res = os.popen('wolframscript -c \"' + s + '\"').readlines()
        return [r.replace("\n", "") for r in res]

# test
# cz = input()
cz = "Solve[x==1,{x}]"
w = WR()
r = w.wolfram(cz)
print(r)
# print(w.w_Solve(w.wolfram(cz)))
print(w.w_Solve(r[0]))