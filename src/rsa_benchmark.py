from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import timeit

# Generate RSA-2048 keys once
RSA_PRIVATE_KEY = rsa.generate_private_key(public_exponent=65537, key_size=2048)
RSA_PUBLIC_KEY = RSA_PRIVATE_KEY.public_key()
RSA_PADDING = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None
)


def rsa_time(file_path, iterations=10):  # Fewer iterations due to RSA slowness
    with open(file_path, "rb") as f:
        data = f.read()

    # Encrypt
    encrypt_time = (
        timeit.timeit(
            lambda: RSA_PUBLIC_KEY.encrypt(data, RSA_PADDING), number=iterations
        )
        / iterations
        * 1e6
    )

    # Decrypt (pre-encrypt data once)
    ciphertext = RSA_PUBLIC_KEY.encrypt(data, RSA_PADDING)
    decrypt_time = (
        timeit.timeit(
            lambda: RSA_PRIVATE_KEY.decrypt(ciphertext, RSA_PADDING), number=iterations
        )
        / iterations
        * 1e6
    )

    return encrypt_time, decrypt_time
