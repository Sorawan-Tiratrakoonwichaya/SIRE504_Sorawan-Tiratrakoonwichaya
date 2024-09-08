# SeqCal module
def countBase(seq, base): # got bugs #เรียบร้อย
    """
    This function counts the number of occurrences of a specific base in a given DNA sequence.
    
    Parameters:
    seq (str): The DNA sequence in which to count the base (e.g., "ATGC").
    base (str): The base to count within the sequence (e.g., "A").
    
    Returns:
    int: The number of times the specified base appears in the sequence.
    """
    base_count = 0
    for dna in seq:
        if base == dna:
            base_count+=1

    return base_count

def gcContent(seq): # got bugs #เรียบร้อย
    """
    This function calculates the GC content of a DNA sequence.
    
    The GC content is the percentage of nucleotides in the sequence that are either 
    guanine (G) or cytosine (C). It is calculated as:
    
    GC Content = (Number of G + Number of C) / (Total Number of Bases) * 100
    
    Parameters:
    seq (str): The DNA sequence for which to calculate GC content (e.g., "ATGC").
    
    Returns:
    float: The GC content as a percentage of the total sequence length.
    """
    # G+C/(A+T+G+C)
    # use countBase function to count bases

    GC_content = (countBase(seq,"G")+countBase(seq,"C"))/(countBase(seq,"A")+countBase(seq,"T")+countBase(seq,"G")+countBase(seq,"C"))
    return GC_content

def atContent(seq): # got bugs #เรียบร้อย
    """
    This function calculates the AT content of a DNA sequence.
    
    The AT content is the percentage of nucleotides in the sequence that are either 
    adenine (A) or thymine (T). It is calculated as:
    
    AT Content = (Number of A + Number of T) / (Total Number of Bases) * 100
    
    Parameters:
    seq (str): The DNA sequence for which to calculate AT content (e.g., "ATGC").
    
    Returns:
    float: The AT content as a percentage of the total sequence length.
    """
    # A+T/(A+T+G+C)
    # use countBase function to count bases

    AT_content = (countBase(seq,"A")+countBase(seq,"T"))/(countBase(seq,"A")+countBase(seq,"T")+countBase(seq,"G")+countBase(seq,"C"))
    return AT_content

def countBasesDict(seq): # got bugs #เรียบร้อย
    """
    Counts the occurrences of each nucleotide base in a given DNA sequence.

    Parameters:
    seq (str): The DNA sequence to be analyzed. The sequence should consist of characters representing nucleotide bases (e.g., 'A', 'T', 'C', 'G').

    Returns:
    dict: A dictionary where the keys are the nucleotide bases and the values are the counts of each base in the sequence.

    Example:
    >>> countBasesDict("ATCGATCGA")
    {'A': 3, 'T': 2, 'C': 2, 'G': 2}
    """
    basesM = {}
    # Bases = "ATGC"
    for base in seq:
        basesM[base] = countBase(seq,base)
    return basesM

if __name__ == "__main__":
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    seq = seq.upper()
    print(countBase(seq,"A"))
    print(countBase(seq,"T"))
    print(countBase(seq,"G"))
    print(countBase(seq,"C"))
    print(gcContent(seq))
    print(atContent(seq))
    print(countBasesDict(seq))
