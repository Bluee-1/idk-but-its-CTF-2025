#!/usr/local/bin/python
import random, time
from Crypto.Util.number import *

flag = b'CSC{.......}'
p, q = getPrime(512), getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)
random.seed(int(time.time()))

def midnight(msg):
    e = random.randint(1, n)
    while GCD(e, phi) != 1: e = random.randint(1, n)
    return long_to_bytes(pow(bytes_to_long(msg), e, n)).hex()

def main():
    print('n:', n)
    while True:
        print('1. flag')
        print('2. message')
        print('3. exit')
        match int(input('> ')):
            case 1: print('flag:', midnight(flag))
            case 2: print('message:', midnight(bytes.fromhex(input('message in hex: '))))
            case 3: exit(); break
            case _: print('invalid choice')
        

if __name__ == '__main__':
    main()