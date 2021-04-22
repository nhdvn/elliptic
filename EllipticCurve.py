
from PrimeField.ECurve import ECurve as GP_ECurve
from PrimeField.EPoint import EPoint as GP_EPoint

from BinaryField.ECurve import ECurve as GB_ECurve
from BinaryField.EPoint import EPoint as GB_EPoint
from BinaryField.Polynomial import Polynomial as PL


def Test_GP_ECC():
    # NIST P-256
    A = -3
    B = 41058363725152142129326129780047268409114441015993725554835256314039467401291
    P = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    N = 115792089210356248762697446949407573529996955224135760342422259061068512044368
    E = GP_ECurve(A, B, P)

    # Base Point with Prime Order = Cardinality N
    X = 48439561293906451759052585252797914202762949526041747995844080717082404635286
    Y = 36134250956749795798585127919587881956611106672985015071877198253568414405109
    G = GP_EPoint(X, Y, 1)
    
    R = E.multiply(G, N)
    print(E.normalize(R))
    

def Test_GB_ECC():
    E = GB_ECurve(PL(0x001), PL(0x1CC), PL(0x805))
    P = GB_EPoint(PL(0x420), PL(0x5B3), PL(0x001))
    Q = GB_EPoint(PL(0x4B8), PL(0x167), PL(0x001))

    ifile = open("E7CyclicGroup", "w")

    for _ in range(2050):
        R = E.addition(R, P)
        R = E.normalize(R)
        ifile.write(str(R) + '\n')


if __name__ == "__main__": Test_GB_ECC()