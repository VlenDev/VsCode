import matplotlib.pyplot as plt
import numpy as np


def generate_primes(limit):
    """Use the Sieve of Eratosthenes to generate all primes <= limit."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0:2] = False  # 0 and 1 are not primes
    for number in range(2, int(limit**0.5) + 1):
        if sieve[number]:
            sieve[number*number:limit+1:number] = False
    return np.nonzero(sieve)[0]


def plot_primes(primes):
    """Generate plots from list of prime numbers."""
    indices = np.arange(len(primes))

    # Plot 1: Prime values vs their index
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(indices, primes, marker='.',
             linestyle='None', markersize=1, color='blue')
    plt.title("Prime Numbers up to 1,000,000")
    plt.xlabel("Index")
    plt.ylabel("Prime Value")

    # Plot 2: Prime gaps (difference between consecutive primes)
    gaps = np.diff(primes)
    plt.subplot(1, 2, 2)
    plt.plot(primes[1:], gaps, marker='.',
             linestyle='None', markersize=1, color='red')
    plt.title("Prime Gaps")
    plt.xlabel("Prime")
    plt.ylabel("Gap to Next Prime")

    plt.tight_layout()
    plt.show()


def main():
    limit = 1_000_000
    print(f"Generating primes up to {limit}...")
    primes = generate_primes(limit)
    print(f"Total primes found: {len(primes)}")
    plot_primes(primes)


if __name__ == "__main__":
    main()
