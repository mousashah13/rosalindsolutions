def reverse_complement(s):
    complement_map = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement_map[base] for base in s[::-1]) 
  
 #s[::-1] reverses the order of the nucleotides in the DNA string s.
