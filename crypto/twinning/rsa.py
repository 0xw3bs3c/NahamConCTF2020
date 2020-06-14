from Crypto.Util.number import *

n = 4852900584899
e = 65537

p, q =   2202929,2202931
c = 610073977927

phi = (p-1)*(q-1)
d = inverse(e, phi)

res = pow(c, d, n)
print(res)
