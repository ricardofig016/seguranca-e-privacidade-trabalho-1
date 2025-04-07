import os
import csv
import glob
from aes_benchmark import aes_time, AES_KEY
from rsa_benchmark import rsa_time
from sha_benchmark import sha256_time


def collect_results():
    file_dir = "random_text"

    # AES/SHA-256 Results
    aes_results = []
    sha_results = []
    for size in [8, 64, 512, 4096, 32768, 262144, 2097152]:
        filepaths = glob.glob(os.path.join(file_dir, f"aes_sha_{size}B_*.bin"))
        encrypt_times, decrypt_times, hash_times = [], [], []
        for filepath in filepaths:
            e, d = aes_time(filepath, AES_KEY)
            h = sha256_time(filepath)
            encrypt_times.append(e)
            decrypt_times.append(d)
            hash_times.append(h)
        aes_results.append(
            (
                size,
                sum(encrypt_times) / len(encrypt_times),
                sum(decrypt_times) / len(decrypt_times),
            )
        )
        sha_results.append((size, sum(hash_times) / len(hash_times)))

    # RSA Results
    rsa_results = []
    for size in [2, 4, 8, 16, 32, 64, 128]:
        filepaths = glob.glob(os.path.join(file_dir, f"rsa_{size}B_*.bin"))
        encrypt_times, decrypt_times = [], []
        for filepath in filepaths:
            e, d = rsa_time(filepath)
            encrypt_times.append(e)
            decrypt_times.append(d)
        rsa_results.append(
            (
                size,
                sum(encrypt_times) / len(encrypt_times),
                sum(decrypt_times) / len(decrypt_times),
            )
        )

    # Save to CSV
    os.makedirs("results", exist_ok=True)
    with open("results/results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Algorithm", "Size (Bytes)", "Encrypt (µs)", "Decrypt (µs)", "Hash (µs)"]
        )
        for aes, sha in zip(aes_results, sha_results):
            writer.writerow(["AES", aes[0], aes[1], aes[2], "-"])
            writer.writerow(["SHA", sha[0], "-", "-", sha[1]])
        for rsa in rsa_results:
            writer.writerow(["RSA", rsa[0], rsa[1], rsa[2], "-"])


if __name__ == "__main__":
    collect_results()
