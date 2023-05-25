def deep_copy_kmer_counts(counts):
    """Returns a deep copy of the input kmer counts dictionary.

    Dictionary of kmer counts should be keyed by kmer.

    Arguments:
    counts -- the kmer counts dictionary
    """
    counts_deep_copy = {}
    for kmer, ct in counts.items():
        counts_deep_copy[kmer] = ct
    return counts_deep_copy
