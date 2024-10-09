dna_sequence = input()

if 1<=len(dna_sequence)<=10**6:
    max_rep = 1
    current_rep = 1
    for i in range(len(dna_sequence)-1):
        if dna_sequence[i] == dna_sequence[i+1]:
            current_rep +=1
            if current_rep>max_rep:
                max_rep = current_rep
        else:
            current_rep = 1
    print(max_rep)
else:
    pass