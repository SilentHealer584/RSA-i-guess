import math
from sympy import nextprime, randprime, mod_inverse

def key_gen(cpx):
    start = randprime(2**(cpx-1), 2**cpx)
    p = nextprime(start)
    q = nextprime(p)  # Ensure distinct primes
    n = p * q
    fn = (p-1) * (q-1)
    e = 65537
    while math.gcd(e, fn) != 1:
        e += 2
    d = mod_inverse(e, fn)
    return [e, n], [d, n]

def encrypt(msg, public):
    encoded = 0
    for char in msg:
        encoded = encoded * 256 + ord(char)
        if encoded >= public[1]:
            raise ValueError("Message too large to encode with the given modulus n")
    encrypted = pow(encoded, public[0], public[1])
    return encrypted

def decrypt(encrypted, private):
    encoded = pow(encrypted, private[0], private[1])
    message = ''
    while encoded > 0:
        message = chr(encoded % 256) + message
        encoded //= 256
    return message
