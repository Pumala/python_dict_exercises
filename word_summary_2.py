from sys import argv

script, filename = argv

target = open(filename)

indata = target.read()

indata = indata.replace(".", "").replace("(", "").replace(")", "").replace("\n", "").replace("!", "").replace(",", "")

word_list = indata.split(" ")

counts = {}

for word in word_list:
    counter = counts.get(word, 0)
    counts[word] = counter + 1

print counts

for word, counts in counts.items():
    print "%s: %d" % (word, counts)
