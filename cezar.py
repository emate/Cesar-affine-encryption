#!/usr/bin/env python

"""
Author: Marcin Matłaszek <mmatlaszek@gmail.com>
License: GNU GPL v2

"""



import sys

def isPrime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

class Cesar():

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    crypt_alph = []
    n = 0

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.gen_alphabet(n, k)

    def gen_alphabet(self, n, k):
        for a in range(0,len(self.alphabet)):
            self.crypt_alph.append(self.alphabet[(k*a + n) % len(self.alphabet)])

    def decrypt(self, text):
        d_text = ""
        for a in text:
            d_text += self.alphabet[self.crypt_alph.index(a)]
        return d_text

    def encrypt(self, text):

        e_text = ""
        for a in text:
            e_text += self.crypt_alph[self.alphabet.index(a.lower())]
        return e_text


if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        print """
            Usage: %s <n> <k> <msg>
            """%sys.argv[0]
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    msg = sys.argv[3]
    
    if not isPrime(k):
        print "<k> parameter must be prime"
        sys.exit(1)

    cesar = Cesar(n, k)
    encrypted = cesar.encrypt(msg)
    decrypted = cesar.decrypt(msg)
    print """ 
    Original message: %s

    Decrypted message: %s
    Encrypted message: %s
    """% (msg, decrypted, encrypted)

