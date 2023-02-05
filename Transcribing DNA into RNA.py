def count_nucleotides(s):
    return s.count('A'), s.count('C'), s.count('G'), s.count('T')

def transcribe_DNA_to_RNA(t):
    return t.replace('T', 'U')

t = "ATGCTTCAGAAAGGTCTTACG"
s = transcribe_DNA_to_RNA(t)
result = count_nucleotides(s)
print(*result)
