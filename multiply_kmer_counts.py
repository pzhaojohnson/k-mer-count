from deep_copy_kmer_counts import deep_copy_kmer_counts


def multiply_kmer_counts(counts, factor):
    """Multiplies the kmer counts by the given factor.

    Returns a new dictionary of multiplied kmer counts keyed by kmer.

    The input dictionary of kmer counts should also be keyed by kmer.

    Arguments:
    counts -- the input kmer counts dictionary
    factor -- the factor to multiply by
    """
    multiplied = deep_copy_kmer_counts(counts)
    for kmer in multiplied:
        multiplied[kmer] *= factor
    return multiplied
