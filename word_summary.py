from sys import argv

script, filename = argv

target = open(filename)

indata = target.read()

indata = indata.replace(".", "").replace("(", "").replace(")", "").replace("\n", "").replace("!", "").replace(",", "")


word_list = indata.split(" ")

print word_list

counts = {}

for word in word_list:
    counter = counts.get(word, 0)
    counts[word] = counter + 1

for word, count in counts.items():
    print "%d: %s" % (count, word)
