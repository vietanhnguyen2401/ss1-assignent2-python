from collections import defaultdict
import json

INFILE = 'sample.txt'
OUTFILE = 'sample_out_1.json'

words = defaultdict(int)

#Create a dictionary with a key that represents the number of instances of that term 
# and a value that represents the number of occurrences of that word.
with open(INFILE) as infile:
    for line in infile:
        for word in line.strip().lower().split():
            # Increment count of word 
            if word in words:
                words[word] = words[word] + 1
            # Add the word to dictionary
            else:
                words[word] = 1

# Print the contents of dictionary
with open(OUTFILE, 'w') as outfile:
    outfile.write(json.dumps(words, indent=4))

