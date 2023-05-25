from deep_copy_kmer_counts import deep_copy_kmer_counts

from sum_kmer_counts import sum_kmer_counts

from multiply_kmer_counts import multiply_kmer_counts


def subtract_kmer_counts(counts1, counts2):
    """Subtracts the second kmer counts from the first kmer counts.

    Returns a new dictionary keyed by kmer.

    Input dictionaries of kmer counts should also be keyed by kmer.

    Arguments:
    counts1 -- the first kmer counts dictionary
    counts2 -- the second kmer counts dictionary
    """
    deep_copy1 = deep_copy_kmer_counts(counts1)
    deep_copy2 = deep_copy_kmer_counts(counts2)
    negative2 = multiply_kmer_counts(deep_copy2, -1)
    return sum_kmer_counts(deep_copy1, negative2)
