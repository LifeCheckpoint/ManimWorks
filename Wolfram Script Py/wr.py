# -*- coding: UTF-8 -*-
import os
import sys
import re

class WR:
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

    def ana(self, func_name: str, inputs, replace_enter: bool = True, **kwards):
        this_module = sys.modules['__main__']
        if(hasattr(this_module, func_name) == False):
            print("WR cann't analysis \"" + func_name + "\".")
            return inputs
        f = getattr(this_module, func_name)
        if(isinstance(inputs, str)):
            return f(inputs, kwards)
        if(isinstance(inputs, list)):
            return f(str("\n".join(inputs)), kwards)
        print("WR cann't analysis the type of \"" + type(inputs).__name__ + "\"")

# test
# cz = input()
cz = "Solve[x==1,{x}]"
w = WR()
r = w.wolfram(cz)
print(r)
# print(w.w_Solve(w.wolfram(cz)))
print(w.w_Solve(r[0]))