def generate_all_one_mers(IUPAC=False):
    """Returns a list of all one-mers.

    Keyword arguments:
    IUPAC -- whether to include the special IUPAC codes (default False)
    """
    one_mers = ['A', 'T', 'G', 'C']
    if IUPAC:
        one_mers += ['R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N']
    return one_mers
