def count_kmers(sequence='', k=1):
    """Returns a dictionary of counts keyed by kmers of size k.

    kmers not present in the sequence are not included as keys in the
    returned dictionary.

    Keyword arguments:
    sequence -- the sequence to count kmers for (default '')
    k -- the size of kmers to count (default 1)
    """
    counts = {}
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        ct = counts[kmer] + 1 if kmer in counts else 1
        counts[kmer] = ct
    return counts
