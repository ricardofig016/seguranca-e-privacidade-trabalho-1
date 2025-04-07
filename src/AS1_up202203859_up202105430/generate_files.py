import os

# File sizes (AES/SHA and RSA)
AES_SHA_SIZES = [8, 64, 512, 4096, 32768, 262144, 2097152]  # Bytes
RSA_SIZES = [2, 4, 8, 16, 32, 64, 128]  # Bytes
NUM_FILES_PER_SIZE = 5  # Generate 5 files per size for statistical significance


def generate_files(sizes, prefix):
    output_dir = "random_text"
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    for size in sizes:
        for i in range(NUM_FILES_PER_SIZE):
            data = os.urandom(size)
            file_path = os.path.join(output_dir, f"{prefix}_{size}B_{i}.bin")
            with open(file_path, "wb") as f:
                f.write(data)


if __name__ == "__main__":
    generate_files(AES_SHA_SIZES, "aes_sha")
    generate_files(RSA_SIZES, "rsa")
