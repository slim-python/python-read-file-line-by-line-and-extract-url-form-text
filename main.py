import json
import re
# read line by linee
file1 = open('index.json', 'r')
Lines = file1.readlines()

# write file to text file
file3 = open('urls.txt', 'w')
for line in Lines:
    line = re.search("(?P<url>https?://[^\s]+)", line).group("url")
    file3.write(line + '\n')
file3.close()
