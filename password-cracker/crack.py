"""
L9.0 Password Cracker — starter skeleton.

Mount a dictionary attack on the hashes in hashes.txt using the
candidate words in wordlist.txt. Each line of hashes.txt is formatted as:

    md5:HEX_HASH
    sha256:HEX_HASH

For each hash, your program should try every word in the wordlist,
hash it under the correct algorithm, and check whether it matches.

Output (one line per hash):

    HEX_HASH cracked_word
    HEX_HASH NOT FOUND

Usage:
    python crack.py
"""

import hashlib


def hash_word(word, algo):
    """Return the hex digest of word under the given algorithm ('md5' or 'sha256')."""
    word_bytes = word.encode()
    if algo == "md5":
        return hashlib.md5(word_bytes).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(word_bytes).hexdigest()
    raise ValueError(f"Unknown algorithm: {algo}")


def load_wordlist(path):
    """Read wordlist file. Return list of candidate passwords (stripped of whitespace)."""
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def load_hashes(path):
    """Read hashes file. Return list of (algo, hex_hash) tuples.

    Skips blank lines and comment lines (starting with '#').
    """
    pairs = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            algo, h = line.split(":", 1)
            pairs.append((algo, h))
    return pairs


def crack(target_algo, target_hash, wordlist):
    """
    Try every candidate in the wordlist. If hash_word(candidate, target_algo)
    matches target_hash, return candidate. If no candidate matches, return None.

    TODO: Write the loop. Use hash_word() above.
    """
    pass  # YOUR CODE HERE


def main():
    hashes = load_hashes("hashes.txt")
    words = load_wordlist("wordlist.txt")

    for algo, h in hashes:
        result = crack(algo, h, words)
        if result is None:
            print(f"{h} NOT FOUND")
        else:
            print(f"{h} {result}")


if __name__ == "__main__":
    main()
