from cryptography.hazmat.primitives import hashes
import timeit


def sha256_time(file_path, iterations=1000):
    with open(file_path, "rb") as f:
        data = f.read()

    # Create a new Hash object each iteration
    def hash_data():
        digest = hashes.Hash(hashes.SHA256())
        digest.update(data)
        return digest.finalize()

    time_per_run = timeit.timeit(hash_data, number=iterations) / iterations * 1e6
    return time_per_run
