import collections
Nucleotides = ["A", "T", "G", "C"]
DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


# DNA validation
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "T": 0, "G": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))


def transcription(seq):
    return seq.replace("T", "U")


def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq][::-1])
