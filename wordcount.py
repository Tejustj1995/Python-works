file = open("C:/Users/TJ/PycharmProjects/proj1/tejus.txt", "r+")
wordcount = {}
word = 0
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print(word, wordcount, "\n")
file.close()
