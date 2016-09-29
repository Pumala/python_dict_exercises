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

# for word, counts in counts.items():
#     print "%s: %d" % (word, counts)
# v1
# def mykey(entry):
    # return entry[1]
entries = counts.items()
# v2
entries.sort(key = lambda entry: entry[1], reverse=True)
print entries[:10]

word_count = counts.items()

for word, count in word_count:
    print "%s appeared %d times" % (word, count)














# print counts
# counts_list = counts
# freq_words_list = []
# counter = 10
# highest_count = 2
# max_count = 20
# freq_word = ""
#
# while counter > 0:
#     for word, counts in counts_list.items():
#         print "high %d" % highest_count #3
#         print "max %d" % max_count #3
#         print "counts %d" % counts #1
#         if counts > highest_count and counts < max_count:
#             # print "hi"
#             highest_count = counts
#             freq_word = word
#             max_count = counts
#     freq_words_list.append(freq_word)
#     counter -= 1
#
# print freq_words_list





    # freq_count = 1
    # frequent_words_list = {}
    #
    # word_counts = []
    # word_list = []
    # freq_words = []
    #
    # for word, count in counts.items():
    #     word_counts.append(count)
    #
    # for word, counts in counts.items():
    #     word_list.append(word)
    # limit = 0
    # while limit < 10:
    #     highest_count = 0
    #     counter = 0
    #     for num in word_counts:
    #         if num > highest_count:
    #             highest_count = num
    #             index = counter
    #         counter += 1
    #
    #     print highest_count
    #     print index
    #     print word_list[index]
    #     frequent_words_list[word_list[index]] = highest_count
    #     del word_counts[index]
    #     del word_list[index]
    #     print frequent_words_list
    # limit += 1

# print word_list

# freq_words_list = []



# for word, counts in counts.items():
#     if counts > freq_count:
#         freq_count = counts
#         freq_word = word
#
# frequent_words_list[freq_word] = freq_count
# del counts[freq_word]
# print frequent_words_list
# print counts


# freq_count = 1
# frequent_words_list = {}
#
# for word, counts in counts.items():
#     if counts > freq_count:
#         freq_count = counts
#         freq_word = word
#
# frequent_words_list[freq_word] = freq_count
# del counts[freq_word]
# print frequent_words_list
