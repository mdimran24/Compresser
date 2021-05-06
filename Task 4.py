sentence = raw_input("Enter a sentence: ")
sentence = sentence.lower().split()
uniquewords = []
for word in sentence:
    if word not in uniquewords:
        uniquewords.append(word)

positions = [uniquewords.index(word) for word in sentence]

file = open("unique.txt", "a+")
file = open("unique.txt", "r+")
file.truncate()
file.write(str(uniquewords))
file.close()
file2 = open("words.txt", "a+")
file2 = open("words.txt", "r+")
file2.truncate()

file2.write(str(sentence))
file2.close()



print (positions)
