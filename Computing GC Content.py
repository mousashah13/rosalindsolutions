def gc_content(file_path):
    # create an empty dictionary to store the DNA strings with their respective IDs
    dna_strings = {}
    # open the file and read it line by line
    with open(file_path, 'r') as file:
        # set a flag for the ID line
        id_flag = False
        # initialize an empty string to store the current DNA string
        dna_string = ''
        # loop through each line in the file
        for line in file:
            # if the line starts with '>', it's an ID line
            if line.startswith('>'):
                # if the ID flag is True, it means we have finished reading a DNA string
                if id_flag:
                    # add the DNA string to the dictionary with its corresponding ID as the key
                    dna_strings[dna_id] = dna_string
                    # reset the DNA string
                    dna_string = ''
                # set the ID flag to True
                id_flag = True
                # remove the '>' character from the line and store the ID
                dna_id = line.strip()[1:]
            # if the line does not start with '>', it's a DNA string line
            else:
                # add the line to the current DNA string
                dna_string += line.strip()
        # after looping through all the lines, add the last DNA string to the dictionary
        dna_strings[dna_id] = dna_string
    # initialize a variable to store the DNA ID with the highest GC-content
    highest_gc_id = ''
    # initialize a variable to store the highest GC-content
    highest_gc_content = 0
    # loop through the DNA strings in the dictionary
    for dna_id, dna_string in dna_strings.items():
        # calculate the GC-content of the DNA string
        gc_count = sum([1 for nucleotide in dna_string if nucleotide in ['C', 'G']])
        gc_content = gc_count / len(dna_string) * 100
        # if the GC-content of the current DNA string is higher than the highest GC-content
        if gc_content > highest_gc_content:
            # update the highest GC-content
            highest_gc_content = gc_content
            # update the DNA ID with the highest GC-content
            highest_gc_id = dna_id
    # return the DNA ID with the highest GC-content and the highest GC-content
    return highest_gc_id, highest_gc_content
