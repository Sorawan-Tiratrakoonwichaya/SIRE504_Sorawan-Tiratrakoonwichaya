# SeqMan module
def reverseSeq(seq):
    return seq[::-1]

def complementSeq(seq):
    compl = {"A": "T", "T": "A",
             "G": "C", "C": "G"}
    complementary = "".join([ compl[base] for base in seq ])
    return complementary

def reverseComplementSeq(seq):  # got bugs #เรียบร้อย
    """
    This function takes a DNA sequence as input and returns its reverse complement.
    
    The reverse complement is generated by first reversing the sequence and then 
    replacing each nucleotide with its complement:
    - 'A' becomes 'T'
    - 'T' becomes 'A'
    - 'C' becomes 'G'
    - 'G' becomes 'C'

    Parameters:
    seq (str): The input DNA sequence (e.g., "ATGC").

    Returns:
    str: The reverse complement of the input DNA sequence.
    """
    revComp = complementSeq(reverseSeq(seq))
    return revComp

def dna2rna(seq): # got bugs #เรียบร้อย
    """
    This function converts a DNA sequence to an RNA sequence.
    
    In RNA, the nucleotide thymine ('T') found in DNA is replaced by uracil ('U').
    This function will replace all occurrences of 'T' in the DNA sequence with 'U' 
    to produce the corresponding RNA sequence.

    Parameters:
    seq (str): The input DNA sequence (e.g., "ATGC").

    Returns:
    str: The corresponding RNA sequence with 'T' replaced by 'U'.
    """
    RNA = []
    for dna in seq:
        if dna == "T":
            RNA.append("U")
        else:
            RNA.append(dna)
    RNA_str = "".join(RNA)
    return RNA_str

def dna2protein(seq):
    DNA_Codons = loadCodons()
    protein = ""
    for i in range(0,len(seq),3):
        dna = seq[i:i+3]
        protein += DNA_Codons.get(dna, "")
    return protein

def loadCodons():
    DNA_Codons = {
        # 'M' - START, '_' - STOP
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "TGT": "C", "TGC": "C",
        "GAT": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "TTT": "F", "TTC": "F",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "CAT": "H", "CAC": "H",
        "ATA": "I", "ATT": "I", "ATC": "I",
        "AAA": "K", "AAG": "K",
        "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "ATG": "M",
        "AAT": "N", "AAC": "N",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAA": "Q", "CAG": "Q",
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "TGG": "W",
        "TAT": "Y", "TAC": "Y",
        "TAA": "_", "TAG": "_", "TGA": "_"
    }
    return DNA_Codons

if __name__ == "__main__":
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    seq = seq.upper()
    print(reverseComplementSeq(seq))
    print(dna2rna(seq))
    print(dna2protein(seq))