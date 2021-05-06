
sentence = input("Enter a sentence ")
sentence = ''.join([c for c in sentence if c not in ("!","£","$","%","^","&","*","(",")","{","}","[","]",":",";","@","~","#","<",">","?","/","_","-","=","+",".",",","'")])
words = sentence.lower().split() #Splits the numbers/words up so you can see them individually.
another = [0]
if len(sentence) > 100:
    print ("Error Only 100 characters allowed")
for count, i in enumerate(words):
    if words.count(i) < 2:
        another.append(max(another) + 1) #adds +1 each time a word is used, showing the position of each word.
    else:
        another.append(words.index(i) +1)
        
another.remove(0)
list = (another, words)
file = open("Text.txt", "a+")
file = open("Text.txt", "r+")
file.truncate()
file.write(str(list))

file.close() #prints the number that word is in.
