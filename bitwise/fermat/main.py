'''Fermat's little theorem: If p is a prime number, then for any integer a, the
number a^p − a is an integer multiple of p. In the notation of modular
arithmetic, this is expressed as a^p ≡ a mod p'''

# pylint: disable=C0103

import numpy as np
from matplotlib import pyplot as plt


def plot_little_fermat(height, width, overlay_primes=False):
    '''Plot a^(q-1) for ranges of integers a, q.'''
    # Compute the values
    array = np.zeros([height, width])

    for i in range(height):
        for j in range(width):
            q = j + 1  # ranges from 1 to WIDTH included
            a = height - i  # ranges from 1 to HEIGHT included
            array[i, j] = int(a ** (q - 1)) % q

    plt.imshow(array)

    # If we want to overlay primes we do it here
    if overlay_primes:
        overlay = get_prime_overlay(height, width)
        plt.imshow(overlay, alpha=0.3, cmap='gray')

    # If we want to overlay ... we do it here


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def get_prime_overlay(height, width):
    '''Return an array containing 1s where the column index is a prime number.'''
    prime_numbers = primes(width)
    prime_overlay = [[1 if i in prime_numbers else 0
                      for i in range(1, width + 1)],] * height
    return prime_overlay

if __name__ == '__main__':
    WIDTH = 1080
    HEIGHT = 1080

    plot_little_fermat(HEIGHT, WIDTH, overlay_primes=True)
    plt.show()
