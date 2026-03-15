# core/otp/utils/hash.py

import hashlib


def hash_otp(code: str):
    return hashlib.sha256(code.encode()).hexdigest()


def verify_otp(code: str, hashed: str) -> bool:
    return hash_otp(code) == hashed