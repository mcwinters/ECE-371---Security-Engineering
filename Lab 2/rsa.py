
import random

#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extended euclidean algorithm to get the d value
def get_d(e, z):
    d=0
    init_z = z
    rs = [0, 0]     # Our array for the coefficient values
    rs1 = [1, 0]    # Our array for the left hand coefficients
    rs2 = [0, 1]    # Our array for the right hand coefficients
    while True:
        try:
            constant = z // e   # To see how many times e fits into z evenly
            temp = e
            e = z % e
            z = temp
            rs[0] = rs1[0] - constant*rs2[0]    # Doing arithmetic to get coefficient values, see line 7
            rs[1] = rs1[1] - constant*rs2[1]
            rs1[0] = rs2[0]     # "Bringing the value of rs2 down"
            rs1[1] = rs2[1]
            rs2[0] = rs[0]      # Substituting before algebra
            rs2[1] = rs[1]
            d = rs[1]           # Only care about right most coefficient value
            if z % e == 0:      # If the remainder is 0, like 4/1, we're done
                break
        except ZeroDivisionError:   # If the numbers don't adhere to e boundaries
            print("Choose an 'e' value such that 1<e<z and that is relatively prime to z")
            break
    while d < 0:
        d = d + init_z
    return d
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2):
         
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

    e=0
    d=0
    n = p * q
    z = (p - 1) * (q - 1)
    for i in range(2, n, 2):
        if gcd(z, i) == 1:
            e = i
            break
    d = get_d(e, z)
    return (e, n), (d, n)

def encrypt(pk, plaintext): # pk argument must be generate keypair(p,q)[0]
    m = int(plaintext)
    e = pk[0]
    n = pk[1]
    cipher = pow(m, e, n)
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    return cipher

def decrypt(pk, ciphertext): # pk argument must be generate keypair(p,q)[1]
    d = pk[0]
    n = pk[1]
    plain = pow(ciphertext, d, n)
    plain = str(plain)
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    return plain
