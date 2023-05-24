from .generate_all_one_mers import generate_all_one_mers


def generate_all_kmers(k=1, IUPAC=False):
    """Returns a list of all sequences of size k.

    Keyword arguments:
    k -- the size of sequences to generate (default 1)
    IUPAC -- whether to include the special IUPAC codes (default False)
    """
    one_mers = generate_all_one_mers(IUPAC=IUPAC)
    all_mers = [one_mers]
    for i in range(2, k + 1):
        # all sequences of size i - 1
        minus_one_mers = all_mers[i - 2]
        # all sequences of size i
        imers = [mer + c for mer in minus_one_mers for c in one_mers]
        # append all sequences of size i
        all_mers.append(imers)
    # return all sequences of size k
    return all_mers[k - 1]
