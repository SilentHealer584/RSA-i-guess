# RSA-i-guess
Python asymetric encryption system (Litterally RSA). Pretty customiseable, coded it from scratch using the math principles I learned from preparing my Oral Exam (Grand Oral).

Took me 2 days to code (on and off) for a total of maybe 3 hours. Had to figure out some bugs and optimize a lot. Only one external module is used.

**Use is pretty straght-forward:**


##For The Demo file
1. Install sympy by running `pip install sympy` in a command prompt.
2. Open the file and adjust the `message` and `complexity` parameters as needed.
3. Run the script. The output will comprehend both public and private keys, as well as the encrypted and original decrypted messages.

> Complexity is the length of the prime numbers used for key generation. These directly impact encryptable message length and encryption strength.

##For The Module
1. Install sympy by running `pip install sympy` in a command prompt.
2. Add the module to the same directory as your script.
3. Import the desired functions to your script.

> Functions include: `key_gen(complexity)`, `encrypt(message, public_key)` and `decrypt(message, private_key)`

##Example use
```
import rsa_i_guess

message = "Hello World"
complexity = 1024

public, private = key_gen(complexity)
print(public, '\n\n', private)

encrypted = encrypt(message, public)
print(encrypted)

decrypted = decrypt(encrypted, private)
print(decrypted)
```
