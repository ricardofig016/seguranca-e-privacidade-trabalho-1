import csv
import matplotlib.pyplot as plt


def load_data():
    aes, rsa, sha = [], [], []
    with open("results/results.csv") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            if row[0] == "AES":
                aes.append((int(row[1]), float(row[2]), float(row[3])))
            elif row[0] == "RSA":
                rsa.append((int(row[1]), float(row[2]), float(row[3])))
            elif row[0] == "SHA":
                sha.append((int(row[1]), float(row[4])))
    return aes, rsa, sha


def plot_results(aes, rsa, sha):
    # AES Plot
    plt.figure()
    sizes = [x[0] for x in aes]
    plt.plot(sizes, [x[1] for x in aes], label="AES Encrypt")
    plt.plot(sizes, [x[2] for x in aes], label="AES Decrypt")
    plt.xscale("log")
    plt.xlabel("File Size (Bytes)")
    plt.ylabel("Time (µs)")
    plt.xticks(
        [8, 64, 512, 4096, 32768, 262144, 2097152],
        [8, 64, 512, 4096, 32768, 262144, 2097152],
    )
    plt.legend()
    plt.savefig("results/aes.png")

    # RSA Plot
    plt.figure()
    sizes = [x[0] for x in rsa]
    plt.plot(sizes, [x[1] for x in rsa], label="RSA Encrypt")
    plt.plot(sizes, [x[2] for x in rsa], label="RSA Decrypt")
    plt.xscale("log")
    plt.xlabel("File Size (Bytes)")
    plt.ylabel("Time (µs)")
    plt.xticks([2, 4, 8, 16, 32, 64, 128], [2, 4, 8, 16, 32, 64, 128])
    plt.legend()
    plt.savefig("results/rsa.png")

    # SHA Plot
    plt.figure()
    sizes = [x[0] for x in sha]
    plt.plot(sizes, [x[1] for x in sha], label="SHA-256")
    plt.xscale("log")
    plt.xlabel("File Size (Bytes)")
    plt.ylabel("Time (µs)")
    plt.xticks(
        [8, 64, 512, 4096, 32768, 262144, 2097152],
        [8, 64, 512, 4096, 32768, 262144, 2097152],
    )
    plt.legend()
    plt.savefig("results/sha.png")


if __name__ == "__main__":
    aes_data, rsa_data, sha_data = load_data()
    plot_results(aes_data, rsa_data, sha_data)
