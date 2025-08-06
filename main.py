from DNAToolkit import *
import random

# Creating a random DNA sequence for testing:
randDNASeq = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNASeq)
print(countNucFrequency(DNAStr))
