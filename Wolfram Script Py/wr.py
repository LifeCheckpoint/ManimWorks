# -*- coding: UTF-8 -*-
import os
import re
import time
import threading as th
import ctypes
import inspect

class WR_sc_thread(th.Thread):
    calc_suc = False

    def __init__(self, threadID, s):
        th.Thread.__init__(self)
        self.threadID = threadID
        self.s = s
    
    def run(self):
        print("WolframScript_" + str(self.threadID) + " starts")
        self.res = os.popen(self.s).readlines()
        self.calc_suc = True
        print("WolframScript_" + str(self.threadID) + " ends")

class WR:
    wm_Solo = "Solo"
    wm_Mult = "Mult"

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        ress = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if ress == 0:
            raise ValueError("invalid thread id")
        elif ress != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def stop_thread(self, thread):
        self._async_raise(thread.ident, SystemExit)
        
        def w_List2list(self, strs, **kwards):
            pass

    # def w_Solve(self, strs, **kwards):
    #     if(strs == "{}"):
    #         return []
    #     res = []
    #     patt = "(.*) -> (.*)"
    #     ree = re.compile(patt)
    #     r = ree.findall(strs)
    #     if r:
    #         print(len(r))
    #         return r
    #     else:
    #         print("No match.")

    def wolfram(self, s: str, mode = wm_Solo, **kwargs):
        f_delete = True
        f_time = 5000   # ms
        for key, value in kwargs.items():
            if(key.lower() == "delete"):
                f_delete = value
            if(key.lower() == "timeout"):
                f_time = value
        
        t_st = time.time() * 1000
        
        if mode == self.wm_Solo:
            s = s.replace("\"", "\\\"")

            th_id = int(time.time())
            calc_th = WR_sc_thread(th_id, "wolframscript -c \"" + s + "\"")
            calc_th.start()
            while time.time() * 1000 - t_st < f_time:
                if calc_th.calc_suc:
                    res = calc_th.res
                    return [r.replace("\n", "") for r in res]
                else:
                    time.sleep(0.05)
            
            self.stop_thread(calc_th)
            return ["TimeOut of " + str(f_time) + " ms"]

        if mode == self.wm_Mult:
            Filename = os.getcwd() + "\\" + str(time.time()) + "_wr.wrs"
            tmpFile = open(Filename, "w")
            print("Sent tmp File to \"" + Filename + "\"")
            tmpFile.write(s)
            tmpFile.close()
            
            th_id = int(time.time())
            calc_th = WR_sc_thread(th_id, "wolframscript -f \"" + Filename + "\" -print all")
            calc_th.start()
            while time.time() * 1000 - t_st < f_time:
                if calc_th.calc_suc:
                    res = calc_th.res
                    if f_delete:
                        os.remove(Filename)
                    return [r.replace("\n", "") for r in res]
                else:
                    time.sleep(0.05)
            
            self.stop_thread(calc_th)
            if f_delete:
                os.remove(Filename)
            return ["TimeOut of " + str(f_time) + " ms"]

# test
t_const, t_diy, t_mult = 1, 2, 3
w = WR()
# set test mode
test_mode = t_mult

# print(time.time() * 1000)
# time.sleep(1)
# print(time.time() * 1000)

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
    
    r = w.wolfram(
        cz, 
        mode = w.wm_Mult, 
        delete = True, 
        timeout = 10000
    )
    print(r)
    