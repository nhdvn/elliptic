
from PrimeField.EPoint import EPoint

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
        N = (self.N)
        U = (P.x * Q.z) % N
        V = (P.y * Q.z) % N
        W = (P.z * Q.z) % N
        # Initiate
        A = (Q.y * P.z - V) % N
        B = (Q.x * P.z - U) % N
        S = (B * B) % N
        C = (A * A * W - B * S - 2 * S * U) % N
        # NewPoint
        X = (B * C) % N
        Y = (A * (S * U - C) - B * S * V) % N
        Z = (B * S * W) % N
        return EPoint(X, Y, Z)

    def doubling(self, P):
        # Initiate
        N = (self.N)
        A = (self.A * P.z * P.z + 3 * P.x * P.x) % N
        B = (P.y * P.z) % N
        C = (B * P.x * P.y) % N
        D = (A * A - 8 * C) % N
        # NewPoint
        X = (2 * B * D) % N
        Y = (A * (4 * C - D) - 8 * P.y * P.y * B * B) % N
        Z = (8 * B * B * B) % N
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
        if not P.z: P.y = 1
        else:
            N = self.N
            I = pow(P.z, -1, N)
            P.z = 1
            P.x = P.x * I % N
            P.y = P.y * I % N
        return P