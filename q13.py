file = open('a.txt','r')

file1 = open('file1.txt','w')
file2 = open('file2.txt','w')

lineCount = 0
wordCount = 0
charCount = 0

freq = {}

allWords = []

for line in file : 
    lineCount += 1
    charCount += len(line)

    words = line.split()
    allWords.extend(words)
    wordCount += len(words)

    for ch in line:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    if lineCount%2 == 0:
        file1.write(line)
    else:
        file2.write(line)

print("Total number of characters : {}".format(charCount))
print("Total number of words      : {}".format(wordCount))
print("Total number of lines      : {}".format(lineCount))


print("Frequency of each character : ")
for ch in freq.keys():
    print("{} : {}".format(ch, freq[ch]))

allWords.reverse()
print("Words in reverse order : ")
print(allWords)