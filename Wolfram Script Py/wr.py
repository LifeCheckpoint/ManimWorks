# -*- coding: UTF-8 -*-
import os
import re
import time

class WR:
    wm_Solo = "Solo"
    wm_Mult = "Mult"

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


    def wolfram(self, s: str, mode = wm_Solo, **kwargs):
        f_delete = True
        for key, value in kwargs.items():
            if(key == "delete"):
                f_delete = value
        if mode == self.wm_Solo:
            s = s.replace("\"", "\\\"")
            res = os.popen("wolframscript -c \"" + s + "\"").readlines()
            return [r.replace("\n", "") for r in res]
        if mode == self.wm_Mult:
            Filename = os.getcwd() + "\\" + str(time.time()) + "_wr.wrs"
            tmpFile = open(Filename, "w")
            print("Sent tmp File to \"" + Filename + "\"")
            tmpFile.write(s)
            tmpFile.close()
            res = os.popen("wolframscript -f \"" + Filename + "\" -print all").readlines()
            if f_delete:
                os.remove(Filename)
            return [r.replace("\n", "") for r in res]

# test
t_const, t_diy, t_mult = 1, 2, 3
w = WR()
# set test mode
test_mode = t_mult

if test_mode == t_const:
    cz = "Solve[x==1,{x}]"
    r = w.wolfram(cz)
    print(r)
    # print(w.w_Solve(w.wolfram(cz)))
    print(w.w_Solve(r[0]))
if test_mode == t_diy:
    cz = input()
    r = w.wolfram(cz)
    print(r)
if test_mode == t_mult:
    cz = ""
    while True:
        tmp = input()
        if(tmp.lower() == "end"):
            break
        cz = cz + tmp + "\n"
    r = w.wolfram(cz, mode = w.wm_Mult, delete = True)
    print(r)
    