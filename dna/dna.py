import csv
import sys


def main():
    # TODO: Check for command-line usage (2 arguments expected: database CSV, DNA sequence file)

    # TODO: Read the database file into memory
    #   - Open with csv.DictReader
    #   - You'll need the list of STR column names (the keys other than "name")
    #   - And the list of people rows (each is a dict)

    # TODO: Read the DNA sequence file into a single string

    # TODO: For each STR, compute the longest consecutive run in the sequence
    #   - Use the longest_match() helper below
    #   - Store the results in a dict, keyed by STR

    # TODO: Compare those counts against each person's profile in the database
    #   - If every STR count matches, print that person's name and stop
    #   - If no person matches after checking all of them, print "No match"

    return


def longest_match(sequence, subsequence):
    """Return the length of the longest consecutive run of `subsequence` in `sequence`."""

    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each starting position in the sequence
    for i in range(sequence_length):

        count = 0

        # Extend the run as long as the next chunk matches
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
