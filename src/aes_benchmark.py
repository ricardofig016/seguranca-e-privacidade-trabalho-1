from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import timeit


def aes_time(file_path, key, iterations=100):
    with open(file_path, "rb") as f:
        data = f.read()

    # Time encryption
    def encrypt():
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded = padder.update(data) + padder.finalize()
        return iv + encryptor.update(padded) + encryptor.finalize()  # IV prepended

    encrypt_time = timeit.timeit(encrypt, number=iterations) / iterations * 1e6  # µs

    # Time decryption
    ciphertext = encrypt()
    iv = ciphertext[:16]
    actual_ct = ciphertext[16:]

    def decrypt():
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        padded = decryptor.update(actual_ct) + decryptor.finalize()
        return unpadder.update(padded) + unpadder.finalize()

    decrypt_time = timeit.timeit(decrypt, number=iterations) / iterations * 1e6
    return encrypt_time, decrypt_time


# Generate a single AES-256 key for all tests
AES_KEY = os.urandom(32)
