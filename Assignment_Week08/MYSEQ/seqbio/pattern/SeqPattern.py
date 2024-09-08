# SeqPattern module
import re

def cpgSearch(seq):
    cpgs = []
    for m in re.finditer(r'CG', seq, re.I):
        cpgs.append((m.group(), m.start(), m.end()))
    return cpgs

def enzTargetsScan(seq, enz): # got bugs #เรียบร้อย
    """
    Scans a DNA sequence for recognition sites of a specified restriction enzyme.

    Parameters:
    seq (str): The DNA sequence in which to search for enzyme recognition sites.
    enz (str): The name of the restriction enzyme whose recognition site is to be searched.

    Returns:
    list of tuples: A list of tuples where each tuple contains:
        - The matched sequence (recognition site) as a string.
        - The start position of the match in the DNA sequence.
        - The end position of the match in the DNA sequence.
    
    If the specified enzyme is not found in the `resEnzyme` dictionary, an empty list is returned.

    Example:
    >>> enzTargetsScan('GAATTCCGGAATTCTAGC', 'EcoRI')
    [('GAATTC', 0, 6), ('GAATTC', 8, 14)]
    """
    
    resEnzyme = dict(EcoRI='GAATTC', BamHI='GGATCC', 
                 HindIII='AAGCTT',AccB2I='[AG]GCGC[CT]',
                 AasI='GAC[ATCG][ATCG][ATCG][ATCG][ATCG][ATCG]GTC',
                 AceI='GC[AT]GC')
    enz_target = []
    if enz in resEnzyme:
        for m in re.finditer(resEnzyme[enz],seq):
            enz_target.append((m.group(),m.start(),m.end()))
    return enz_target

if __name__ == "__main__":
    # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    seq = 'GAATTCCGGAATTCTAGC'
    seq = seq.upper()
    print(cpgSearch(seq))
    print(enzTargetsScan(seq,'EcoRI'))