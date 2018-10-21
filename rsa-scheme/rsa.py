"""rsa.py"""

from utils import *
from random import getrandbits

class RSA:
    """
    RSA scheme implementation: allows for generation of public/private key pairs
    as well as encryption/decryption using them.

    Attributes:
        user (string): Name of the user who this RSA scheme belongs to.
        p, q (int): Two large (512-bit and above) prime numbers
        N (int): The modulus, equal to p * q
        totient (int): The number of primes below N, equal to (p - 1) * (q - 1)
        e (int): Arbitrary prime that is coprime with totient
        d (int): The inverse of (e mod totient)
    """

    def __init__(self, user):
        self.user = user
        self.p, self.q = self.generate_keys()
        self.N = self.p * self.q

        # Totient function (p - 1) * (q - 1) is the # of primes below N = p * q
        self.totient = (self.p - 1) * (self.q - 1)

        self.e = generate_coprime(self.totient)
        self.public_key = (self.N, self.e)
        self.d = find_inverse(self.totient, self.e)

    def encrypt(self, message):
        """
        Returns the encryption of a given message:
            E(x) = x^e mod N
        """
        assert type(message) == int, 'Must provide an integer message'
        return pow(message, self.e, self.N)

    def decrypt(self, encrypted):
        """
        Returns the decryption of a given encryption with the same
        public/private key pair.
            D(y) = y^d mod N
        """
        assert type(encrypted) == int, 'Must provide an integer encrypted message'
        return pow(encrypted, self.d, self.N)

    def generate_keys(self):
        """
        Creates a pair of unique large primes which the public/private keys will be
        created from.
        """
        p = generate_prime()
        q = generate_prime()
        while p == q:
            q = generate_prime()
        return p, q

    def __str__(self):
        return "{0}'s RSA: \nPublic key pair (N, e) = {1}".format(self.user, self.public_key)

if __name__ == '__main__':
    name = input('What is your name? ')
    print('Generating your RSA keys...\n')
    your_rsa = RSA(name)
    another_rsa = RSA('John DeNero')

    # Get a valid message
    msg = input('What is your message (as a string or an integer)? ')
    try:
        msg = int(msg)
    except:
        pass

    encrypted, decyrypted, wrong_decrypt = None, None, None
    if isinstance(msg, int):
        encrypted = your_rsa.encrypt(msg)
        decrypted = your_rsa.decrypt(encrypted)
        wrong_decrypt = another_rsa.decrypt(encrypted)
    else:
        msg = [ord(c) for c in list(msg)]
        encrypted = [your_rsa.encrypt(m) for m in msg]
        decrypted = ''.join([chr(your_rsa.decrypt(e)) for e in encrypted])
        try:
            wrong_decrypt = ''.join([chr(another_rsa.decrypt(e)) for e in encrypted])
        except:
            wrong_decrypt = 'Error! The other user cannot convert their decrypted message back to a string.'

    print('\nYour encrypted message is: \n')
    if isinstance(encrypted, list):
        for i, c in enumerate(encrypted):
            print('Encrypted Character #{0}:\n{1}'.format(i, c))
    else:
        print(encrypted)

    print('\n' + another_rsa.user + ', a user with different public/private key pairs, cannot decrypt your message!')
    print('He does not have the correct private key pair. This is what they get trying to decrypt your message: \n')

    print(wrong_decrypt)

    print('\nOnly you are able to decrypt the message.')
    print('Your decrypted (original) message is:', decrypted)
