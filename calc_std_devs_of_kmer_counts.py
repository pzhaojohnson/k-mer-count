from calc_mean_kmer_counts import calc_mean_kmer_counts


def calc_std_devs_of_kmer_counts(kmer_counts_list):
    """Returns a dictionary of kmer count standard deviations.

    The returned dictionary is keyed by kmer.

    Input kmer counts dictionaries should also be keyed by kmer.

    Returns an empty dictionary for an empty list of kmer counts
    dictionaries.

    Arguments:
    kmer_counts_list -- a list of kmer counts dictionaries
    """
    if len(kmer_counts_list) == 0:
        return {}
    means = calc_mean_kmer_counts(kmer_counts_list)
    std_devs = {}
    for kmer, mu in means.items():
        numerator = 0
        for kmer_counts in kmer_counts_list:
            xi = kmer_counts[kmer] if kmer in kmer_counts else 0
            numerator += (xi - mu) ** 2
        N = len(kmer_counts_list)
        std_devs[kmer] = (numerator / N) ** 0.5
    return std_devs
