import numpy as np
import math
from itertools import product

class Circuit:
    def __init__(self,nodes=7):
        R = 1e7 * np.ones([nodes, nodes])
        L = 1e3 * np.ones([nodes, nodes])
        C = np.zeros([nodes, nodes])
        W = 1e7 * np.ones([nodes, nodes])
        CPE_Y = 1e-12*np.ones([nodes, nodes])
        CPE_n = np.ones([nodes, nodes])
        self.adj = np.stack((R, L, C, W, CPE_Y, CPE_n))
        
    def parallel(self,imps):   # Returns equivalent impedance of input tuple imps
        res = 1e-12
        # print(type(imps))
        for Z in imps:
        #     pass
            # print(type(Z))
            # if Z.any() <= 1e-12:
            res += 1/Z
        return 1/res

    def Z_cpe(self,Y,n,w):
        if Y <= 1e-12:
            Y = 1e-12
        return 1/(Y*(1j*w)**n)

    def Z_W(self,A,w):
        return A*(1-1j)/(w**0.5)
    
def createTables(params):
        tables = [tuple(row) for row in product(*params)]
        return tables
    
def dec_step(start, end, steps):
    log_list = np.logspace(np.log10(start), np.log10(end), num=steps)
    return log_list



