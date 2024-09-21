import numpy as np
from Circuit import Circuit

class EC08(Circuit):
    def __init__(self, Rs ,R1, R2,Y1, n1,Y2,n2):
        super().__init__()
        self.Rs = Rs
        self.R1 = R1
        self.R2 = R2 
        self.Y1 = Y1
        self.n1 = n1
        self.Y2 = Y2
        self.n2 = n2
        
        

        
        R = self.adj[0]
        R[0][1] = R[1][0] = Rs
        R[1][2] = R[2][1] = R1
        R[2][3] = R[3][2] = R2
       
        
        
        Y = self.adj[4]
        Y[1][2] = Y[2][1] = Y1
        Y[2][3]=Y[3][2]=Y2
        
        
        n = self.adj[5]
        n[1][2] = n[2][1] = n1
        n[2][3] = n[3][2] = n2
        

           
    
    def Z_W(self,A,w):
            return A*(1-1j)/(w**0.5)
        
    def freq_response(self, f):
        w = 2*np.pi*f
        R1andCP1 = self.parallel((self.Z_cpe(self.Y1,self.n1,w), self.R1))
        R2andCP2 = self.parallel((self.Z_cpe(self.Y2,self.n2,w), self.R2))
       
        
        Z13 = self.Rs+R1andCP1+R2andCP2
        return Z13
    

