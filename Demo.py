import math
from sympy import nextprime, randprime, mod_inverse

def random_primes(cpx):
    start = randprime(2**(cpx-1), 2**cpx)
    prime1 = nextprime(start)
    prime2 = nextprime(prime1)
    return [prime1, prime2]

def encode(message, n):
    encoded = 0
    for char in message:
        encoded = encoded * 256 + ord(char)
        if encoded >= n:
            raise ValueError("Message too large to encode with the given modulus n")
    return encoded

def decode(encoded):
    message = ''
    while encoded > 0:
        message = chr(encoded % 256) + message
        encoded //= 256
    return message

def key_gen(p, q):
    n = p * q
    fn = (p-1) * (q-1)
    e = 65537
    while math.gcd(e, fn) != 1:
        e += 2
    d = mod_inverse(e, fn)
    return [e, n], [d, n]

def encrypt(msg, public):
    enc_msg = encode(msg, public[1])
    encrypted = pow(enc_msg, public[0], public[1])
    return encrypted

def decrypt(encrypted, private):
    decrypted = pow(encrypted, private[0], private[1])
    dec_msg = decode(decrypted)
    return dec_msg

message = "github.com/SilentHealer584/RSA-i-guess"
complexity = 1024  # Can be set to higher values such as 204 for increased security.

prime1, prime2 = random_primes(complexity)
public, private = key_gen(prime1, prime2)
encrypted = encrypt(message, public)
decrypted = decrypt(encrypted, private)

print(f'\nEncrypted:\n{encrypted}')
print(f'\nDecrypted:\n{decrypted}\n')
