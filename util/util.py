from Crypto.Hash import RIPEMD160
from hashlib import sha256
from math import log

def get_hash256(h):
    return sha256(sha256(h).digest()).digest()

def get_hash160(h):
    return RIPEMD160.new(sha256(h).digest()).digest()

def bytes_needed(b):
    if b == 0:
        return 1
    return int(log(b, 256)) + 1

