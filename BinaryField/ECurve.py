
from BinaryField.EPoint import EPoint
from BinaryField.Polynomial import Polynomial

class ECurve:
    def __init__(self, A, B, N):
        self.A = A
        self.B = B
        self.N = N

    def addition(self, P, Q):
        O = EPoint()
        if  P == O: return Q
        if  Q == O: return P
        if  P == Q: return self.doubling(P)
        if -Q == P: return O
        # Initiate
        N = (self.N)
        A = (P.y * Q.z + P.z * Q.y) % N
        B = (P.x * Q.z + P.z * Q.x) % N
        C = (B * B) % N
        D = (P.z * Q.z) % N
        E = ((A * A + A * B + self.A * C) * D + B * C) % N
        # NewPoint
        X = (B * E) % N
        Y = (C * (A * P.x + B * P.y) * Q.z + (A + B) * E) % N
        Z = (B * B * B * D) % N
        return EPoint(X, Y, Z)
        
    def doubling(self, P):
        # Initiate
        N = (self.N)
        A = (P.x * P.x) % N
        B = (A + P.y * P.z) % N
        C = (P.x * P.z) % N
        D = (C * C) % N
        E = (B * B + B * C + self.A * D) % N
        # NewPoint
        X = (C * E) % N
        Y = (E * (B + C) + A * A * C) % N
        Z = (C * D) % N
        return EPoint(X, Y, Z)      

    def multiply(self, T, K):
        Q = EPoint()
        P = EPoint(T.x, T.y, T.z)
        while K:
            if K & 1: 
                Q = self.addition(P, Q)
            K = K >> 1
            P = self.doubling(P)                
        return Q

    def normalize(self, P):
        if not P.z:
            P.y = Polynomial(1)
        else:
            N = (self.N)
            I = (P.z).invert(N)
            P.x = P.x * I % N
            P.y = P.y * I % N
            P.z = Polynomial(1)
        return P
