


#loop thorugh the words
#get word and lenth and store it in a list for the first five words.
#get a list of five words
# read in next word
# if word is bigger than smallest then replace that one

# or we can sort the list from largest to smallest and print the top 5
words = []
with open('/usr/share/dict/words', 'r') as f:
            words = f.read().splitlines()

            sorted_words = words.sort(key=len, reverse = True)
            for i in range(5):
                        print(words[i])
