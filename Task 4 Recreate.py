file = open("unique.txt", "r")
uniquewords = file.read()
file.close()
file2 = open("words.txt", "r")
sentence =file2.read()
file2.close()
for word in sentence:
    if word not in uniquewords:
        uniquewords.append(word)
positions = [uniquewords.index(word) for word in sentence]
recreated = " ".join([uniquewords[i] for i in positions])
print ("sentence recreate from positions: " )
print (recreated)
