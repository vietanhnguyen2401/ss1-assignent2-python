from collections import defaultdict
import json

INFILE = 'sample1.txt'
OUTFILE = 'sample_out_3.json'

words = defaultdict(lambda: 0)

#Create a dictionary with a key that represents the number of instances of that term 
# and a value that represents the number of occurrences of that word.
with open(INFILE) as infile:
    for line in infile:
        for word in line.strip().lower().split():
            # Increment count of word
            if word in words:
                words[word] = words[word] + 1 
            #Add the word to dictionary 
            else:
                words[word] = 1

# count total number of words
wordcount = sum(words.values())

#create a list of packets (percentage, word) to sort by percentage, 
# then create the final output dictionary with values in the correct order.
j_cal = {key: round(value/ wordcount * 100.0, 2) for key, value in words.items()}

#create a list of packets (percentage, word) to sort by percentage, 
# then create the final output dictionary with values in the correct order.
j_out = {key: -value for value, key in sorted([(-value, key) for key, value in j_cal.items()])}

# Print the contents of dictionary into JSON file
with open(OUTFILE, 'w') as outfile:
    outfile.write(json.dumps(j_out,indent=4))