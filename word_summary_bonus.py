from sys import argv

script, filename = argv

target = open(filename)

indata = target.read()

indata = indata.replace(".", "").replace("(", "").replace(")", "").replace("\n", "").replace("!", "").replace(",", "")

word_list = indata.split(" ")

# print word_list

counts = {}

for word in word_list:
    counter = counts.get(word, 0)
    counts[word] = counter + 1

# sorted list with highest count first due to reverse = True
# we include "key = lambda(key, val): val" => to sort by key's value
sorted_word_list = sorted(counts.items(), key = lambda(key, val): val, reverse=True)

# print sorted_word_list[:10]

for word, count in sorted_word_list[:10]:
    print "'%s' appeared %d times." % (word, count)



# for word, counts in counts.items():
#     print "%s: %d" % (word, counts)
