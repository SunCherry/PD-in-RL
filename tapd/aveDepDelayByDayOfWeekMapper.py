import sys
import csv
 
# Create a dictionary to map words to counts
wordcount = {}
 
# Get input from stdin
for line in sys.stdin:
    #Remove spaces from beginning and end of the line
    line = line.strip()
 
    s = line.split(',', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
## the fourth item is day-of-week, so we extract this value
    try:
        wordcount[s[3]] = wordcount[s[3]]+count
    except:
        wordcount[s[3]] = count
 
# Write the tuples to stdout
# Currently tuples are unsorted
for word in wordcount.keys():
    print '%s\t%s'% ( word, wordcount[word] )
