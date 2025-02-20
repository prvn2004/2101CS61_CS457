from math import gcd, isqrt
import random
from random import randint
import sys
import time

def encodeMessage(msg):
    encodedMsg = 0

    for char in msg:
        encodedMsg = encodedMsg << 8
        encodedMsg = encodedMsg ^ ord(char)
    return encodedMsg

def getRandomPrime(primeSize, algorithm="miller-rabin"):
    """Generate a prime number using the specified algorithm."""
    x = randint(1 << (primeSize - 1), (1 << primeSize) - 1)
    while not (isPrime(x, algorithm)):
        x = randint(1 << (primeSize - 1), (1 << primeSize) - 1) 
    return x

def isPrime(n, algorithm="miller-rabin"):
    """Check primality using the selected algorithm."""
    if algorithm == "miller-rabin":
        return millerRabinTest(n)
    elif algorithm == "deterministic-root-n":
        return deterministicRootNTest(n)
    else:
        raise ValueError("Unsupported algorithm. Choose 'miller-rabin' or 'deterministic-root-n'.")

# Miller-Rabin Primality Test
def millerRabinTest(n):
    if n % 2 == 0:
        return False

    for i in range(1, 40):
        a = random.randint(1, n - 1)
        if isComposite(a, n):
            return False
    return True

def isComposite(a, n):
    t, d = decompose(n - 1)
    x = pow(a, d, n)
    
    if x == 1 or x == n - 1:
        return False

    for i in range(1, t):
        x0 = x
        x = pow(x0, 2, n)
        if x == 1 and x0 != 1 and x0 != n - 1:
            return True
    if x != 1:
        return True
        
    return False

# Deterministic Root-N Primality Test
def deterministicRootNTest(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    limit = isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            print("Checked for n", n, "False")
            return False
    print("Checked for n", n, "True")
    return True

def decompose(n):
    i = 0
    while n & (1 << i) == 0:
        i += 1
    return i, n >> i

def getKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for i in range(2, phi):
        if gcd(phi, i) == 1:
            e = i
            break
         
    d = multiplicativeInverse(e, phi)
    return n, e, d

def multiplicativeInverse(e, phi):
    return extendedEuclid(e, phi)[1] % phi

def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0
    else: 
        d2, x2, y2 = extendedEuclid(b, a % b)
        d, x, y = d2, y2, x2 - (a // b) * y2
        return d, x, y

try:
    modulusSize = int(sys.argv[1])
except:
    modulusSize = 1024

# Driver Code Starts Here
# Prompt user to enter a message
msg = input("Enter your message: ")

# Ask the user which prime generation algorithm to use
print("\nChoose the prime generation algorithm:")
print("1. Miller-Rabin Test (Probabilistic)")
print("2. Deterministic Root-N Test")
algorithm_choice = input("Enter 1 or 2: ")

if algorithm_choice == "1":
    prime_algo = "miller-rabin"
elif algorithm_choice == "2":
    prime_algo = "deterministic-root-n"
else:
    print("Invalid choice! Defaulting to Miller-Rabin Test.")
    prime_algo = "miller-rabin"

# Start the timer
start_time = time.time()

primeSize = modulusSize // 2
p = getRandomPrime(primeSize, prime_algo)
q = getRandomPrime(primeSize, prime_algo)
while p == q:
    q = getRandomPrime(primeSize, prime_algo)

n, e, d = getKeys(p, q)

encodedMsg = encodeMessage(msg)
encryptedMsg = pow(encodedMsg, e, n)
decryptedMsg = pow(encryptedMsg, d, n)

# Stop the timer
end_time = time.time()
total_time = end_time - start_time

# Display results
print("Public key (e, n):")
print("\te = ", e)
print("\tn = ", n)
print("\nPrivate key (d, n):")
print("\td = ", d)
print("\tn = ", n)
print("\nOriginal message string:\n\t", msg)
print("\nInteger encoded message:\n\t", encodedMsg)
print("\nEncrypted message( C(M) = M^e % n ):\n\t", encryptedMsg)
print("\nDecrypted message( M(C) = C^d % n ):\n\t", decryptedMsg)
if encodedMsg == decryptedMsg:
    print("\nThe decrypted message and the original encoded message match.")

# Display total execution time
print("\nTotal time from message entry to completion: ", total_time * 1000, " ms")
