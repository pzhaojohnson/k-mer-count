def sum_kmer_counts(counts1, counts2):
    """Returns a dictionary of kmer count sums.

    The returned dictionary is keyed by kmer.

    Input dictionaries of kmer counts should also be keyed by kmer.

    Can handle kmer counts dictionaries containing negative counts and
    counts of zero.

    Arguments:
    counts1 -- the first kmer counts dictionary
    counts2 -- the second kmer counts dictionary
    """
    count_sums = {}
    # add all kmer counts in the first dictionary
    for kmer1, ct1 in counts1.items():
        count_sums[kmer1] = ct1
    # add all kmer counts in the second dictionary
    for kmer2, ct2 in counts2.items():
        ct_sum = count_sums[kmer2] if kmer2 in count_sums else 0
        ct_sum += ct2
        count_sums[kmer2] = ct_sum
    return count_sums
