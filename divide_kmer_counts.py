from deep_copy_kmer_counts import deep_copy_kmer_counts

from multiply_kmer_counts import multiply_kmer_counts


def divide_kmer_counts(counts, factor):
    """Divides the kmer counts by the provided factor.

    Returns a new dictionary keyed by kmer.

    Input dictionary of kmer counts should also be keyed by kmer.

    Arguments:
    counts -- the input dictionary of kmer counts
    factor -- the factor to divide by
    """
    counts_deep_copy = deep_copy_kmer_counts(counts)
    return multiply_kmer_counts(counts_deep_copy, 1 / factor)
