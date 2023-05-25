from deep_copy_kmer_counts import deep_copy_kmer_counts

from sum_kmer_counts import sum_kmer_counts

from divide_kmer_counts import divide_kmer_counts


def calc_mean_kmer_counts(kmer_counts_list):
    """Returns a mean kmer counts dictionary.

    Returned dictionary is keyed by kmer.

    Input kmer counts dictionaries should also be keyed by kmer.

    Returns an empty dictionary if the input list of kmer counts
    dictionaries is empty.

    Arguments:
    kmer_counts_list -- a list of kmer counts dictionaries
    """
    if len(kmer_counts_list) == 0:
        return {}
    sums = deep_copy_kmer_counts(kmer_counts_list[0])
    for kmer_counts in kmer_counts_list[1:]:
        sums = sum_kmer_counts(sums, kmer_counts)
    return divide_kmer_counts(sums, len(kmer_counts_list))
