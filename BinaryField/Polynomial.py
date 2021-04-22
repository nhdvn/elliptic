
class Polynomial:
    def __init__(self, P = 0):
        self.value = P

    def __str__(self):
        return "0x{:03X}".format(self.value)

    def __eq__(self, T):
        return self.value == T.value

    def __bool__(self):
        return self.value != 0

    def __add__(self, T):
        R = Polynomial()
        R.value = self.value ^ T.value
        return R

    def __sub__(self, T):
        R = Polynomial()
        R.value = self.value ^ T.value
        return R

    def __lshift__(self, K):
        R = Polynomial()
        R.value = self.value << K
        return R

    def __mul__(self, T):
        K = T.value
        M = Polynomial(self.value)
        R = Polynomial() 
        while K:
            if K & 1: R += M
            K = K >> 1
            M = M << 1
        return R

    def __mod__(self, T):
        R = Polynomial(self.value)
        M = Polynomial(T.value)
        N, K = R.degree(), M.degree()
        while N >= K:
            R += M << (N - K)
            N = R.degree()
        return R

    def invert(self, T):
        if not self: return None
        P = Polynomial(self.value)
        R = Polynomial(1)
        K = (1 << T.degree()) - 2
        while K:
            if K & 1: R = (R * P) % T
            K = K >> 1
            P = (P * P) % T 
        return R

    def degree(self):
        res = self.value.bit_length() 
        return res - 1 # count from 0