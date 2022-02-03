import random


# function for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_d(e, z):
    initial_z = z  # keep track of initial z for case in which we have a negative d

    x = 0  # initialize x, y (rs2)
    y = 1

    rs1x = 1  # initialize rs1x, rs1y (rs1)
    rs1y = 0

    while z != 0:  # keep computing until z = 0
        temp = e // z  # find out how many times z goes into e
        x, rs1x = rs1x - temp * x, x  # rs1x = x (bring value of rs2 down)
        y, rs1y = rs1y - temp + y, y  # rs1y = y (bring value of rs2 down)
        e, z = z, e % z  # update e, z as in Euclid(e,z)

    while rs1x < 0:  # if d is negative, keep adding initial z
        rs1x += initial_z

    return rs1x  # return d


def is_prime(num):
    if num > 1:

        # Iterate from 2 to n / 2  
        for i in range(2, num // 2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
            else:
                return True

    else:
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q  # calculate n
    z = (p - 1) * (q - 1)  # calculate z
    for i in range(3, n, 2):  # iterate through every prime number
        if gcd(z, i) == 1:  # if co-prime with z
            e = i  # set e = i (co-prime with z, prime, less than n)
            break
    d = get_d(e, z)  # run get_d with e & z, to obtain d value

    return (e, n), (d, n)  # returns public and private key pairs


def encrypt(pk, plaintext):  # pk = (e, n); pk[0] = e, pk[1] = n
    cipher = pow(ord(plaintext), int(pk[0]), int(pk[1]))  # int(plaintext) ^ e mod n
    # plaintext is a single character
    # cipher is a decimal number which is the encrypted version of plaintext
    # the pow function is much faster in calculating power compared to the ** symbol !!!
    return cipher


def decrypt(pk, ciphertext):  # pk = (d, n); pk[0] = d, pk[1] = n, ciphertext = plaintext^e mod n
    plain = chr(pow(ciphertext, int(pk[0]), int(pk[1])))  # ciphertext ^ d mod n
    # ciphertext is a single decimal number
    # the returned value is a character that is the decryption of ciphertext
    return "".join(plain)  # append plaintext to empty string

# File we wrote: get_d(), generate_keypair(), encrypt(), decrypt()
# get_d() - inputs e & z, returns d value
# generate_keypair() - inputs p & q, returns private key & public key
# encrypt() - takes in private key and plaintext, returns ciphertext
# decrypt() - takes in public key and ciphertext, returns original plaintext
